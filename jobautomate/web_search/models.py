from django.db import models


class ResumeModel(models.Model):
    resume = models.FileField(upload_to='uploads/')
