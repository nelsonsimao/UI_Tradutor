'''
Created on Jan 5, 2014

@author: nelson
'''
from django import forms


class Input_trad(forms.Form):
    frase = forms.CharField(widget=forms.Textarea(
                attrs={
                       'class':'text',
                       'rows':5, 
                       'cols':50,
                       'wrap':'SOFT',
                       'style':'overflow: hidden; resize:none; height: 187px;',
                       'placeholder':'Insira texto'}), 
                required=True)
    resultado = forms.CharField(max_length=200, widget=forms.Textarea(
                attrs={
                       'rows':5, 
                       'cols':50, 
                       'placeholder':'Texto traduzido'}),
                required=False)
    
    #CHOICES = ('pten', 'enpt', 'ptcn')    
    #lingua = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    
class ShowBest(forms.Form):
    #best_trans = forms.ChoiceField(max_length=100)
    escolhida = forms.ChoiceField(widget=forms.Select)
    