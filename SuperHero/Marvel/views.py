from django.shortcuts import render
from .models import Superhero
# Create your views here.
def superhero(request):
    heros = Superhero.objects.all()
    return render(request, 'allhero.html', {'heros':heros})