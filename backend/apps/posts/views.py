from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import get_user_model
from django_filters import rest_framework as django_filters

from apps.posts.mixins import LikeMixin, DislikeMixin
from apps.posts.models import Post, Like, DisLike
from apps.posts.serializer import PostSerializer, LikeSerializer, DisLikeSerializer
from apps.posts.filters import DateDisLikeFilter, DateLikeFilter

User = get_user_model()


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    filter_backends = [django_filters.DjangoFilterBackend, ]
    filterset_class = DateLikeFilter

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny(), ]
        return [IsAuthenticated(), ]

    @action(methods=['get'], detail=False,)
    def get_range(self, request, *args, **kwargs):
        date_from = request.query_params.get('date_from')
        date_to = request.query_params.get('date_to')
        
        dislike_qs = self.get_queryset().filter(time__gte=date_from, time__lte=date_to)
        serializer = self.get_serializer(dislike_qs, many=True)

        return Response({'Message': f'Likes from {date_from} to {date_to}:  \
                         {dislike_qs.count()}',
                         'Likes': serializer.data},
                        status=status.HTTP_200_OK)


class DisLikeViewSet(ModelViewSet):
    queryset = DisLike.objects.all()
    serializer_class = DisLikeSerializer
    filter_backends = [django_filters.DjangoFilterBackend, ]
    filterset_class = DateDisLikeFilter

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny(), ]
        return [IsAuthenticated(), ]

    @action(methods=['get'], detail=False,)
    def get_range(self, request, *args, **kwargs):
        date_from = request.query_params.get('date_from')
        date_to = request.query_params.get('date_to')

        dislike_qs = self.get_queryset().filter(time__gte=date_from, time__lte=date_to)
        # поскольку мы не получаем данные из реквеста, то и смысла в is_valid нет
        serializer = self.get_serializer(dislike_qs, many=True)

        return Response({'Message': f'Dislikes from {date_from} to {date_to}: {dislike_qs.count()}',
                         'dislikes': serializer.data},
                        status=status.HTTP_200_OK)


class PostViewSet(LikeMixin, DislikeMixin, ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny(), ]
        return [IsAuthenticated(), ]


# class DaysSinceAdvertFilter(admin.SimpleListFilter):
#     # Human-readable title which will be displayed in the
#     # right admin sidebar just above the filter options.
#     title = _('Days Since Advert')

#     # Parameter for the filter that will be used in the URL query.
#     parameter_name = 'last_advert'

#     def lookups(self, request, model_admin):
#         """
#         Returns a list of tuples. The first element in each
#         tuple is the coded value for the option that will
#         appear in the URL query. The second element is the
#         human-readable name for the option that will appear
#         in the right sidebar.
#         """
#         return (
#             ('0', _('Less than 7 days')),
#             ('7', _('7-13 days')),
#             ('14', _('14-20 days')),
#             ('21', _('21-27 days')),
#             ('28', _('28-34 days')),
#             ('35', _('35+ days')),
#         )

#     def queryset(self, request, queryset):
#         """
#         Returns the filtered queryset based on the value
#         provided in the query string and retrievable via
#         `self.value()`.
#         """
#         # Compare the requested value to decide how to filter the queryset.
#         today = datetime.date.today()
#         if self.value() == '0':
#             return queryset.filter(last_advert__gte=today - datetime.timedelta(days=6))
#         if self.value() == '7':
#             return queryset.filter(last_advert__gte=today - datetime.timedelta(days=13),
#                                    last_advert__lte=today - datetime.timedelta(days=7))
#         if self.value() == '14':
#             return queryset.filter(last_advert__gte=today - datetime.timedelta(days=20),
#                                    last_advert__lte=today - datetime.timedelta(days=14))
#         if self.value() == '21':
#             return queryset.filter(last_advert__gte=today - datetime.timedelta(days=27),
#                                    last_advert__lte=today - datetime.timedelta(days=21))
#         if self.value() == '28':
#             return queryset.filter(last_advert__gte=today - datetime.timedelta(days=34),
#                                    last_advert__lte=today - datetime.timedelta(days=28))
#         if self.value() == '35':
#             return queryset.filter(last_advert__lte=today - datetime.timedelta(days=35))
