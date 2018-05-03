from django.shortcuts import render

# Create your views here.
from .models import SpisokMenu, Sponsor, Sushitype

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_spisokmenus=SpisokMenu.objects.all().count()
  
    num_sponsors=Sponsor.objects.count()  # The 'all()' is implied by default.

    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_spisokmenus':num_spisokmenus,'num_sponsors':num_sponsors},
    )
from django.views import generic

class SpisokMenuListView(generic.ListView):
    model = SpisokMenu


class SpisokMenuDetailView(generic.DetailView):
    model = SpisokMenu

class SponsorListView(generic.ListView):
    model = Sponsor


class SponsorDetailView(generic.DetailView):
    model = Sponsor