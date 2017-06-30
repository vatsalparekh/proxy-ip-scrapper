from rest_framework.serializers import ModelSerializer
from .models import IPdata

class IPCreateUpdateSerializer(ModelSerializer):

    class Meta:
        model = IPdata
        fields = ('ip_address','port_no','country','anonymity','HTTPS')

        
class IPDetailSerializer(ModelSerializer):

    class Meta:
        model = IPdata
        fields = ('ip_address','port_no','country','anonymity','HTTPS','last_updated')


class IPListSerializer(ModelSerializer):

    class Meta:
        model = IPdata
        fields = ('ip_address','port_no','country')

