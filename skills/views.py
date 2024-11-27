# views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from .models import Images
import ollama

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
            send_message(file_path)

            return HttpResponseRedirect('/')  # Redirect to a success page or home
    else:
        form = UploadFileForm()

    return render(request, 'upload.html', {'form': form})

def send_message(file_path):
    print("Sending file to Ollama:", file_path)

    # You can read the file as bytes and send it to Ollama
    with open(file_path, 'rb') as file:
        file_bytes = file.read()

    # Send the file as bytes to Ollama
    res = ollama.chat(
        model='llava',
        messages=[{
            'role': 'user',
            'content': 'Describe this image',
            'images': [file_bytes]
        }]
    )

    print(res["message"]["content"])  # Print the response from Ollama
