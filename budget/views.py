from django.http import HttpResponse
from django.shortcuts import render


def project_list(request):
    """List all projects."""
    return HttpResponse("Project list")


def project_details(request, project_slug):
    """Show details for a specific project."""
    return HttpResponse(f"Project detail for {project_slug}")
