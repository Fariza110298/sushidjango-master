from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path(r'^spisokmenus/$', views.SpisokMenuListView.as_view(), name='spisokmenus'),
    path('spisokmenu/<int:pk>', views.SpisokMenuDetailView.as_view(), name='spisokmenu-detail'),
    path('sponsors/', views.SponsorListView.as_view(), name='sponsors'),
    path('sponsor/<int:pk>', views.SponsorDetailView.as_view(), name='sponsor-detail'),
]