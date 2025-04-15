from django.db import models
from django.utils.text import slugify
from user_accounts.models import CustomUser
class Tag(models.Model):
    id=models.AutoField(primary_key=True,editable=False)
    name=models.CharField(max_length=100, unique=True)
    slug=models.SlugField(max_length=100, unique=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        
        
    def __str__(self):
        return f"{self.id} - {self.name}"
    class Meta:
        verbose_name_plural = 'Tags'
        ordering = ['-created_at']
class Blog(models.Model):
    id=models.AutoField(primary_key=True,editable=False)
    title=models.CharField(max_length=200, unique=True)
    description=models.TextField()
    slug=models.SlugField(max_length=200, unique=True, blank=True)
    img=models.ImageField(upload_to='blog_images', blank=True, null=True)
    author=models.ForeignKey('user_accounts.CustomUser', on_delete=models.CASCADE, related_name='blogs')
    tags=models.ManyToManyField('Tag', related_name='blog_Tags', blank=True)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    published=models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.id} - {self.title}"
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name_plural = 'Blogs'
        ordering = ['-created_at']

class Contact(models.Model):
    id=models.AutoField(primary_key=True,editable=False)
   
    First_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=15, blank=True, null=True)
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.id} - {self.name}"
    class Meta:
        verbose_name_plural = 'Contacts'
        ordering = ['-created_at']