# -*- encoding: utf-8 -*-
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext

from app.forms import Input_trad


# Create your views here.
def index(request):
    title = 'Sistema de Tradução Português-Chinês'
    return render(request, 'app/index.html', {'title':title})

def trad(request):
    form = Input_trad()
    
    if request.method == 'POST':
        form = Input_trad(request.POST)
        if form.is_valid():
            print 'Isto é um form: ', form
            request.session['id_frase'] = request.POST
            return HttpResponseRedirect('/app/result/')
    else:
        form = Input_trad()
        
    return render(request, 'app/trad.html', {'form': form})

def result(request):
    best_list = ['您好海伦！', '您海','海伦娜']
    cenas = request.session.get('id_frase').get('frase')
    print cenas
    bl = {'best_list': best_list, 'cenas': cenas}
        
    print bl
    return render(request, 'app/result.html', bl)