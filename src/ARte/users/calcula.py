
from django.db import models

class calcartwork(models.Model,object):

   def __init__(self,work):   
      self.work=work

   def exhibits_count(self,field):
        from core.models import Exhibit 
        return Exhibit.objects.filter(artworks__in=[self.work]).count()
    
   def exhibits_list(self,field):
        from core.models import Exhibit
        return list(Exhibit.objects.filter(artworks__in=[self.work]))







