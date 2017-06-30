from django.conf.urls import url
from .views import (
    IPListAPIView,
    IPDetailList,
    IPUpdateAPIView,
    IPDeleteAPIView,
    IPCreateAPIView,
    IPCountryListAPIView,

)

urlpatterns = [

    #home/
    #home/query_for_any_field_of_database
    url(r'^$', IPListAPIView.as_view(), name="List Of All IP and Can be filter By Query in URL format"),
    
    #home/ip_address
    url(r'^(?P<pk>(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]'
        r'|25[0-5]))/$', IPDetailList.as_view(), name="Search Object with IP"),
    
    #home/ip_address/edit
    url(r'^(?P<pk>(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]'
        r'|25[0-5])+)/edit/$', IPUpdateAPIView.as_view(), name="Edit Specific Object"),
    
    #home/ip_address/delete
    url(r'^(?P<pk>(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]'
        r'|25[0-5])+)/delete/$', IPDeleteAPIView.as_view(), name="Delete Specific Object"),
    
    #home/create
    url(r'^create/$', IPCreateAPIView.as_view(), name="create"),
    
    #home/country
    url(r'^(?P<country>.+)/$', IPCountryListAPIView.as_view(), name="List of IP available in Specific Country"),


]
