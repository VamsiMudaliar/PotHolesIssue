from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class AddIssue(models.Model):
    issue_id = models.AutoField(primary_key=True)
    issue_title = models.CharField(max_length=300, default="")
    location = models.CharField(max_length=50, default="")
    upvotes = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    pub_date = models.DateTimeField(default=timezone.now)
    issue_img = models.ImageField(
        upload_to='UserComplaint/images/', default="")
    issue_status = models.CharField(max_length=50, default="open")

    def __str__(self):
        return self.issue_title
