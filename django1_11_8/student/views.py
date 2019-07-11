from django.shortcuts import render
from django.urls import reverse
from django.views import View
from .models import Student
from .forms import StudentForm
from django.http import HttpResponseRedirect
# Create your views here.

class IndexView(View):
    template_name = 'index.html'

    def get_context(self):
        students = Student.get_all()
        context = {
            'students': students,
        }
        return context

    def get(self, request):
        context = self.get_context()
        form = StudentForm()
        context.update({
            'form': form
        })
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        context = self.get_context()
        context.update({
            'form': form
        })
        return render(request, self.template_name, context=context)
























def index(request):
    # words = 'Words!'
    # return render(request, 'index.html', context={'words': words})
    students = Student.get_all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentForm()
    context = {
        'students': students,
        'form': form,
    }
    return render(request, 'index.html', context=context)