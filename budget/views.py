from django.http import HttpResponse
from django.shortcuts import render


def project_list(request):
    """List all projects."""
    return render(request, "budget/project-list.html")


def project_details(request, project_slug):
    """Show details for a specific project."""
    return render(
        request, "budget/project-details.html", context={"name": project_slug}
    )
