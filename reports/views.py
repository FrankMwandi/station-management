from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views import View
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Claim, Progress, Station, Accuser, Accused
from .forms import ClaimForm, ProgressForm, AccuserForm, AccusedForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.views.generic import CreateView, FormView

class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class LoginView(FormView):
    template_name = 'registration/login.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        login(self.request, form.get_user())
        return redirect('/dashboard/')

def logout_view(request):
    logout(request)
    return redirect('/login/')

@login_required
def dashboard(request):
    return render(request, 'reports/dashboard.html')

class ClaimCreateView(View):
    @method_decorator(login_required)
    def get(self, request):
        form = ClaimForm()
        return render(request, 'reports/claim_form.html', {'form': form})

    @method_decorator(login_required)
    def post(self, request):
        form = ClaimForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'Claim created successfully!'})
        return JsonResponse({'status': 'Error', 'errors': form.errors})

class ClaimDetailView(View):
    @method_decorator(login_required)
    def get(self, request, claim_id):
        claim = get_object_or_404(Claim, id=claim_id)
        progress = claim.progress_set.all()
        return render(request, 'reports/claim_detail.html', {'claim': claim, 'progress': progress})

@method_decorator(login_required, name='dispatch')
class ProgressAddView(View):
    def post(self, request, claim_id):
        claim = get_object_or_404(Claim, id=claim_id)
        form = ProgressForm(request.POST)
        if form.is_valid():
            progress = form.save(commit=False)
            progress.claim = claim
            progress.added_by = request.user
            progress.save()
            return JsonResponse({'status': 'Progress added successfully!'})
        return JsonResponse({'status': 'Error', 'errors': form.errors})

class ClaimStatsView(View):
    @method_decorator(login_required)
    def get(self, request):
        reports_today = Claim.objects.filter(date_reported__date=timezone.now().date()).count()
        reports_week = Claim.objects.filter(date_reported__gte=timezone.now() - timezone.timedelta(days=7)).count()
        reports_month = Claim.objects.filter(date_reported__gte=timezone.now() - timezone.timedelta(days=30)).count()
        return JsonResponse({
            'reports_today': reports_today,
            'reports_week': reports_week,
            'reports_month': reports_month
        })

class AccuserCreateView(View):
    @method_decorator(login_required)
    def get(self, request):
        form = AccuserForm()
        return render(request, 'reports/accuser_form.html', {'form': form})

    @method_decorator(login_required)
    def post(self, request):
        form = AccuserForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'Accuser created successfully!'})
        return JsonResponse({'status': 'Error', 'errors': form.errors})

class AccusedCreateView(View):
    @method_decorator(login_required)
    def get(self, request):
        form = AccusedForm()
        return render(request, 'reports/accused_form.html', {'form': form})

    @method_decorator(login_required)
    def post(self, request):
        form = AccusedForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'Accused created successfully!'})
        return JsonResponse({'status': 'Error', 'errors': form.errors})
