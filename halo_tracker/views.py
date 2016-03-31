from django.shortcuts import render
from halo_tracker.models import gameVariants

def home_page(request):

    gameStrongholds = gameVariants.objects.get(name="Strongholds")

    return render(request, 'index.html', {'strongholds': gameStrongholds.contentId})

