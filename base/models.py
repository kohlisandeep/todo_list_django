from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    # Foreignkey for one to many relationship because a user can have many posts and
    # on_delete=models.CASCADE is for when user delete then all the post will also be deleted
    # models.SET_NULL is for when the user get deleted then post will be remaining
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=200,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # meta class is for ordering
    class Meta:
        ordering=['complete']




