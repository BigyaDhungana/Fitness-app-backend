from django.forms import ModelForm
from exercises.models import Exercises,PreDefinedWorkoutNames,PreDefinedWorkouts
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

class AddWorkoutNameForm(ModelForm):
    class Meta:
        model = PreDefinedWorkoutNames
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 mb-4",
                }
            ),
        }

class AddExerciseToWorkoutForm(forms.Form):
    exercise=forms.ModelChoiceField(queryset=Exercises.objects.all(),empty_label="Select a Exercise")
    reps=forms.IntegerField(label="Reps/Time(in seconds)")
    type=forms.ChoiceField(choices=(('Reps','Reps'),('Time','Time')),widget=forms.RadioSelect)