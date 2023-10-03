from django.contrib import admin
from django.urls import path , include



urlpatterns = [
    path('App-Elevator/', include('AppElevator.urls')),
    path('admin/', admin.site.urls),
]

