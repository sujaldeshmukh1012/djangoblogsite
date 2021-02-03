from django.urls import path
from post.views import index, NewPost, PostDetails, tags, like, favorite,PostDelet,Allusers


urlpatterns = [
   	path('', index, name='index'),
   	path('<uuid:post_id>/delet',PostDelet,name='postdelet'),
   	path('newpost/', NewPost, name='newpost'),
   	path('<uuid:post_id>', PostDetails, name='postdetails'),
   	path('<uuid:post_id>/like', like, name='postlike'),
   	path('<uuid:post_id>/favorite', favorite, name='postfavorite'),
   	path('tag/<slug:tag_slug>', tags, name='tags'),
   	path('allusers',Allusers,name='allusers'),
]