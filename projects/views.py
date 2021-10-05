from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .utils import searchProjects, paginateProjects



def projects(request):
    projects , search_query = searchProjects(request)
    custom_range, projects = paginateProjects(request, projects, 3)
    
    context = {"projects" : projects, 'search_query' : search_query, 'custom_range' : custom_range }
    return render(request, 'projects/project.html',context)

def project_view(request, pk):
    projectObj = Project.objects.get(id= pk)
    review = projectObj.review.all()
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.project = projectObj
            review.owner = request.user.profile
            review.save()
            projectObj.getVoteCount
            messages.success(request, 'Your review has been posted!')
            return redirect('project_view', pk=projectObj.id)
    context = {"project" : projectObj, 'review' : review, 'form' : form}
    return render(request, "projects/single-project.html", context)

@login_required(login_url = 'login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            messages.success(request, "Project has been Successfully Added!")
            return redirect('projects')
    context = {'form' : form}
    return render(request, 'projects/project_form.html',context)    

@login_required(login_url = 'login')
def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST,request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "Project has been Successfully Updated!")
            return redirect('projects')

    context = {'form' : form}
    return render(request, 'projects/project_form.html',context)            

@login_required(login_url = 'login')
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        messages.success(request, "Project has been Successfully Removed!")
        return redirect('projects')
    context = {"object" : project}
    return render(request, 'delete_template.html',context)