from django.urls import path
from . import views
from django.views.generic import RedirectView

# #####:8000/test
urlpatterns = [
    path('',views.test_view),
    path('todo/',views.to_do_view,name='todo'),
]
