from rest_framework import routers

from apps.posts.views import LikeViewSet, PostViewSet, DisLikeViewSet


router = routers.SimpleRouter()
router.register('likes', LikeViewSet, basename='like')
router.register('dislikes', DisLikeViewSet, basename='dislike')
router.register('', PostViewSet, basename='post')


urlpatterns = []
urlpatterns += router.urls

router.urls