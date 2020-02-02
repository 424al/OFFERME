from crispy_forms.helper import FormHelper
from django import forms


from .models import Item
from tinymce.widgets import TinyMCE


class AddItem(forms.ModelForm):
	helper= FormHelper()
	helper.form_show_labels = False
	class Meta:
		model = Item
		fields = ('title','image','description','price','location')
