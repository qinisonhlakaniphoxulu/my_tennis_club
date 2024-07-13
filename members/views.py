from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    members = Member.objects.all()
    template = loader.get_template('all_members.html')
    membersDict = {'members' : members}
    return HttpResponse(template.render(membersDict, request))

def details(request, id):
    member = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    membersDict = {'member' : member}
    return HttpResponse(template.render(membersDict, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def memberstable(request):
    members = Member.objects.all()
    template = loader.get_template('memberstable.html')
    context = {
        'members': members
    }
    return HttpResponse(template.render(context, request))

def testing(request):
    members = Member.objects.all()
    template = loader.get_template('template.html')
    context = {
        'members': members
    }
    return HttpResponse(template.render(context, request))