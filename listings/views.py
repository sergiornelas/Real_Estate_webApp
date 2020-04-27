from django.shortcuts import get_object_or_404, render
    # es un paquete que hace si un objeto es inexistente (algún id falso), mande
    #    por default un error 404

#pull data from listings model
from .models import Listing

def index(request):
    #pull data from listings model
    listingsX = Listing.objects.all()

    #pull data from listings model
    context = {
        'listingsY': listingsX
    }
                                                #pull data from listings model
    return render(request, 'listings/listings.html', context)

#para mostra la información detallada de cada elemento
#AQUI SE MUESTRA COMO MOSTRAR LOS DATOS ESPECÍFICOS DE UN ID!!!
#VEASE URLS.PY PARA VER LA OTRA PARTE!
def listingT(request, lizzting_id):
    listingVar = get_object_or_404(Listing, pk=lizzting_id) 
        #pk=listing_id se refiere al mismo listing_id segundo parámetro de la función.

    context = {
        'listingAA': listingVar
    }
    return render(request, 'listings/listing.html', context)
 





 
def search(request):
    return render(request, 'listings/search.html')