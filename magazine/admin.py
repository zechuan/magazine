from django.contrib import admin  
from magazine.models import Article,Journal,catalog,Author

class AuthorAdmin(admin.ModelAdmin):
    list_display=('name','email','website')

class JournalAdmin(admin.ModelAdmin):
    list_display=('volumn','introduce')
    
class ArticleAdmin(admin.ModelAdmin):
    list_display=('title','author','journal_nom','publish_time','status')
    list_filter=('publish_time',)
    ordering=('-publish_time',)
    raw_id_fields=('author',)
class CatalogAdmin(admin.ModelAdmin):
    list_display=('journal_nom','article','indexinjournal')
    ordering=('-id',)
    list_filter=('journal_nom',)
        
    
admin.site.register(Article,ArticleAdmin)
admin.site.register(Journal,JournalAdmin)
admin.site.register(catalog,CatalogAdmin)
admin.site.register(Author,AuthorAdmin)