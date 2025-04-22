from django.contrib import admin
from django.urls import path,include   
from .import views

urlpatterns = [
    
    
    # ----------------------------public functions-----------------------------------
    
    
    path('',views.home),
    path('login',views.logins),
    
        
    path('adminhome',views.adminhome),
    path('userhome',views.userhome),
    path('slot_reg',views.slot_reg),
    
    path('admin_view_complaint',views.admin_view_complaint,name='admin_view_complaint'),

    path('slot_status',views.slot_status,name='slot_status'),
    path('admin_view_user',views.admin_view_user,name='admin_view_user'),
    path('admin_view_booking',views.admin_view_booking,name='admin_view_booking'),
    path('admin_view_payments',views.admin_view_payment,name='admin_view_payment'),
    path('manage_parking_location',views.manage_parking_location,name='manage_parking_location'),
    
    
    
    
    
    path('user_reg',views.user_reg,name='user_reg'),
    path('view_profile',views.view_profile),
    path('view_near',views.view_near),
    path('user_view_complaints',views.user_view_complaint),
    path('slots/<id>',views.slots),
    path('book/<id>/<am>',views.user_booking),
    path('user_view_booking',views.user_view_booking),
    
    
    path('scanner/<id>',views.scanner),
    path('occupied',views.occupied),
    path('pay/<id>/<ids>',views.pay),
    path('send_reply/<id>',views.send_reply),
    
    
    path('view_near',views.view_near),
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
   
    
    
    
    
    
    
   
    
    


    
]
