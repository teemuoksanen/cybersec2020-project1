from django.urls import path

from .views import homePageView, transferView, claimView

urlpatterns = [
	path('', homePageView, name='home'),
	path('transfer/', transferView, name='transfer'),
	path('claim/', claimView, name='claim'),
]