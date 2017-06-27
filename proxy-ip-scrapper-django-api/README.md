# Django-API 
>	Create REST API for proxy IP addresses.

>	Here, "home" is one app directory, in which home.models consist database tabel "IPdata".

>	"home.urls" file consist all type of url inputs and according to urlpattern particuler view is returned.

>	In "home.views" file all views are included according to view type, different class are created.

>	In "home.serializer" file include all different serializer.

#Links are:

#For List Of ALL IPdata Objects

1 ) LocalHost:8000/
-->Returns List of all IP

2 ) LocalHost:8000/x.x.x.x/
-->Returns Details of Specific IP

3 ) LocalHost:8000/var_country/
-->Returns All IP where country = var_country

#Retrieve IPdata Objects By queries

4A ) LocalHost:8000?ip_address = x.x.x.x
-->Returns object where ip_address = x.x.x.x

4B ) LocalHost:8000?country = x
-->Returns All IPdata Objects where country = x

4C ) LocalHost:8000?port_no = x
-->Returns All IPdata Objects where Port NO = x

4D ) LocalHost:8000?anonymity = x
-->Returns All IPdata Objects where Anonymity = x

4E ) LocalHost:8000?HTTPS = x
-->Returns All IPdata Objects where HTTPS = x

#Admin Page

5 ) LocalHost:8000/admin/
-->Admin Page

6 ) LocalHost:8000/create/
-->To Create a New Object

7 ) LocalHost:8000/x.x.x.x/edit/
-->To Edit Object which have IP Address = x.x.x.x

8 ) LocalHost:8000/x.x.x.x/delete/
-->To Delete Object which have IP Address = x.x.x.x

NOTE : Admin Links(Edit, Delete, Create) can only access by Admin User. 	
     : Here, IP address is primary key field.
