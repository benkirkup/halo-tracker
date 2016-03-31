from django.db import models

class gameVariants(models.Model):
    name = models.CharField(max_length=30, default='', blank=False, null=False)
    contentId = models.CharField(max_length=36, default='', blank=False, null=False)

    def __str__(self):
        return self.name

