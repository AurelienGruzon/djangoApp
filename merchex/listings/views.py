from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band

def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
    <h1>hello Django!</h1>
    <p>Mes groupes:</p>
    <ul><li>{bands[0].name}</li>
    <li>{bands[1].name}</li>
    <li>{bands[2].name}</li></ul>""")

def about(request):
    return HttpResponse('<h1>A propos</h1><p>Nous adorons merch!</p>')

def listings(request):
    return HttpResponse('<h1>Liste:</h1><ul><li>Article1</li><li>Article 2</li>')

def contact_us(request):
    return HttpResponse('<h1>Bonjour</h1><p>Contact</p>')
