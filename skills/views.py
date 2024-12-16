# views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from .models import Images, Skills
import ollama
import json

def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the uploaded file temporarily
            uploaded_file = form.cleaned_data['file']
            image_instance = Images(image=uploaded_file)  # Create a new Images instance
            image_instance.save()  # Save the instance (this will save the file)

            # Now you can get the file path to send to Ollama
            file_path = image_instance.image.path  # Get the file path

            # Send the file to Ollama
            send_message(file_path, request.user)

            return HttpResponseRedirect('/')  # Redirect to a success page or home
    else:
        form = UploadFileForm()

    return render(request, 'upload.html', {'form': form})

def send_message(file_path, user):
    print("Sending file to Ollama:", file_path)

    # You can read the file as bytes and send it to Ollama
    with open(file_path, 'rb') as file:
        file_bytes = file.read()

    # Send the file as bytes to Ollama
    res = ollama.chat(
        model='llava',
        messages=[{
            'role': 'user',
            'content': 'What is the skill practiced in the photo, Return only with a JSON object structured as follows: {"skill":skill}, for example: {"skill": "Juggling"}',
            'images': [file_bytes]
        }]
    )
    result = res["message"]["content"]

    try:
        json_result = json.loads(result)
        print(result)
    except Exception as e:
        print(result)
        print(e)
        send_message(file_path, user)
        return None

    skill_name = json_result.get("skill", None)
    
    if not skill_name:
        print("No skill found in the response.")
        return

    print(f"Skill identified: {skill_name}")

    if not user.skills.filter(name=skill_name).exists():
        new_skill = Skills.objects.create(
            user = user,
            name = skill_name,
            level = 1,
            current_exp = 0,
            rank = "novice",
        )

        new_skill.save()

        print(f"New skill '{skill_name}' created for user {user.username}.")
    else:

        skill = user.skills.filter(name=skill_name).first()

        if skill:
            print(skill)
            print(skill.name)
            print(skill.current_exp)
            print(skill.rank)
            print(skill.level)
        else:
            print("skill not found")

        res = ollama.chat(
            model="llava",
            messages=[
                {
                    'role': 'user',
                    'content': f'Analyze the photo and determine the difficulty level of the skill being performed, for a person of skill level {skill.level}/60, with exponential growth, and a {skill.rank} in {skill}. Respond only with a JSON object structured as follows: {'difficulty': "difficulty_level"}, where difficulty_level is a number from 1 (easy) to 10 (very hard), use only integers.'
                }
            ]
        )
        

        print(f"Skill '{skill_name}' already exists for user {user.username}.")

    
    
