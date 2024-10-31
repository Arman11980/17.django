from django.shortcuts import render
from django.views.generic import TemplateView


class ShabClass(TemplateView):
    template_name = 'second_task/class_template.html'


def shab_func(request):
    return render(request, 'second_task/func_template.html')

