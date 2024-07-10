from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    members = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    membersDict = {'members' : members}
    return HttpResponse(template.render(membersDict, request))

def details(request, id):
    member = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    membersDict = {'member' : member}
    return HttpResponse(template.render(membersDict, request))