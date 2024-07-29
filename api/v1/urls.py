from django.urls import path

from apps.users import views
from apps.ads.views import ad_detail, ad_list

urlpatterns = [
    path('ads/', ad_list, name='ad-list'),
    path('ads/<int:ad_id>/', ad_detail, name='ad-detail'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('token/', views.token, name='token'),
    
]
