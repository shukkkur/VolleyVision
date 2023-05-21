from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import os
import subprocess

def upload_video(request):
    if request.method == 'POST':
        form = UploadVideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.cleaned_data.get('video')
            processing_types = form.cleaned_data.get('processing_types')  # assuming this is a list
            # Save uploaded video to media folder
            video_path = default_storage.save(video.name, video)
            file_path = os.path.join(settings.MEDIA_ROOT, video_path)
            
            # Set initial input and output paths
            input_path = file_path
            output_path = os.path.join(settings.MEDIA_ROOT, 'output.mp4')

            # Loop over selected processing types
            for processing_type in processing_types:
                if processing_type == 'track_volleyball':
                    command = ['python', 'Stage I - Volleyball/volley_track.py', '--input_video_path', input_path, '--output_video_path', output_path]
                elif processing_type == 'track_players':
                    command = ['python', 'Stage II - Players & Actions/players/yV8_medium/weights/best.pt', 'source=' + input_path]
                elif processing_type == 'action_recognition':
                    command = ['python', 'Stage II - Players & Actions/actions/yV8_medium/weights/best.pt', 'source=' + input_path]
                elif processing_type == 'track_court':
                    command = ['python', 'Stage III - Court Detection/court_detect.py', input_path, '--output_path', output_path]
                subprocess.run(command)

                # Set the output of this processing step as the input to the next step
                input_path = output_path

            return redirect('view_results')
    else:
        form = UploadVideoForm()

    return render(request, 'tracker/upload.html', {'form': form})
