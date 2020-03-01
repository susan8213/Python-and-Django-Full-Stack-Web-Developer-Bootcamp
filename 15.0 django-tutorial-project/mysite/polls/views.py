from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from django.views import generic

from .models import Question

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:5]

def index(request):
    latest_question_list = Question.objects.order_by('-published_date')[:5]
    context = {'latest_question_list': latest_question_list}
    
    # render() is the shortcut for 'template = loader.get_template() -> HttpResponse(template.render())'
    return render(request, 'polls/index.html', context)

    # hard code
    # return HttpResponse("You're looking at index page."")

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

def detail(request, pk):
    # try:
    #     question = Question.objects.get(pk=pk)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    # shortcut for above
    question = get_object_or_404(Question, pk=pk)

    return render(request, 'polls/detail.html', {'question': question})
    # hard code
    # return HttpResponse("You're looking at question %s" % pk)

class ResultsView(generic.DeleteView):
    model = Question
    template_name = 'polls/results.html'

def results(request, pk):
    question = get_object_or_404(Question, pk=pk)

    return render(request, 'polls/results.html', {'question': question})

def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

        # reverse() helps avoid having to hardcode a URL in the view function. 
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))