from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path('logout/', views.user_logout, name="logout"),
    
     path('travelor/', views.travelor_view, name="travelor"),
    path('reject/', views.reject_booking, name="reject"),
    path('accept/', views.accept_booking, name="accept"),
    path('package-create/', views.create_package, name="package-create"),
    path('activity-create/', views.create_activity, name="activity-create"),
    path('dest-create/', views.create_Destination, name="dest-create"),
    path('hotel-create/', views.create_Hotel, name="hotel-create"),
    path('booked/', views.booked_customers, name="booked"),
    path('rejected/', views.rejected_customers, name="rejected"),
    path('signup/', views.authView, name="signup"),
    path('', views.dashboard_view, name="home"),
     path('manage/', views.manage_view, name="manage"),
    path('single-accepted/', views.single_accepted, name="single-accepted"),
    path('single-rejected/', views.single_rejected, name="single-rejected"),
    path('activity-edit/', views.activity_edit, name="activity-edit"),
    path('package-manager/', views.managePackages, name="package-manager"),
    path('single-hotel/', views.SingleHotelView, name="single-hotel"),
    path('single-dest/', views.SingleDestView, name="single-dest"),
    path('edit-package/', views.edit_package, name="edit-package"),
    path('delete-package/', views.package_delete, name="delete-package"),
    
    
    
]