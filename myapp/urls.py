from . import views
from django.urls import path
#import matplotlib
#from matplotlib.pyplot import text


from django.conf.urls.static import static
from django.conf import settings

app_name = "myapp"

urlpatterns = [
    path('', views.index, name='index'),
    path('query',views.get_query_data,name='query'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_URL)
