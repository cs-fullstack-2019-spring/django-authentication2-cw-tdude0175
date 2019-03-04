from django.contrib.auth.models import User
from django.db import models
# Create your models here.

# Create a blog app that will allows pre-created users to log in and see all posts created/assigned to them.
#
# A user's post should include a username, blog_title, and blog_entry.

class BlogPostModel(models.Model):
    username= models.CharField(max_length=100)
    blog_title= models.CharField(max_length=100)
    blog_entry= models.CharField(max_length=100)
    userIDkey= models.ForeignKey(User, on_delete=models.PROTECT,null=True,blank=True)
    # the [userIDkey] is what is used to compare and get all the necessary posts to use.

    def __str__(self):
        return self.username