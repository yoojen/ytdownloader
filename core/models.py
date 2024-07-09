from django.db import models

# Create your models here.
class SearchQueries(models.Model):
    query=models.CharField(max_length=256)
    no_returned_rs=models.PositiveIntegerField(default=0)
    date_mdeia_uploaded=models.DateTimeField()
    date_created=models.DateTimeField(auto_now_add=True)


class Download(models.Model):
    media_type=models.CharField(max_length=256)
    channel_id=models.CharField(max_length=256)
    date_created=models.DateTimeField(auto_now_add=True)