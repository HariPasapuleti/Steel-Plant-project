from django.urls import include, path
from . import views

urlpatterns = [
    # path('', include('authentication.urls')),
    path('list/', views.machine_list, name='machine_list'),
    path('add/', views.machine_add, name='machine_add'),
]


