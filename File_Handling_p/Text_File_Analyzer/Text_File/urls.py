from django.urls import path
from . import views

urlpatterns = [
    path('',views.Text),
    path('create/',views.Create),
    path('create_request/',views.Create_requeest),
    path('create_request/',views.Create_requeest),
    path('write/',views.Write),
    path('write_request/',views.Write_request),
    path('all_operations/',views.All_Operations),
    path('update/',views.Update),
    path('read/',views.Read),
    path('read_update_data/',views.Read_Update_Data),
    path('delete/',views.Delete),
]