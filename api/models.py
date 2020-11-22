from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=50, null=False, blank=False)


class Images(models.Model):
    '''
    We can also use content delivery network to store images
    and use image field to store location of images.
    '''
    image = models.ImageField(upload_to="images/")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    date_added = models.DateField(auto_now_add=True)