from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('login/',views.login_page,name='login_page'),
    path('register/',views.register_page,name='register_page'),
    path('home/',views.home,name='home_page'),
    path('',views.landing_page,name='landing_page'),
    path('logout/',views.logout_page,name='logout_page'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)