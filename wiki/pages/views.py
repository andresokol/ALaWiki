from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from pages.models import Page

def index(request):
    page_list = Page.objects.order_by('title')
    template = loader.get_template('pages/index.html')
    art_titles = []
    for elem in page_list:
        if elem.name == '':
            elem.name = elem.title.replace('_', ' ')
    context = RequestContext(request, {
        'page_list': page_list,
    })
    return HttpResponse(template.render(context))

def get_article(request, title):
    art_title = title.replace('_', ' ')
    try:
        page = Page.objects.get(title=title)
        text = page.article
        template = loader.get_template('pages/page.html')
        context = RequestContext(request, {
            'ArtTitle': art_title, 'ArtText': text, 'Path': title,
        })
        return HttpResponse(template.render(context))
    except:
        template = loader.get_template('pages/nopage.html')
        context = RequestContext(request, {
            'ArtTitle': art_title, 'Path': title,
        })
        return HttpResponse(template.render(context))

def edit_article(request, title):
    art_title = title.replace('_', ' ')
    try:
        page = Page.objects.get(title=title)
        text = page.article
    except:
        text = ''
    template = loader.get_template('pages/edit.html')
    context = RequestContext(request, {
        'ArtTitle': art_title, 'ArtText': text, 'Path': title,
    })
    return HttpResponse(template.render(context))

def submit_changes(request, title):
    try:
        page = Page.objects.get(title=title)
        page.change(request.POST['text-field'])
    except:
        page = Page(title=title, article=request.POST['text-field'])
    page.save()
    return HttpResponseRedirect('/wiki/' + title)

def create_article(request):
    art_title = request.POST['titel']
    title = art_title.replace(' ', '_')
    return HttpResponseRedirect('/wiki/' + title + '/edit/')
