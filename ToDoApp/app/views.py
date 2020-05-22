from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import ToDo
from django.http import HttpResponseRedirect


def app(request):
    all_items = ToDo.objects.all().order_by("-added_date")
    return render(request, 'app.html', {'all_items': all_items})


@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    if content != "":
        ToDo.objects.create(text=content, added_date=current_date)
    else:
        return HttpResponse("Invalid val")

    return HttpResponseRedirect("/")


@csrf_exempt
def delete(request, item_id):
    # print(request.POST['content'])
    item = ToDo.objects.get(pk=item_id).delete()
    print(item)
    print(item)
    return HttpResponseRedirect("/")
