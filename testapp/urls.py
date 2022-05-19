from django.urls import path
from . import views
from django.views.generic import RedirectView

# #####:8000/test
urlpatterns = [
    path('',views.test_view),
]
