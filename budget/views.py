import json
from decimal import Decimal, InvalidOperation

from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Expense


@csrf_exempt
@require_http_methods(["GET", "POST"])
def expenses_api(request):
    if request.method == "GET":
        expenses = Expense.objects.all()
        data = [
            {
                "id": e.id,
                "title": e.title,
                "amount": str(e.amount),
                "category": e.category,
                "date": str(e.date),
                "description": e.description,
            }
            for e in expenses
        ]
        return JsonResponse({"expenses": data})

    if request.method == "POST":
        try:
            body = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        title = body.get("title")
        amount = body.get("amount")
        category = body.get("category", "other")
        date = body.get("date")

        if not title or amount is None or not date:
            return JsonResponse(
                {"error": "title, amount, and date are required"}, status=400
            )

        try:
            amount = Decimal(str(amount))
        except (InvalidOperation, ValueError):
            return JsonResponse({"error": "Invalid amount"}, status=400)

        expense = Expense.objects.create(
            title=title,
            amount=amount,
            category=category,
            date=date,
            description=body.get("description", ""),
        )
        return JsonResponse(
            {
                "id": expense.id,
                "title": expense.title,
                "amount": str(expense.amount),
                "category": expense.category,
                "date": str(expense.date),
            },
            status=201,
        )


def dashboard(request):
    expenses = Expense.objects.all()
    total = expenses.aggregate(total=Sum("amount"))["total"] or Decimal("0")
    by_category = (
        expenses.values("category")
        .annotate(total=Sum("amount"))
        .order_by("-total")
    )
    return render(
        request,
        "budget/dashboard.html",
        {
            "expenses": expenses,
            "total": total,
            "by_category": by_category,
        },
    )
