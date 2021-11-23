from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Posts(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank = True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-pub_date',)