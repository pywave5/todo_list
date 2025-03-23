from django import forms
from .models import Task
from django.core.exceptions import ValidationError

def validate_image_file(file):
    if not file.name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
        raise ValidationError("Можно загружать только изображения (PNG, JPG, JPEG, GIF, WEBP).")

class TaskForm(forms.ModelForm):
    image = forms.ImageField(label="Фото", required=False, validators=[validate_image_file])
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'deadline', 'image']
        labels = {
            'image': 'Фото',
        }
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }