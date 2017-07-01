from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView
)

# authentication permissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)

from home.models import IPdata

from home.serializers import (
    IPDetailSerializer,
    IPListSerializer,
    IPCreateUpdateSerializer,
)


# home/country_name
class IPCountryListAPIView(ListAPIView):
    serializer_class = IPListSerializer

    # permission_class = [AllowAny]
    def get_queryset(self):
        country_name = self.kwargs['country']
        return IPdata.objects.filter(country__iexact=country_name).order_by('-last_updated')


# home/create
class IPCreateAPIView(CreateAPIView):
    queryset = IPdata.objects.all().order_by('-last_updated')
    serializer_class = IPCreateUpdateSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]


# home/specific_object's_ip_address
class IPDetailList(RetrieveAPIView):
    queryset = IPdata.objects.all().order_by('-last_updated')
    serializer_class = IPDetailSerializer


# home/specific_object/delete
class IPDeleteAPIView(DestroyAPIView):
    queryset = IPdata.objects.all().order_by('-last_updated')
    serializer_class = IPDetailSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


# home/?ip_address=any_ip_address
# home/?country=country_name
# home/?port_no=any_port_no
# home/?anonymity=any_var
# home/?HTTPS=any_var
# home/

class IPListAPIView(ListAPIView):
    serializer_class = IPListSerializer

    # permission_class = [AllowAny]
    def get_queryset(self):

        query = []
        queryset = IPdata.objects.all()
        query = [
            self.request.query_params.get("ip_address", None),
            self.request.query_params.get("country", None),
            self.request.query_params.get("port_no", None),
            self.request.query_params.get("anonymity", None),
            self.request.query_params.get("HTTPS", None)
        ]

        if query[0] is not None:
            queryset = queryset.filter(ip_address=query[0])  # for case insensitive search
        elif query[1] is not None:
            queryset = queryset.filter(country__iexact=query[1])
        elif query[2] is not None:
            queryset = queryset.filter(port_no=query[2])
        elif query[3] is not None:
            queryset = queryset.filter(anonymity__iexact=query[3])
        elif query[4] is not None:
            queryset = queryset.filter(HTTPS__iexact=query[4])
        return queryset.order_by('-last_updated')


# home/specific_object/edit
class IPUpdateAPIView(RetrieveUpdateAPIView):
    queryset = IPdata.objects.all().order_by('-last_updated')
    serializer_class = IPCreateUpdateSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]