from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing
from listings.forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect
from listings.forms import BandForm
from listings.forms import ListForm

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
    return render(request, "listings/contact.html", {'form' : form})

def email_sent(request):

    return render(request, 'listings/email_sent.html')

def band_create(request):

    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)

    else:
        form = BandForm()

    return render(request,
            'listings/band_create.html',
            {'form': form})


def listing_create(request):

    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            listing = form.save()
            return redirect('listing-detail', listing.id)
    else:
        form = ListForm()

        return render(request, 'listings/listing_create.html', {'form': form})

def band_change(request, id):
    
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)

    return render(request, 'listings/band_change.html', {'form': form})

def listing_change(request, id):

    listing = Listing.objects.get(id=id)
    if request.method == 'POST':
        form = ListForm(request.POST, instance=listing)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données                                                                                                                                                                            
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour                                                                                                                                                         
            return redirect('listing-detail', listing.id)
    else:
        form = ListForm(instance=listing)

    return render(request, 'listings/listing_change.html', {'form': form})

def band_delete(request, id):

    band = Band.objects.get(id=id)
    if request.method == "POST":
        band.delete()
        return redirect('band-list')
    return render(request, 'listings/band_delete.html', {'band' : band})
