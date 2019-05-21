import os

from django.conf.urls import url
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import index
from ezbusiness.settings import BASE_DIR


'''path('', IndexView.as_view(), name='index'),'''
app_name = 'webapp'
urlpatterns = [
    path('', index, name='index'),
] + static(settings.MEDIA_URL, document_root=os.path.join(BASE_DIR, 'webapp', 'media'))
