from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
#from django.shortcuts import render
from django.urls import reverse
from django.template import loader

def index(request):
	#latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('brain/index.html')
	context = {}
	return HttpResponse(template.render(context, request))

def result(request):
	#template = loader.get_template('brain/result.html')
	context = {scode_text : request.POST['scode']}
	return HttpResponseRedirect(reverse('brain:test',args=(context,)))
	
def test(request):
	return render(request, '/brain/test.html', {'scode_text':'asd'})

'''
def detail(request, question_id):
	return render(request, 'polls/detail.html', {'question': get_object_or_404(Question, pk=question_id)})

def detail(request, question_id):
	return HttpResponse("You're looking at question %s." % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
'''
