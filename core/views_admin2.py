from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from core.views_admin import is_admin
from users.models import CustomUser
from tasks.models import Project, Task, WeeklyReport
from files.models import File

@user_passes_test(is_admin)
def admin2_dashboard(request):
    return render(request, 'core/admin2_dashboard.html')

@user_passes_test(is_admin)
def admin2_projects(request):
    from django.db import models
    projects = Project.objects.all().order_by(
        models.Case(
            models.When(status='active', then=0),
            models.When(status='pending', then=1),
            models.When(status='archived', then=2),
            default=3,
            output_field=models.IntegerField(),
        ),
        '-created_at'
    )
    return render(request, 'core/admin2_projects.html', {'projects': projects})

@user_passes_test(is_admin)
def admin2_tasks(request):
    tasks = Task.objects.select_related('project').all().order_by('-created_at')
    return render(request, 'core/admin2_tasks.html', {'tasks': tasks})

@user_passes_test(is_admin)
def admin2_reports(request):
    reports = WeeklyReport.objects.select_related('user', 'project').all().order_by('-week_start')
    return render(request, 'core/admin2_reports.html', {'reports': reports})

@user_passes_test(is_admin)
def admin2_files(request):
    files = File.objects.select_related('uploader').all().order_by('-uploaded_at')
    return render(request, 'core/admin2_files.html', {'files': files})
