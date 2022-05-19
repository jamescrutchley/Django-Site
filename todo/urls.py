from django.urls import path
import testapp
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('',testapp.views.test_view),
    path('todo/',testapp.views.to_do_view,name='todo'),
]

