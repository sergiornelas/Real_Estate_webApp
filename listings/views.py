from django.shortcuts import render

#pull data from listings model
from .models import Listing

def index(request):
    #pull data from listings model
    listings = Listing.objects.all()

    #pull data from listings model
    context = {
        'listings': listings
    }
                                                #pull data from listings model
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    return render(request, 'listings/listing.html')
 
def search(request):
    return render(request, 'listings/search.html')