from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.core.urlresolvers import reverse
import random

from daodejing.models import *

def index(request):
    daodej_list=Daodej.objects.order_by('zhangjie')
    context={'daodej_list':daodej_list}
    return render(request,'daodejing/index.html',context)

def detail(request,daodej_id):
    daodej=get_object_or_404(Daodej,pk=daodej_id)
    return render(request,'daodejing/detail.html',{'daodej':daodej})

def results(request,poll_id):
    poll=get_object_or_404(Poll,pk=poll_id)
    return render(request,'polls/results.html',{'poll':poll})

def vote(request,poll_id):
    p=get_object_or_404(Poll,pk=poll_id)
    try:
        selected_choice=p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'poll':p,
            'error_message':"You didn't select a choice.",
            })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))

def getone(request,dbanben=0):
    nmax=Daodej.objects.filter(banben=dbanben).count()
    daodej=get_object_or_404(Daodej,pk=random.randint(1,nmax))
    return render(request,'daodejing/detail.html',{'daodej':daodej})