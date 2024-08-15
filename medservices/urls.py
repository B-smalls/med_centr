from django.urls import path

from medservices.views import service, servShedule, servRecord


urlpatterns = [
    path('medserv/serv/serv-list/', service.ServiceAllView.as_view(), name='serv-list'),
    path('medserv/serv/servshed-list/', servShedule.ServSheduleView.as_view(), name='servshed-list'),
    path('medserv/serv/search-servshed/<int:serv_id>/', servShedule.SearchSheduleView.as_view(), name='search-servshed'),
    path('medserv/serv/create-serv-record/', servRecord.ServRecordCreateView.as_view(), name='create-serv-record'),
    path('medserv/serv/delete-serv-record/<int:pk>/', servRecord.ServRecordDeleteView.as_view(), name='delete-serv-record'),
    path('medserv/serv/user-serv-record/', servRecord.ServRecordListView.as_view(), name='user-serv-record'),

   # path('clients/change-passwd/', clients.ChangePasswordView.as_view(), name='change_passwd'),
]
