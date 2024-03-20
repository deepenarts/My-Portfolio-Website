from django.urls import path

from .views import contact, home  # Import the contact view

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),  # Define the URL pattern for the contact view
]
