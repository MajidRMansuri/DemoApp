from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('page',page,name='page'),
    path('otp_page',otp_page,name='otp_page'),
    path('registration',registration,name='registration'),
    path('create_otp',create_otp,name='create_otp'),
    # path('profile',profile,name='profile'),
    path('verify_otp',verify_otp,name='verify_otp'),
    path('login',login,name='login'),
    path('user_login',user_login,name='user_login'),
    path('profile_page',profile_page,name='profile_page'),
    path('error_page',error_page,name='error_page'),
    path('home_page',home_page,name='home_page'),
    path('shop_type_view',shop_type_view,name='shop_type_view'),
    path('profile_data',profile_data,name='profile_data'),
    path('profile_view',profile_view,name='profile_view'), 
    path('del_type_view',del_type_view,name='del_type_view'), 
    path('profile_remove/<int:pk>',profile_remove,name='profile_remove'),
    path('profileImage_remove',profileImage_remove,name='profileImage_remove'),
    path('update_basic_details_customer',update_basic_details_customer,name='update_basic_details_customer'), 
    path('profile_image_upload',profile_image_upload,name='profile_image_upload'),
    path('update_basic_details_merchant',update_basic_details_merchant,name='update_basic_details_merchant'),
    path('logout',logout,name='logout'),
    # path('update_contact_details_merchant',update_contact_details_merchant,name='update_contact_details_merchant'),
    # path('profile_basic_data',profile_basic_data,name='profile_basic_data'),
    # path('del_status',del_status,name='del_status'),
]