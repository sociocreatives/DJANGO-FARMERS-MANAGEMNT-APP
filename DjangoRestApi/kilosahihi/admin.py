from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin
from kilosahihi.models import UserFarmers

admin.site.register(models.UserPermissions)
admin.site.register(models.Produce)
admin.site.register(models.UserRoles)
admin.site.register(models.UserAttributes)
admin.site.register(models.ProduceVariety)
admin.site.register(models.Banks)
admin.site.register(models.UserBankAccounts)
admin.site.register(models.Unions)
admin.site.register(models.Cooperatives)
admin.site.register(models.Factories)
admin.site.register(models.SmallHolderEstates)
admin.site.register(models.UserUnions)

admin.site.register(models.UserSmallHolderEstates)
admin.site.register(models.UserCooperative)
admin.site.register(models.UserFieldOfficers)

@admin.register(UserFarmers)
class UserFarmersAdmin(ImportExportModelAdmin):
    list_display = ("farmer_number", "member_name", "county", "sub_county", "id_no", "year_of_birth", "phone_number", "no_of_trees")
    

admin.site.register(models.Farms)
admin.site.register(models.Devices)
admin.site.register(models.FarmersTransactions)

admin.site.register(models.SmallHolderEstateTransactions)
admin.site.register(models.FarmerIncomeSource)
admin.site.register(models.FarmerDebts)
admin.site.register(models.SmallHolderEstateIncomeSource)
admin.site.register(models.SmallHolderEstateDebts)
admin.site.register(models.FarmInputs)
admin.site.register(models.FarmerInputRequest)

admin.site.register(models.SmallHolderEstateInputRequest)
admin.site.register(models.Payment)
admin.site.register(models.Audits)

