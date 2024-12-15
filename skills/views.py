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
            'content': 'What is the skill practiced in the photo, respond with only with a json object {"skill":skill}',
            'images': [file_bytes]
        }]
    )
    result = res["message"]["content"]

    try:
        json_result = json.loads(result)
    except Exception as e:
        send_message(file_path, user)
        return None

    skill_name = json_result.get("skill", None)
    
    if not skill_name:
        print("No skill found in the response.")
        return

    print(f"Skill identified: {skill_name}")

    if not user.skills.filter(name__iexact=skill_name).exists():
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
        print(f"Skill '{skill_name}' already exists for user {user.username}.")

    
    
