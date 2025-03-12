from django.contrib import admin
from django.urls import path, include
# from iostreakApi import urls
from .views import ContactUsView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('/',include('iostreakApi.urls')),
     path('view/', ContactUsView.as_view(), name='contact_us'),

]