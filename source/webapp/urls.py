from django.urls import path
from webapp.views import HomeView

app_name = 'webapp'

urlpatterns = [
    path('', HomeView.as_view(), name='index')
]
