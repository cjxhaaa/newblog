from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Blog information',{'fields':['title','content']}),
        ('Date information',{'fields':['pub_time']})
    ]
    list_display = ('title','pub_time')
    list_filter = ['pub_time']
    search_fields = ['title']
admin.site.register(Article,ArticleAdmin)

