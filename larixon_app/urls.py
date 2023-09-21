from django.urls import path
from larixon_app import views

urlpatterns = [
    path('advert-list/', views.advert_list_view),
    path('advert/<int:pk>', views.advert_view),
]

