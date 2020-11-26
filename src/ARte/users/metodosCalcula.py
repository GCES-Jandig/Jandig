
from users import calculaartwork
from users.models import Artwork
from core.models import Exhibit

 def exhibits_count(Artwork: artwork):
        return Exhibit.objects.filter(artworks__in=[artwork]).count()
    
def exhibits_list(Artwork: artwork):
        return list(Exhibit.objects.filter(artworks__in=[artwork]))




from users import calculaartwork

 calculaartwork.exhibits_count(artwork)
 calculaartwork.exhibits_list(artwork)