from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Claim, Progress, Station, Accuser, Accused
from .forms import ClaimForm, ProgressForm

@login_required
def home(request):
    claims = Claim.objects.all()
    return render(request, 'reports/home.html', {'claims': claims})

@login_required
def add_claim(request):
    if request.method == 'POST':
        form = ClaimForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClaimForm()
    return render(request, 'reports/add_claim.html', {'form': form})

@login_required
def update_progress(request, claim_id):
    claim = get_object_or_404(Claim, id=claim_id)
    if request.method == 'POST':
        form = ProgressForm(request.POST)
        if form.is_valid():
            progress = form.save(commit=False)
            progress.claim = claim
            progress.added_by = request.user
            progress.save()
            return redirect('home')
    else:
        form = ProgressForm()
    return render(request, 'reports/update_progress.html', {'form': form, 'claim': claim})