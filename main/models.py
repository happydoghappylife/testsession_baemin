from django.db import models

class Store(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="image/")
    address = models.CharField(max_length=200)
    menu_title = models.CharField(max_length=200)
    menu_image = models.ImageField(upload_to="image/")

    def __str__(self):
        return self.title