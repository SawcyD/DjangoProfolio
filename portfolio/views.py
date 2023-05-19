from django.shortcuts import render
from .models import Projects

# Create your views here.

def projectList(request):
	projects = Projects.objects.all()
	context = {
		'projects': projects
	}
	return render(request, 'base.html', context)

def fullView(request, pk):
	project = Projects.objects.get(pk=pk)
	context = {
		'project': project
	}
	return render(request, 'fullView.html', context)