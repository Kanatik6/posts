from django.contrib import admin

from apps.posts.models import Post, Like, DisLike

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(DisLike)
