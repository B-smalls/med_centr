from django.urls import path

from doctors.views import doctor, doctShedule, doctRecord, specialization


urlpatterns = [
    path('doctors/doct/specializations/', specialization.SpacializationsAllView.as_view(), name='specializations'),
    path('doctors/doct/all-doctors/', doctor.DoctorsAllView.as_view(), name='all-doctors'),
    path('doctors/doct/search-doctors/<int:special_id>/', doctor.SearchDoctorsView.as_view(), name='search-doctors'),

    path('doctors/doctShedule/', doctShedule.DoctSheduleAllView.as_view(), name='doctShedule'),
    path('doctors/doctShedule/shedulebydoctor/<int:doctor_id>/', doctShedule.DoctSheduleByDoctView.as_view(), name='shedulebydoctor'),
    path('doctors/doctShedule/shedulebyspecializations//<int:special_id>/', doctShedule.DoctSheduleBySpecView.as_view(), name='shedulebyspecializations'),




    # path('medserv/serv/serv-list/', service.ServiceAllView.as_view(), name='serv-list'),
    # path('medserv/serv/servshed-list/', servShedule.ServSheduleView.as_view(), name='servshed-list'),
    # path('medserv/serv/search-servshed/<int:serv_id>/', servShedule.SearchSheduleView.as_view(), name='search-servshed'),
    # path('medserv/serv/create-serv-record/', servRecord.ServRecordCreateView.as_view(), name='create-serv-record'),
    # path('medserv/serv/delete-serv-record/<int:pk>/', servRecord.ServRecordDeleteView.as_view(), name='delete-serv-record'),
    # path('medserv/serv/user-serv-record/', servRecord.ServRecordListView.as_view(), name='user-serv-record'),user-serv-record

   # path('clients/change-passwd/', clients.ChangePasswordView.as_view(), name='change_passwd'),
]
