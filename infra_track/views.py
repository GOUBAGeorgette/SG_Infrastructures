from django.shortcuts import render
from .forms import SignalementPanneForm

from django.shortcuts import render

def home(request):
    return render(request, 'SG_infrastructure/home.html')  # Assure-toi que le fichier home.html existe

from django.http import HttpResponse

def test_view(request):
    return HttpResponse('Le serveur fonctionne bien')



def signaler_panne(request):
    if request.method == 'POST':
        form = SignalementPanneForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'SG_infrastructure/confirmation.html')  # Page de confirmation
    else:
        form = SignalementPanneForm()

    return render(request, 'SG_infrastructure/signaler_panne.html', {'form': form})
