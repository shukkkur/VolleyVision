from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def home(request):
    return render(request, 'home.html')


def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'upload.html')
