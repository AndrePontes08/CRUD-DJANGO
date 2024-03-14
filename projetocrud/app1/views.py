#from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

def index(request):
  
  users = User.objects.all()
  context = {
        'users':users
  }  
  return render(request, 'index.html',context)

def create(request):

  if request.method == 'GET':
    form = UserForm()

    context = {
      'form': form,
    }

    return render(request, 'criar.html',context=context)
  else:
    form = UserForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect(index)


def refresh(request,user_id):

  user = User.objects.get(pk=user_id)
  
  if request.method == "POST":
    form = UserForm(data=request.POST,instance=user)
    
    if form.is_valid():
      form.save()
      return redirect(index)
  else:
    form = UserForm(instance=user)

    context = {"form": form}

    return render(request,'criar.html',context=context)
  

def delete(request,user_id):

  user = User.objects.get(pk=user_id)
  user.delete()

  return redirect(index)

  