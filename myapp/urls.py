from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.employee_create, name='create'),
    path('detail/<int:pk>/', views.employee_detail, name='detail'),
    path('update/<int:pk>/', views.employee_update, name='update'),
    path('delete/<int:pk>/', views.employee_delete, name='delete'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('attendance/', views.attendance_view, name='attendance'),
    path('approval/', views.approval_view, name='approval'),
    path('approval/<int:req_id>/<str:status>/', views.update_request_status, name='update_request_status'),
    path('payroll/', views.payroll_view, name='payroll'),
    path('payroll/export-bank/', views.export_bank_file, name='export_bank_file'),
    path('reports/', views.report_view, name='reports'),
    path('ess/', views.ess_dashboard, name='ess_dashboard'),
]

