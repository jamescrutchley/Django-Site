from django.urls import path
from . import views

# #####:8000/test
urlpatterns = [
    path('',views.test_view),
    path('/todo',views.to_do_view)
]
