from django.forms import ModelForm
from .models import Stories

class Addstory(ModelForm):
	class Meta:
		model = Stories
		fields = ['parent','title', 'body', 'image']
