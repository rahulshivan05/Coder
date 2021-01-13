from django.urls import path, include

from .import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # path('movie/', views.movie, name='movie'),
    
    path('search', views.search, name='search'),
    # Login, signup and logout here 
    path('signup', views.handleSignup, name='handleSignup'),
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
    
    ######################## Ends here ##################

    path('profile', views.my_profile_view, name='profile'),
    path('activate/<uidb64>/<token>', views.VerificationView.as_view(), name='activate'),
    path('login_user', views.LoginView, name='login_user'),

    path('download', views.Download_Video, name='download'),
    path('down', views.DownYtd_Video, name='down'),
    path('download_complete/<res>', views.download_complete, name='download_complete'),
    path('geo', views.geolocator, name='geo'),
    path('geo_loc', views.geo_loc, name='geo_loc'),
    path('fuel', views.get_fuel_rate, name='fuel'),

    ############ Cookie Tutorial #############
    path('set', views.setcookie, name='set'),
    path('get', views.getcookie, name='get'),
    path('del', views.delcookie, name='del'),
]