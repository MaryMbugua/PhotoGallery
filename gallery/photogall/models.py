from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length=60)

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Category(models.Model):
    category_name = models.CharField(max_length=60)

    def __str__(self):
        return self.category_name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
class Image(models.Model):
    image = models.ImageField(upload_to = 'pictures/',blank=True)
    image_name = models.CharField(max_length =60)
    image_description = HTMLField()
    image_location = models.ManyToManyField(Location)
    image_category = models.ManyToManyField(Category)
   
    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_image_by_id(cls):
        images = Image.objects.all()
        return images
    @classmethod
    def search_image(cls,search_term):
        images = cls.objects.filter(location_name_icontains=search_term)
        return images
    @classmethod
    def search_by_category(cls, search_term):
        images = cls.objects.filter(category_name__icontains=search_term)
        return images





    
    