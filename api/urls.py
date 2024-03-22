from django.urls import path, include

#documantions
from api.spectacular.urls import urlpatterns as doc_urls

#apps_url
from clients.urls import urlpatterns as user_urls
from medservices.urls import urlpatterns as serv_urls
from doctors.urls import  urlpatterns as doct_urls
from medbooks.urls import urlpatterns as medbook_ulrs

app_name = 'api'

urlpatterns = [
    path('auth/', include('djoser.urls.jwt'))
]


urlpatterns += doc_urls

#apps_url
urlpatterns += user_urls
urlpatterns += serv_urls
urlpatterns += doct_urls
urlpatterns += medbook_ulrs
