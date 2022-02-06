from django.db import models


class Memes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField( max_length=50, blank = True, null = True)

    def __str__(self):
        return self.name

