from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from magazine import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'magazine_site.views.home', name='home'),
    # url(r'^magazine_site/', include('magazine_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
     url(r'^admin/', include(admin.site.urls)),
     url(r'^comments/', include('django.contrib.comments.urls')),
     url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
     url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    )

urlpatterns+=patterns('',
        url(r'^$',views.newjournal),
        url(r'^journal/new/',views.newjournal),
        url(r'^journals/$',views.historyJournal),
        url(r'^content/$',views.content),
        url(r'^journal/([0-9]+)/$',views.journalitem),
        url(r'^articles/([0-9]+)/$',views.aritcles),
        url(r'^article/([0-9]+)/$',views.aritcle),
        url(r'^article/([0-9]+)/showcomment/$',views.article_show_comment),
    )
