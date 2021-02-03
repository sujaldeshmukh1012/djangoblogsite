from django import forms
from post.models import Post

class NewPostForm(forms.ModelForm):
	image = forms.ImageField(required=True)
	caption = forms.CharField(widget=forms.Textarea(attrs={'class': 'summernote'}), required=True)
	tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control inputtags','type':'text','placeholder':'Add COMMA(,) to saperate tags'}), required=True)
	title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control '}), required=True)
	class Meta:
		model = Post
		fields = ('image', 'caption', 'tags','title')	


		