from .models import TRANSACTION
from rest_framework import routers, serializers, viewsets, generics, filters
from .serializers import TRANSACTIONSerializer
import django_filters


class TRANSACTIONViewSet(viewsets.ModelViewSet):
    """
    Viewset made for our user.
    """

    serializer_class = TRANSACTIONSerializer
    queryset = TRANSACTION.objects.all()
    lookup_field = "id"
    http_method_names = ["get", "post", "patch", "delete"]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = "__all__"
