from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from apps.posts.models import Like, DisLike


class LikeMixin:

    @action(methods=['post'], detail=True)
    def add_like(self, request, *args, **kwargs):
        user = request.user
        post = self.get_object()
        like = Like.objects.filter(user=user, post=post)

        if like.exists():
            like.first().delete()
            post.like_rating -= 1
            post.save()
            return Response({'message': 'like is delete'},
                            status=status.HTTP_200_OK)

        dislike = DisLike.objects.filter(user=user, post=post)
        if dislike.exists():
            dislike.first().delete()
            post.dislike_rating -= 1

        Like.objects.create(user=user, post=post)
        post.like_rating += 1
        post.save()

        return Response({'message': 'like is added'},
                        status=status.HTTP_200_OK)


class DislikeMixin:

    @action(methods=['post'], detail=True)
    def add_dislike(self, request, *args, **kwargs):
        user = request.user
        post = self.get_object()
        dislike = DisLike.objects.filter(user=user, post=post)

        if dislike.exists():
            dislike.first().delete()
            post.dislike_rating -= 1
            post.save()
            return Response({'message': 'dislike is delete'},
                            status=status.HTTP_200_OK)

        like = Like.objects.filter(user=user, post=post)
        if like.exists():
            like.first().delete()
            post.like_rating -= 1

        DisLike.objects.create(user=user, post=post)
        post.dislike_rating += 1
        post.save()

        return Response({'message': 'dislike is added'},
                        status=status.HTTP_200_OK)
# proxy abstract 
