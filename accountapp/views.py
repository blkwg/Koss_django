from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decoraters import account_ownership_required
from accountapp.models import Helloworld
from accountapp.templates.forms import AccountUpdateForm

has_ownership = [account_ownership_required, login_required]

@login_required
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






class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'








