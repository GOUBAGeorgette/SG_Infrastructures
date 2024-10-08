from django.shortcuts import render
from .forms import SignalementPanneForm  # Assure-toi que le formulaire est importé

def signaler_panne(request):
    if request.method == 'POST':
        form = SignalementPanneForm(request.POST)
        if form.is_valid():
            # Logique pour traiter le signalement (enregistrer dans la base de données, etc.)
            form.save()
            return render(request, 'SG_infrastructure/confirmation.html')  # Page de confirmation ou redirection
    else:
        form = SignalementPanneForm()

    return render(request, 'SG_infrastructure/signaler_panne.html', {'form': form})
