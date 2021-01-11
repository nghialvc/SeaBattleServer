from django.urls import path
from . import views

urlpatterns = [
    path('port<int:ports>-player<int:player_id1>-player<int:player_id2>',views.index,name='index'),
    path('wait-<int:ports>',views.wait,name='wait'),
]
