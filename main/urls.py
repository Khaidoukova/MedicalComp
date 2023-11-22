from django.urls import path
from main.apps import MainConfig
from main.views import LabTestListView, LabTestDetailView, LabTestCreateView, LabTestUpdateView, IndexView, \
    DoctorListView, DoctorDetailView, DoctorCreateView, DoctorUpdateView

app_name = MainConfig.name

urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('labtest_list', LabTestListView.as_view(), name='labtest_list'),
    path('labtest/<int:pk>', LabTestDetailView.as_view(), name='labtest_detail'),
    path('labtest_create/', LabTestCreateView.as_view(), name='labtest_create'),
    path('labtest_update/<int:pk>', LabTestUpdateView.as_view(), name='labtest_update'),
    path('doctor_list', DoctorListView.as_view(), name='doctor_list'),
    path('doctor/<int:pk>', DoctorDetailView.as_view(), name='doctor_detail'),
    path('doctor_create/', DoctorCreateView.as_view(), name='doctor_create'),
    path('doctor_update/<int:pk>', DoctorUpdateView.as_view(), name='doctor_update'),

]