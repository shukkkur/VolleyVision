import os
import shutil
import glob
import subprocess
from .forms import UploadFileForm
from django.shortcuts import render, redirect
from django.http import FileResponse, Http404
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect


def clean_cache(request):
    media_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media')
    if os.path.exists(media_path):
        shutil.rmtree(media_path)
    return HttpResponseRedirect('/')



def home(request):
    return render(request, 'home.html')


def upload(request):
    clean_cache(request)
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            processing = form.cleaned_data['processing']
            file_type = form.cleaned_data['file_type']

            folder_name = "media"
            output_folder = "media/Output"

            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            # Save the uploaded file
            filepath = os.path.join('media', file.name)
            with open(filepath, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

            # Initialize the input path for the first process
            input_path = filepath
            extention = os.path.splitext(file.name)[1]
            for i, option in enumerate(processing):
                # Generate a unique output path for each process
                fname = f'output_{i}{extention}'
                output_path = os.path.join(output_folder, fname)

                if option == 'volleyball':
                    if file_type == 'video':
                        command = ["python", "Stage I - Volleyball/volley_detect.py", "--input_video_path", input_path, "--output_video_path", output_path]
                    elif file_type == 'image':                    
                        command = ["python", "Stage I - Volleyball/roboflow_detect.py", "--input_path", input_path, "--output_path", output_path]
                    subprocess.run(command)
                    input_path = output_path

                elif option == 'action':
                    command = ["yolo", "predict", "model=Stage II - Players & Actions/actions/yV8_medium/weights/best.pt", f"source={input_path}", "show_conf=False", "show_labels=True", "conf=0.5", 'project=media', 'name=Y_action']
                    subprocess.run(command)

                    input_name = os.path.split(input_path)[1]
                    os.rename(os.path.join(folder_name, 'Y_action', input_name), output_path)
                    input_path = output_path

                elif option == 'player':
                    command = ["yolo", "predict", "model=Stage II - Players & Actions/players/yV8_medium/weights/best.pt", f"source={input_path}", "show_conf=False", "show_labels=False", "conf=0.7", 'project=media', 'name=Y_player', 'max_det=12']
                    subprocess.run(command)

                    input_name = os.path.split(input_path)[1]
                    os.rename(os.path.join(folder_name, 'Y_player', input_name), output_path)
                    input_path = output_path

                elif option == 'court':
                    command = ["python", "Stage III - Court Detection/court_detect.py",  "--input_path", input_path, "--output_path", output_path]
                    subprocess.run(command)
                    input_path = output_path  # Update the input path for the next process

            # Redirect to the results page
            request.session['final_output_path'] = output_path
            return redirect('volleyapp:result')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def result(request):
    # Get the path of the processed file from the session
    file_path = request.session.get('final_output_path', 'default_value')
    return render(request, 'result.html', {'file_path': file_path})


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'), content_type='video/mp4')
        response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
        return response
    raise Http404
