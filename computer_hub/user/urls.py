from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.LogInView.as_view(),name='userlogin'),
    #path('dashboard/',views.DashBoardView.as_view(),name='dashboard'),
    path('',views.DashBoardView.as_view(),name='dashboard'),
    path('userlist/',views.ListOfUserView.as_view(),name='userlist'),
    path('userlogout/',views.UserLogoutView.as_view(),name='userlogout'),
    path('userregistrationform/',views.UserRegistrationView.as_view(),name = 'userregistration'),
    
]
