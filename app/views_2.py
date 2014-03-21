# -*- encoding: utf-8 -*-
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext

from app.forms import Input_trad

import subprocess

# Create your views here.
def index(request):
    title = 'Sistema de Tradução Português-Chinês'
    return render(request, 'app/index.html', {'title':title})

#def trad(request):
#    form = Input_trad()
#    
#    if request.method == 'POST':
#        form = Input_trad(request.POST)
#        if form.is_valid():
#            print 'Isto é um form: ', form
#            request.session['id_frase'] = request.POST
#            return HttpResponseRedirect('/app/result/')
#    else:
#        form = Input_trad()
#        
#    return render(request, 'app/trad.html', {'form': form})


def trad(request):
    print "cona"
    form = Input_trad()
    #print form
    print request.method
    print 'Cassss'
    if request.method == 'POST':
        print 'cenassssssssssssssssssssss'
        form = Input_trad(request.POST)
        if form.is_valid():
            request.session['id_frase'] = request.POST
            print request.POST['frase']
            #codigo para traduzir
            form = Input_trad(initial={'frase': request.POST['frase'], 'resultado': 'Tradução'})
            #return render(request, 'app/index.html', {'form': form})
    else:
        print 'geeeeet'
        form = Input_trad()

    return render(request, 'app/index.html', {'form': form})


#def result(request):
#    best_list = ['您好海伦！', '您海','海伦娜']
#    cenas = request.session.get('id_frase').get('frase')
#    print cenas
#    bl = {'best_list': best_list, 'cenas': cenas}
#        
#    print bl
#    return render(request, 'app/result.html', bl)

def result(request):
    str_input = request.session.get('id_frase').get('frase')
    working_str = 'working_pten'
    #print str_input
    
    bashCommand = 'echo "' + str_input + '" | ~/mosesdecoder/bin/moses -f ~/' + working_str + '/binarised-model/moses.ini -n-best-list ~/best_list.txt 10 distinct'

    process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, shell=True)

    output = process.communicate()[0]

    #print output

    best_trans_list = []		#lista com as best translations (em bruto)
    best_list = []          		#lista com as best translations (so' frases)
    f = open('/home/nelson/best_list.txt')

    line = f.readline()

    while line:

        best_trans_list.append(line)
        tokens = line.split()
        str = ''

        #retira os simbolos nao necessarios ficando só a frase que interessa
        for tok in tokens[2:]:

            if tok == '|||':
                #print "|||"
                break
            else:
                str += tok + " "

        best_list.append(str)
        #print str
        line = f.readline()

    #print best_list[1]
    f.close()



    bl = {'best_list': best_list, 'cenas': str_input}

    print bl
    return render(request, 'app/index.html', bl)

