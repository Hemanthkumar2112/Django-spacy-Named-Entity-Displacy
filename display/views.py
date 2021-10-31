from django.shortcuts import render
import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_sm')
def index(request):
    context = {}
    if request.method =='POST':
        text = nlp(request.POST['text'])
        html = displacy.render(text,style='ent')
        context['data'] = html

         

  
    return render(request,'index.html',context=context )