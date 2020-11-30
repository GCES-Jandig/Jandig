# parte retirada

# user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
 
 #retirada de artwork

@property 
def exhibits_count(self):
   from calcula import calcartwork  
   calc1=calcartwork.__init__()
   return calc1.exhibits_count()   
        

@property 
def exhibits_list(self):
   from calcula import calcartwork
   calc1=calcartwork.__init__(self)
   return calc1.exhibits_list()    

  

    @property
    def exhibits_count(self):
        from core.models import Exhibit
        return Exhibit.objects.filter(artworks__in=[self]).count()

     
     
     # method was  take out from artwrok in order to  verify is work properly. 
     @property
    def in_use(self):
        if self.exhibits_count > 0:
            return True

        return False     