from django import forms
from blog.models import Post, Category
from django.utils.text import slugify
from django.core.exceptions import ObjectDoesNotExist


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    phone = forms.RegexField(required=False, regex='^[6-9]\d{9}$')

    def clean(self):
        cleaned_data = super().clean()
        # print(cleaned_data)

        if not (cleaned_data.get('email') or cleaned_data.get('phone')):
            raise forms.ValidationError('Please Enter either email or phone!', code='invalid')


    def clean_email(self):
       data = self.cleaned_data['email']
       if '@' not in data:
           raise forms.ValidationError('invalid domain', code='invalid')

class PostForm(forms.ModelForm):
   
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'status', 'image']
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        slug = slugify(title)
        try:
            post_obj = Post.objects.get(slug=slug )
            raise forms.ValidationError('Title already exist!', code='Invalid title')
        
        except ObjectDoesNotExist:
            return title
            
   
