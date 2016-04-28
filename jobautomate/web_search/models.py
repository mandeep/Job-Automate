from django.db import models


class Resume(models.Model):
    upload = models.FileField(upload_to=None)
