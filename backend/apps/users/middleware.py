from rest_framework.request import Request as RestFrameworkRequest
from rest_framework.views import APIView

from django.utils.timezone import now
from django.contrib.auth import get_user_model

User = get_user_model()


def SetLastActiveMiddleware(get_response):
    def middleware(request):

        response = get_response(request)
        drf_request: RestFrameworkRequest = APIView().initialize_request(request)
        drf_request = APIView().initialize_request(request)
        user = drf_request.user
        if not user.is_anonymous:
            User.objects.filter(id=user.id) \
                .update(last_login=now())

        return response
    return middleware
