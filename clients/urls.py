from django.urls import path, include
from rest_framework.routers import DefaultRouter

from clients.views import clients

#router = DefaultRouter()


#router.register(r'search', clients.UserListSearchView, 'users-search')

urlpatterns = [
    path('clients/reg/', clients.RegistrationView.as_view(), name='reg'),
    path('clients/me/', clients.MeView.as_view(), name='me'),
    path('clients/change-passwd/', clients.ChangePasswordView.as_view(), name='change_passwd'),
]

#urlpatterns += path('users/', include(router.urls)),