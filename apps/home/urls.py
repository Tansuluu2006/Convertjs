from django.urls import path
from apps.home.views import index, about_page, contact_page

urlpatterns = [
    path('', index, name='home'),
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
]