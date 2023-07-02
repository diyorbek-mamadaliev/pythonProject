from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views,HOD_views
from .views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),
    # Login Path
    path('', views.LOGIN, name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='logout'),
    path('register/', register, name='register'),
    # Main
    path('Hod/Home', HOD_views.HOME, name='home'),
    path('Hod/Chem', HOD_views.CHEM, name='chem'),
    path('hod-chat/', HOD_views.hod_chat, name='hod_chat'),
    path('chem-chat/', HOD_views.chem_chat, name='chem_chat'),
    # Profile
    path('profile', views.PROFILE, name='profile'),
    path('Profile/update', views.PROFILE_UPDATE, name='profile_update'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
