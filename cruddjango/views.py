from django.shortcuts import render,redirect
from django.contrib import messages
from cruddjango.models import Member

# Create your views here.

def home(request):
    members=Member.objects.all()
    context={'members':members}
    return render(request,"index.html",context)

def create(request):
    member=Member()
    member.firstname=request.POST['firstname']
    member.lastname=request.POST['lastname']
    member.contact=request.POST['contact']
    member.address=request.POST['address']
    member.save()
    return redirect('/')

def edit(request):
    id=request.GET['id']
    member=Member.objects.get(id=id)
    context={'members':member}
    return render(request,"edit.html",context)

def update(request):
    id=request.POST['id']
    member=Member.objects.get(id=id)
    member.id=request.POST['id']
    member.firstname=request.POST['firstname']
    member.lastname=request.POST['lastname']
    member.contact=request.POST['contact']
    member.address=request.POST['address']
    member.save()
    return redirect('/')

def delete(request):
    id=request.GET['id']
    Member.objects.filter(id=id).delete()
    context={'members':Member}
    return redirect('/')
