from django.urls import path
from django.conf.urls import url, include

from backend import views as devViews


urlpatterns = [
    path('api/v1/', include('backend.urls')),
    path('', devViews.index, name='index'), 
]
