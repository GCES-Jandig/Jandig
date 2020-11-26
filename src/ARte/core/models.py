from django.db import models
from users.models import Artwork, Profile
from datetime import datetime
import urllib

class Artwork2(models.Model):
    name = models.CharField(unique=True, max_length=50)
    patt = models.CharField(default="hiro", max_length=50)
    gif = models.CharField(default="peixe", max_length=50)
    scale = models.CharField(default="1 1", max_length=50)
    position = models.CharField(default="0 0 0", max_length=50)
    rotation = models.CharField(default="270 0 0", max_length=50)

class Exhibit(models.Model):
    owner = models.ForeignKey(Profile,on_delete=models.DO_NOTHING,related_name="exhibits")
    name = models.CharField(unique=True, max_length=50)
    slug = models.CharField(unique=True, max_length=50)
    artworks = models.ManyToManyField(Artwork,related_name="exhibits")
    creation_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def artworks_count(self):
        return self.artworks.count()

    @property
    def date(self):
        return self.creation_date.strftime("%d/%m/%Y")
    
    @property
    def exhibits_count(self):
        from core.models import Exhibit
        return Exhibit.objects.filter(artworks__augmented=self).count()

    @property
    def exhibits_list(self):
        from core.models import Exhibit
        return Exhibit.objects.filter(artworks__augmented=self) 