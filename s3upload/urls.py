from django.conf.urls import url

from .views import get_upload_params

urlpatterns = [
    url('^get_upload_params/', get_upload_params, name='s3upload')
]
