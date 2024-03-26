from django.forms import ModelForm
from exercises.models import Exercises
from django import forms

class AddExerciseForm(ModelForm):
    class Meta:
        model=Exercises
        fields="__all__"
        
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500  p-2.5  mb-4",
                
                }
            ),
            "desc": forms.Textarea(
                attrs={
                    "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500  p-2.5  mb-4 items-center"
                }
            ),
            "focus":forms.Select(
                attrs={
                    "class":"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 mb-4",   
                },
            ),
            "gif":forms.ClearableFileInput(
                attrs={
                    "class":" text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50"
                }
            )
          
        }