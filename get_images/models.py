from django.db import models


class Image(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.url
