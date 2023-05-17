from django import forms

class UploadFileForm(forms.Form):
    PROCESSING_CHOICES = [
        ('volleyball', 'Volleyball Detection'),
        ('action', 'Action Recognition'),
        ('player', 'Player Detection'),
        ('court', 'Court Detection'),
    ]
    FILE_TYPE_CHOICES = [
        ('image', 'Image'),
        # Removed 'video' choice
    ]
    file = forms.FileField()
    processing = forms.MultipleChoiceField(choices=PROCESSING_CHOICES, widget=forms.CheckboxSelectMultiple)
    file_type = forms.ChoiceField(choices=FILE_TYPE_CHOICES)
