from django.contrib.auth.models import User
from django.db import models


class User(models.Model):
    user_name= models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name

class Category(models.Model):
    name = models.CharField(max_length=100, default="Uncategorized")

    def __str__(self):
        return self.name

class Listing(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=300)
    description = models.TextField()
    image_url = models.URLField(max_length=200, blank=True, null=True)
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return f'{self.title} - {self.description}'

    class Meta:
        ordering = ['-created_at']
    

class Bid(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    bid_amout = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
        return f'{self.user_name} - {self.bid_amout}'

class Comment(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    content = models.TextField()

    
    def __str__(self):
        return f'{self.name} - {self.content}'