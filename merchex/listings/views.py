from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing
from listings.forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect
def band_list(request):
    bands = Band.objects.all()
    return render(request, "listings/band_list.html", context = {"bands": bands})

def band_detail(request, id):

    band = Band.objects.get(id = id)
    return render(request, "listings/band_detail.html", {'band': band})

def about(request):
    return render(request, "listings/about.html")

def listings(request):
    listings = Listing.objects.all()
    return render(request, "listings/listings.html", context = {"listings": listings})

def listing_detail(request, id):
    listing = Listing.objects.get(id = id)
    return render(request, "listings/listing_detail.html", {'listing' : listing})

def contact_us(request):
    
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
        )
        return redirect('email-sent')
    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).
    else:
        form = ContactUsForm()
    return render(
        request,
        "listings/contact.html",
        {'form' : form}
    )

def email_sent(request):
    return render(request, 'listings/email_sent.html')
