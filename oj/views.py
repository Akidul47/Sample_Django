from django.shortcuts import render

from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .forms import CompilerModelForm
from .models import CompilerModel


class IndexView(CreateView):
    template_name = "oj/index.html"
    form_class = CompilerModelForm
    success_url = '/thanks/'

    def form_valid(self, form):
        return super().form_valid(form)


class SubmitView(TemplateView):
    template_name = "oj/success.html"
