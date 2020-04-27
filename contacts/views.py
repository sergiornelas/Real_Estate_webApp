from django.shortcuts import render, redirect
from django.contrib import messages
#from django.core.mail import send_mail

#from django.conf import settings

from .models import Contact

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['id_listado']
        listing = request.POST['listado']
        
        name = request.POST['nombre']
        email = request.POST['correo']
        phone = request.POST['fono']
        message = request.POST['mensaje']

        #este es solamente cuando se esta haciendo el contact con login.
        user_id = request.POST['id_usuario']
        realtor_email = request.POST['correo_realtor']

        #Check if user has made inquiry already
        # if request.user.is_authenticated:
        #     user_id = request.user.id
        #     has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
        #     if has_contacted:
        #         messages.error(request, 'You have already made an inquiry for this listing')
        #         return redirect('/listings/'+listing_id)

        contactVar = Contact(listing=listing, listing_id=listing_id, name=name, email=email,
        phone=phone, message=message, user_id=user_id )

        contactVar.save()

        #Send email
        #send_mail(
        #    'Property Listing Inquiry',
        #    'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
        #    'sergio.ibm.ornelas@gmail.com',
        #    [realtor_email, 'techguyinfo@gmail.com'],
        #    fail_silently=False
        #)
        # el otro archivo que se tiene que descomentar para el email es settings.py
        messages.success(request, "Your request has been submitted, a realtor will get back to you soon")
        
        return redirect('/listingsXX/'+listing_id)