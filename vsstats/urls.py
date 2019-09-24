from django.urls import path

from . import views

app_name = 'vsstats'

urlpatterns = [
    path('', views.index, name='index'),
    path('sources', views.index, name='index'),
    path('sources/<int:source_id>', views.sources, name='sources'),
    path('api/stats/<int:source_id>', views.api_stats, name='api_stats')
]
