from django.contrib import admin
from .models import AddIssue, Comments
# Register your models here.

admin.site.register((AddIssue, Comments))
