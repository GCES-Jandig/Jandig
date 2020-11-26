


class calculaartwork():
    pass
    
from .models import Artwork
from core.models import Exhibit

def exhibits_count(Artwork: artwork):
        return Exhibit.objects.filter(artworks__in=[artwork]).count()
    
def exhibits_list(Artwork: artwork):
        return list(Exhibit.objects.filter(artworks__in=[artwork]))





calculaartwork.exhibits_count(artwork)
calculaartwork.exhibits_list(artwork)
