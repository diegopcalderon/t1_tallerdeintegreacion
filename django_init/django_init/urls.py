"""django_init URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aplicaciones.consumir_api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('search', views.search, name='search'),
    path('seasons_bb/', views.seasons_bb, name='seasons_bb'),
    path('seasons_bcs/', views.seasons_bcs, name='seasons_bcs'),
    path('episodes_breaking_bad/<int:id>/', views.episodes_breaking_bad, name='episodes_breaking_bad'),
    path('episodes_better_call_saul/<int:id>/', views.episodes_better_call_soul, name='episodes_better_call_saul'),
    path('detalle_episode/<int:episode_id>/', views.episodes, name='episodes'),
    path('characters/<str:character>', views.characters, name='characters'),
]
