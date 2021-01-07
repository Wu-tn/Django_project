#wxapp view.py
import json

from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Question,Choice
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('wxapp/index.html')
    #output = ', '.join([q.question_text for q in latest_question_list])
    context = {
        'latest_question_list':latest_question_list,
    }
    #return HttpResponse(template.render(context,request))
    return render(request,'wxapp/index.html',context)

def detail(request, question_id):
    """ try:
         question = Question.objects.get(pk=question_id)
     except Question.DoesNotExist:
         raise Http404("Question does not exist")
     return render(request,"wxapp/detail.html",{'question':question})
     """
   #用 get_object_or_404快捷函数代替try except
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'wxapp/detail.html',{'question':question})

def results(request, question_id):
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % question_id)
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'wxapp/results.html',{'question':question})
'''
class IndexView(generic.ListView):
    template_name = 'wxapp/index.html'
    context_object_name = 'latest_question_list'    #调用get_queryset

    # 错误显示了未来的question
    # def get_queryset(self):
    #     '''Return the last five published quetsions.'''
    #     return Question.objects.order_by('-pub_date')
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        '''Question.objects.filter(pub_date__lte=timezone.now()) 
        returns a queryset containing Questions whose pub_date is less than or equal to - that is, earlier than or equal to - timezone.now.
        '''
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'wxapp/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'wxapp/results.html'

def vote(request, question_id):
    #return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'wxapp/detail.html',{
            'question':question,
            'error_message':"You do not select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    #reverse函数可以避免硬编码，使用urls中定义的name去访问url
    return HttpResponseRedirect(reverse('wxapp:results',args=(question_id,)))

def service(request):
    formula = request.GET['formula']
    try:
        result = eval(formula, {})
    except:
        result = 'Error formula'
    return HttpResponse(result)

