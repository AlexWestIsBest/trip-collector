from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('trips/', views.trips_index, name='index'),
    path('trips/<int:trip_id>/', views.trips_detail, name='detail'),
    path('trips/create/', views.TripCreate.as_view(), name='trips_create'),
    path('trips/<int:pk>/update/', views.TripUpdate.as_view(), name='trips_update'),
    path('trips/<int:pk>/delete/', views.TripDelete.as_view(), name='trips_delete'),
    path('trips/<int:trip_id>/add_transport', views.add_transport, name='add_transport'),
    path('trips/<int:trip_id>/assoc_companion/<int:companion_id>/', views.assoc_companion, name='assoc_companion'),

    path('companions/', views.CompanionIndex.as_view(), name='companion_list'),
    path('companions/create/', views.CompanionCreate.as_view(), name='companion_create'),
    path('companions/<int:pk>/', views.CompanionDetail.as_view(), name='companion_detail'),
    path('companions/<int:pk>/update/', views.CompanionUpdate.as_view(), name='companion_update'),
    path('companions/<int:pk>/delete/', views.CompanionDelete.as_view(), name='companion_delete'),

    path('accounts/signup/', views.signup, name='signup'),
]