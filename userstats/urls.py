from django.urls import path
from . views import ExpenseSummaryStats, IncomeSourcesSummaryStats

urlpatterns = [
    path('expenses_category_data', ExpenseSummaryStats.as_view(), name='expense-category-summary'),
    path('income_sources_data', IncomeSourcesSummaryStats.as_view(), name='income_sources_data'),
]
