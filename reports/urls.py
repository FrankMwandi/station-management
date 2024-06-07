from django.urls import path
from .views import ClaimCreateView, ClaimDetailView, ProgressAddView, ClaimStatsView, search_claims, claim_stats_pdf, AccuserCreateView, AccusedCreateView

urlpatterns = [
    path('create/', ClaimCreateView.as_view(), name='create_claim'),
    path('<int:claim_id>/', ClaimDetailView.as_view(), name='claim_detail'),
    path('<int:claim_id>/add_progress/', ProgressAddView.as_view(), name='add_progress'),
    path('stats/', ClaimStatsView.as_view(), name='claim_stats'),
    path('search/', search_claims, name='search_claims'),
    path('stats/pdf/', claim_stats_pdf, name='claim_stats_pdf'),
    path('add_accuser/', AccuserCreateView.as_view(), name='add_accuser'),
    path('add_accused/', AccusedCreateView.as_view(), name='add_accused'),
]
