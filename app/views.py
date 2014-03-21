# -*- encoding: utf-8 -*-
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext

from app.forms import Input_trad, ShowBest

import subprocess


# def index(request):
#     title = 'Sistema de Tradução Português-Chinês'
#     return render(request, 'app/index.html', {'title':title})

global c
c = 'pten'
def trad(request):
    
    form = Input_trad()
            
    best_trans_list = []        #lista com as best translations (em bruto)
    best_list = []              #lista com as best translations (so' frases)
    #print request.method

    if request.method == 'POST':
        #print 'POST!'
        form = Input_trad(request.POST)
        if form.is_valid():
            request.session['id_frase'] = request.POST
            #print request.POST['frase']
            print request.POST
            if 'button' in request.POST:
                print request.POST['button']
                c = request.POST['button']

            #print request.session.get('id_frase').get('frase')
            #codigo para traduzir
            str_input = request.POST['frase']
            working_str = 'working_' + c
            #print str_input
            
            bashCommand = 'echo "' + str_input \
                    + '" | ~/mosesdecoder/bin/moses -f ~/' \
                    + working_str \
                    + '/binarised-model/moses.ini -n-best-list \
                    ~/best_list.txt 10 distinct > log.txt'
        
            process = subprocess.Popen(bashCommand, 
                                       stdout=subprocess.PIPE, shell=True)
        
            output = process.communicate()[0]
        
            #print output
            f = open('/home/nelson/best_list.txt')
        
            line = f.readline()
        
            while line:
        
                best_trans_list.append(line)
                tokens = line.split()
                str = ''
        
                ''' retira os simbolos nao necessarios
                ficando só a frase que interessa
                '''
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
            
            p = open('frase', 'w')
            p.write(str_input.encode('utf8'))
            f.close()
            
            form = Input_trad(initial={'frase': request.POST['frase'], \
                                       'resultado': best_list[0]})
            
    else:
        #print 'GET!'
        form = Input_trad()

    return render(request, 'app/index.html', {'form': form, \
                                              'best_list': best_list[1:]})


def treino(request):
    
    if request.method == 'POST':
        print 'PRINT SELECT'
        print request.POST["select1"]
        resposta = request.POST["select1"]
        t = open('traducao', 'w')
        t.write(resposta.encode('utf8'))
        t.close()
#         
#         bashCommand = 'echo "' + str_input \
#                     + '" | ~/mosesdecoder/bin/moses -f ~/' \
#                     + working_str \
#                     + '/binarised-model/moses.ini -n-best-list \
#                     ~/best_list.txt 10 distinct > log.txt'
#         
#             process = subprocess.Popen(bashCommand, 
#                                        stdout=subprocess.PIPE, shell=True)
#         
#             output = process.communicate()[0]
        
    else:
        print 'ERRO NO SLELECT'
        
    return render(request, 'app/treino.html', {'resposta': resposta})