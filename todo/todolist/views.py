from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.
def index(request):
    todo = Articles.objects.order_by('priority')
    return render(request, 'todolist/index.html', {'todo' : todo})

class todoDetailView(DetailView):
    model = Articles
    template_name = 'todolist/details_view.html'
    context_object_name = 'article'

class todoUpdateViews(UpdateView):
    model = Articles
    template_name = 'todolist/create.html'

    form_class = ArticlesForm

class todoDeleteViews(DeleteView):
    model = Articles
    success_url = '/'
    template_name = 'todolist/delete.html'

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main-page')
        else:
            error = 'Ошибка'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }


    return render(request, 'todolist/create.html',data)
