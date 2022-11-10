from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='blog/images/', blank=True)

    def __str__(self):
        return self.title