from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404

from .models import Budget
from .forms import BudgetForm


# Show All Budget

def budget_list(request):

    budgets = Budget.objects.all()

    return render(request, 'budget_app/budget_list.html', {
        'budgets': budgets
    })


# Add Budget

def budget_add(request):

    if request.method == 'POST':

        form = BudgetForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('budget_list')

    else:

        form = BudgetForm()

    return render(request, 'budget_app/budget_form.html', {
        'form': form
    })


# Edit Budget

def budget_edit(request, id):

    budget = get_object_or_404(Budget, id=id)

    if request.method == 'POST':

        form = BudgetForm(request.POST, instance=budget)

        if form.is_valid():

            form.save()

            return redirect('budget_list')

    else:

        form = BudgetForm(instance=budget)

    return render(request, 'budget_app/budget_form.html', {
        'form': form
    })


# Delete Budget

def budget_delete(request, id):

    budget = get_object_or_404(Budget, id=id)

    if request.method == 'POST':

        budget.delete()

        return redirect('budget_list')

    return render(request, 'budget_app/delete.html', {
        'budget': budget
    })