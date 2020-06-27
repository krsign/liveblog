from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    
    def __str__(self):
        return self.name


class Post(models.Model):
    statuses = [('D', 'Draft'), ('P', 'Publish')]

    title = models.CharField(max_length=250)
    content = RichTextField(blank=True, null=True)
    # content = models.TextField()
    status = models.CharField(max_length=1 ,choices=statuses, default='D')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    image = models.ImageField(upload_to='blog/', blank=True)
    slug = models.SlugField(unique=True, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
     
    def __str__(self):
        return self.title

    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('post-detail', args=[self.slug])
