from django.urls import path
from . import views 
urlpatterns = [
    # map the URL (empty string) to the view
    path(r'', views.ResultsListView.as_view(), name='home'),
]