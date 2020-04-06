from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    date_posted = models.DateField(null=True)
    blog_img = models.ImageField(upload_to='images/') 
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('post-detail', args=[str(self.id)])

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('category-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.name

