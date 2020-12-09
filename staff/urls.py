from django.urls import path
from .views import *

appname = 'staff'
urlpatterns = [
    path('login/', loginView, name='login'),
    path('', loginView, name='login'),
    path('registration/', registerView, name='registration'),
    path('dashboard/', dashboardView, name='dashboard'),
    path('profile/', addUserProfile, name='profile'),
    path('addUnit/', addUnit, name='addUnit'),
    path('addSession/', addSession, name='addSession'),
    path('all/', allqs, name='all'),
    path('allReport/', allReport, name='allReport'),
    path('report/<int:id>', report, name='report'),
    path('allocateWithReport/', allocateWithReport, name='allocateWithReport'),
    path('logout/', loguotView, name='logout'),
]