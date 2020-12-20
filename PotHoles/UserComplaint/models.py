from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


STATUS_OPTIONS = (

    ("Open", "Open"),
    ("Submitted to newpaper", "Submitted to newpaper"),
    ("resolved", "resolved"),
    ("no action taken", "no action taken"),
)


class AddIssue(models.Model):
    issue_id = models.AutoField(primary_key=True)
    issue_title = models.CharField(max_length=300, default="")
    location = models.CharField(max_length=50, default="")
    upvotes = models.ManyToManyField(
        User, default=None, blank=True, related_name="upvotes")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1, related_name="author")
    pub_date = models.DateTimeField(default=now)
    issue_img = models.ImageField(
        upload_to='UserComplaint/images/', default="")
    issue_status = models.CharField(
        choices=STATUS_OPTIONS, default="open", max_length=50)

    def __str__(self):
        return self.issue_title

    @property
    def num_likes(self):
        return self.upvotes.all().count()


class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(AddIssue, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)
