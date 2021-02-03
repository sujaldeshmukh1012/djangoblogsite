from django.contrib import admin
from post.models import Post, Tag, Follow, Stream
# Register your models here.
admin.site.register(Tag)
admin.site.register(Follow)
admin.site.register(Stream)

class PostAdmin(admin.ModelAdmin):
	 list_display = ('title','id','posted','user','likes')
	 list_filter = ('likes','user')
	 search_fields = ('title', 'caption')
	 ordering = ('-likes',)

admin.site.register(Post,PostAdmin)