from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import TeamLeader, ACM, Files

@admin.register(TeamLeader)
class TeamLeaderAdmin(ImportExportModelAdmin):
   list_display = ('name', 'branch')  # Fields to display in the list view

@admin.register(ACM)
class ACMAdmin(ImportExportModelAdmin):
    list_display = ('name', 'branch', 'shift', 'team_leader')  # Fields to display in the list view

@admin.register(Files)
class FilesAdmin(ImportExportModelAdmin):
   list_display = ('client_name', 'product_name', 'account_number', 'balance', 'account_name', 'termination_code', 'acm')  # Fields to display in the list view