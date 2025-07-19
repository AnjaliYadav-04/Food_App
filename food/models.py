from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.item_name

    user_name=models.ForeignKey(User,on_delete=models.CASCADE,default=1)#we add foreign key belong to user that establish connection between user and item
    item_name=models.CharField(max_length=200)
    item_desc=models.CharField(max_length=200)
    item_price=models.IntegerField(default=0)
    item_image=models.CharField(max_length=500,default="https://www.shutterstock.com/image-illustration/coming-soon-concept-image-text-600nw-2402613961.jpg")
    
    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
    