from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from accountapp.models import Helloworld


def hello_world(request):

    if request.method == "POST":
        temp = request.POST.get('hello_world_input')

        new_hello_world = Helloworld()
        new_hello_world.text = temp
        new_hello_world.save()

        hello_world_list = Helloworld.objects.all()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))

    else:
        hello_world_list = Helloworld.objects.all()
        return render(request, 'accountapp/helloworld.html', context={'hello_world_output': hello_world_list})


#-------------------------------------------

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    succes_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'


