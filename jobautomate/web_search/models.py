from django.db import models


class ResumeModel(models.Model):
    upload = models.FileField(upload_to=None)
