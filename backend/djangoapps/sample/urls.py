from django.urls import path
from django.conf.urls import url

from backend.djangoapps.sample import views as SampleViews


urlpatterns = [
    # json 반환의 기본
    path('default', SampleViews.sample_default, name='sample_default'),

    # raw query 기반 로직
    path('raw_query', SampleViews.sample_raw_query, name='sample_raw_query'),

    # orm 기반 로직
    path('orm', SampleViews.sample_orm, name='sample_orm'),
]