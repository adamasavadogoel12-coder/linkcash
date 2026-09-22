from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Link, Click
import random
import string

def generate_slug(length=6):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def home(request):
    return render(request, 'links/home.html')

@login_required
def dashboard(request):
    links = Link.objects.filter(user=request.user)
    return render(request, 'links/dashboard.html', {'links': links})

@login_required
def create_link(request):
    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        slug = generate_slug()
        Link.objects.create(user=request.user, original_url=original_url, slug=slug)
        return redirect('dashboard')
    return render(request, 'links/create_link.html')

def redirect_link(request, slug):
    link = get_object_or_404(Link, slug=slug)
    # Enregistrer le clic
    Click.objects.create(link=link)
    # Ici, plus tard, on ajoutera la page avec les pubs HilltopAds
    return redirect(link.original_url)