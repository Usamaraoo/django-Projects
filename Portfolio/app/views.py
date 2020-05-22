from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import (View, TemplateView, ListView, DeleteView, DetailView, CreateView)
from .forms import DeveloperForm
from .models import Developer
from django.core.mail import send_mail

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


class DeveloperList(ListView):
    model = Developer
    template_name = 'app/developer_list.html'


class DeveloperDetail(DetailView):
    model = Developer
    template_name = 'app/developer_detail.html'
    context_object_name = 'person'

    def get_queryset(self):
        return Developer.objects.all()


class NewDeveloper(CreateView):
    form_class = DeveloperForm
    model = Developer
    context_object_name = 'dev'

    def posted(self, request):

        if request.method == 'POST':
            form = DeveloperForm(request.POST, request.FILES)
            if form.is_valid():
                developer = form.save(commit=False)
                developer.profile_pic = request.FILES['profile_pic']
                file_type = developer.display_picture.url.split('.')[-1]
                file_type = file_type.lower()

                if file_type not in IMAGE_FILE_TYPES:
                    return HttpResponse('error.html')
                developer.save()
                return redirect('success')
            else:
                print(form.errors)
        else:
            form = DeveloperForm()


def success(request):
    return HttpResponse('successfully uploaded')



