
from django.db import models
from core.models import Exhibit
from .models import Artwork

class calcartwork(models.Model,object):

   def __init__(self,id):   
      self.id=id            
         
   def exhibits_count(self):
        artwork=Artwork.objects.get(id=self.id)
        return Exhibit.objects.filter(artworks__in=[artwork]).count()
    
   def exhibits_list(self):
        artwork=Artwork.objects.get(id=self.id)
        return list(Exhibit.objects.filter(artworks__in=[artwork]))







