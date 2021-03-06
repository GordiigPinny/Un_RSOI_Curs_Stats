from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.pagination import LimitOffsetPagination
from RequestStats.models import RequestsStats
from RequestStats.serializers import RequestsStatsSerializer
from StatsService.utils import RetrieveQueryParamsMixin


class RequestsStatsListView(ListCreateAPIView, RetrieveQueryParamsMixin):
    """
    Вьюха для спискового представления статы по реквестам
    """
    serializer_class = RequestsStatsSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return RequestsStats.objects.filter(**self.get_lookup_fields(['user_id']))


class RequestsStatsDetailView(RetrieveAPIView):
    """
    Вьюха для детального представления статы по реквесту
    """
    serializer_class = RequestsStatsSerializer

    def get_queryset(self):
        return RequestsStats.objects.all()
