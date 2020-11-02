from django.urls import path
from django.conf.urls import url, include


urlpatterns = [
    path('sample/', include('backend.djangoapps.sample.urls')),
    path('admin/', include('backend.djangoapps.admin.urls')),
    path('user/', include('backend.djangoapps.user.urls')),
]
