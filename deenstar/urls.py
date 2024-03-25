
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from django.conf import settings

from django.views.static import serve
from main import views
from auth.views import user_login


urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls'), ),
    path('', views.index_view),
    path('hotels/', views.hotel_view,name='one_hotel'),
    path('book/', views.book_view,name='book'),
    path('allpackages/', views.packages_view_all, name="allpackages"),
    path('single-package/', views.single_package, name="single-package"),
    path('accounts/login/',user_login, name="login"),
    
    
    
    path('tour-save/', views.tour_save, name="toursave"),
  
    
   

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
