from django.http.response import HttpResponse
from django.template import Context,Template
from django.shortcuts import render_to_response
from magazine.models import Article,Journal,catalog,Author
from django.http import HttpResponse
from django.http.response import Http404
from django.core.context_processors import request
from django.db import connection
from django.core.context_processors import csrf
from django.template import RequestContext

def homepage(request):
    return render_to_response('index.html',{})

def historyJournal(request):
    journals=Journal.objects.all().filter().order_by('-id')
    return render_to_response('journals.html',{'journals':journals})

def content(request):
    return render_to_response('catalogue.html',{})

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def journalitem(request,param1):        
    try:
        offset=int(param1)
    except:
        raise Http404
    journal=Journal.objects.get(id=offset)
    sqlstring="""
                select a.article_id,a.journal_nom_id,  b.id, b.title, b.author_id,a.indexinjournal,b.html_content,b.article_image
                from magazine_catalog as a left join magazine_article as b 
                on a.article_id=b.id 
                where a.journal_nom_id= "%s"
                order by a.indexinjournal"""%(offset)
    cursor = connection.cursor()
    cursor.execute(sqlstring)
    articles=dictfetchall(cursor)
    return render_to_response('catalogue.html',Context({'journal':journal,'articles':articles}))

def newjournal(request):
    sqlstring="""
                select *
                from magazine_journal
                order by id desc
                limit 0,1"""
    cursor = connection.cursor()
    cursor.execute(sqlstring)
    journalsql=dictfetchall(cursor)
    journal_nom=journalsql[0]['id']
#    return render_to_response('sdfsdf.html',Context({'journal_nom':journal_nom}))
    journal=Journal.objects.get(id=journal_nom)
    sqlstring="""
                select a.article_id,a.journal_nom_id,  b.id, b.title, b.author_id,a.indexinjournal,b.html_content,b.article_image
                from magazine_catalog as a left join magazine_article as b 
                on a.article_id=b.id 
                where a.journal_nom_id= "%s"
                order by a.indexinjournal"""%(journal_nom)
    cursor = connection.cursor()
    cursor.execute(sqlstring)
    articles=dictfetchall(cursor)
    return render_to_response('catalogue.html',Context({'journal':journal,'articles':articles}))

def aritcles(request,param):
    try:
        offset=int(param)
    except:
        raise Http404
    sqlstring="""
                select b.id,b.title
                from magazine_catalog as a left join magazine_article as b 
                on a.article_id=b.id 
                where a.journal_nom_id= "%s"
                order by a.indexinjournal"""%(offset)
    cursor = connection.cursor()
    cursor.execute(sqlstring)
    articles=dictfetchall(cursor)
    return render_to_response('content.html',Context({'articles':articles}))
def aritcle(request,param):
    try:
        offset=int(param)
    except:
        raise Http404
    aritcle=Article.objects.get(id=offset)
    return render_to_response('article.html',Context({'article':aritcle}),context_instance=RequestContext(request)) 

def article_show_comment(request, id):
    try:
        offset=int(id)
    except:
        raise Http404
    article = Article.objects.get(id=offset)
    return render_to_response('article_comments_show.html', {"article": article})