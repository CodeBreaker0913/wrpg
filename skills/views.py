from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import UploadFileForm
from .models import Images, Skills
import ollama
import json

AI_RETURN = {}

def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['file']
            image_instance = Images(image=uploaded_file)
            image_instance.save()
            file_path = image_instance.image.path
            send_message(file_path, request.user)
            return redirect('/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def send_message(file_path, user):
    global AI_RETURN
    
    try:
        with open(file_path, 'rb') as file:
            file_bytes = file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    prompt = 'Identify the skill in the image. Return JSON: {"skill": "SkillName"}'
    AI_RETURN = ollama_sender(prompt, file_bytes, "skill")
    
    if not AI_RETURN:
        print("Failed to retrieve skill data from Ollama.")
        return
    
    skill_name = AI_RETURN.get('skill')
    if not skill_name:
        print("Skill name missing from response.")
        return
    
    skill, created = Skills.objects.get_or_create(
        user=user, name=skill_name,
        defaults={"level": 1, "current_exp": 0, "rank": "novice"}
    )

    if not created:
        prompt = f"Determine difficulty (1-10) for {skill.name} at level {skill.level}. Return JSON: {"difficulty": 5}"
        difficulty_data = ollama_sender(prompt, file_bytes, "difficulty")
        difficulty = int(difficulty_data.get('difficulty', 1))
        
        prompt = f"Rate performance (1-5) for {skill.name} at level {skill.level}. Return JSON: {"wellness": 3}"
        wellness_data = ollama_sender(prompt, file_bytes, "wellness")
        wellness = int(wellness_data.get('wellness', 1))
        
        exp_gained = wellness * difficulty * 10
        skill.add_exp(exp_gained)
        skill.save()

def ollama_sender(content, image, name, retries=3):
    global AI_RETURN
    for attempt in range(retries):
        try:
            res = ollama.chat(
                model="llava",
                messages=[
                    {'role': 'user', 'content': content, 'images': [image]}
                ]
            )
            result = res.get("message", {}).get("content", "{}")
            return json.loads(result)
        except Exception as e:
            print(f"Ollama request failed (attempt {attempt+1}): {e}")
    return {}
