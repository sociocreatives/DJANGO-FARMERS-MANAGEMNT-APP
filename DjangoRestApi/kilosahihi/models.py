from django.db import models
from django.conf import settings


################################# KILOSAHIHI START #############################################

class UserPermissions(models.Model):
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "User Permissions"

class UserRoles(models.Model):
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "User Roles"

class UserAttributes(models.Model):
    name = models.CharField(max_length=50)
    user =  models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    gender =  models.CharField(max_length=10)
    national_id =  models.CharField(max_length=20)
    address =  models.CharField(max_length=50)
    contact = models.CharField(max_length=20)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "User Attributes"

class Produce(models.Model):
    name = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Produce"


class ProduceVariety(models.Model):
    name = models.CharField(max_length=50, unique=True)
    produce =  models.ForeignKey(Produce,on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Produce Variety"

class Banks(models.Model):
    name = models.CharField(max_length=50, unique=True)
    reg_date  = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Banks"

class UserBankAccounts(models.Model):
    name = models.CharField(max_length=50)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    bank = models.ForeignKey(Banks,on_delete=models.CASCADE,null=True)
    account = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Bank Account"

class Unions(models.Model):
    name = models.CharField(max_length=50,unique=True)
    reg_date  = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Unions"

class Cooperatives(models.Model):
    name = models.CharField(max_length=50,unique=True)
    union = models.ForeignKey(Unions,on_delete=models.CASCADE,null=True)
    growers_code = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    status = models.CharField(max_length=10)
    reg_date  = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Cooperatives"

class Factories(models.Model):
    name = models.CharField(max_length=50, unique=True)
    cooperative =  models.ForeignKey(Cooperatives,on_delete=models.CASCADE,null=True)
    zone = models.CharField(max_length=50)
    reg_date  = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Factories/Collection Centres"

class SmallHolderEstates(models.Model):
    name = models.CharField(max_length=50, unique=True)
    union =  models.ForeignKey(Unions,on_delete=models.CASCADE,null=True)
    region = models.CharField(max_length=50)
    growers_code = models.CharField(max_length=50)
    geolocation = models.CharField(max_length=50)
    reg_date  = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Small Holder Estates"

class UserUnions(models.Model):
    name = models.CharField(max_length=50,blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    union = models.ForeignKey(Unions,on_delete=models.CASCADE,null=True)
    permission = models.ForeignKey(UserPermissions,on_delete=models.CASCADE,null=True)
    role = models.ForeignKey(UserRoles,on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "User Unions"

class UserSmallHolderEstates(models.Model):
    name = models.CharField(max_length=50,blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    smallholderestate = models.ForeignKey(SmallHolderEstates,on_delete=models.CASCADE,null=True)
    permission = models.ForeignKey(UserPermissions,on_delete=models.CASCADE,null=True)
    role = models.ForeignKey(UserRoles,on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "User Small Holder Estates"

class UserCooperative(models.Model):
    name = models.CharField(max_length=50,blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    cooperative = models.ForeignKey(Cooperatives,on_delete=models.CASCADE,null=True)
    permission = models.ForeignKey(UserPermissions,on_delete=models.CASCADE,null=True)
    role = models.ForeignKey(UserRoles,on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "User Cooperative Societies"

class UserFieldOfficers(models.Model):
    name = models.CharField(max_length=50,blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    factory = models.ForeignKey(Factories,on_delete=models.CASCADE,null=True)
    employee_number = models.CharField(max_length=50)
    permission = models.ForeignKey(UserPermissions,on_delete=models.CASCADE,null=True)
    role = models.ForeignKey(UserRoles,on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "User Field Officers"

class UserFarmers(models.Model):
    # user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,unique=True)
    farmer_number = models.CharField(max_length=50,null=True,unique=False)
    member_name = models.CharField(max_length=50,null=True,blank=True)
    county = models.CharField(max_length=50,null=True,blank=True)
    sub_county = models.CharField(max_length=50,null=True,blank=True)
    id_no = models.CharField(max_length=50,null=True,blank=True)
    year_of_birth = models.CharField(max_length=50,null=True,blank=True)
    phone_number = models.CharField(max_length=50,null=True,blank=True)
    no_of_trees = models.CharField(max_length=50,null=True,blank=True)

    def __str__ (self):
        return str(self.member_name)
    class Meta:
        verbose_name_plural = "User Farmers"

class Farms(models.Model):
    name = models.CharField(max_length=50)
    farmer = models.ForeignKey(UserFarmers,on_delete=models.CASCADE,null=True)
    acres  = models.CharField(max_length=20, unique=True)
    trees  = models.CharField(max_length=20, unique=True)
    reg_date  = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Farms"

class Devices(models.Model):
    name = models.CharField(max_length=50)
    factory = models.ForeignKey(Factories,on_delete=models.CASCADE,null=True)
    imei  = models.CharField(max_length=50, unique=True)
    reg_date  = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Devices"

class FarmersTransactions(models.Model):
    name = models.CharField(max_length=50,unique=True)
    farmer = models.ForeignKey(UserFarmers,on_delete=models.CASCADE,null=True)
    fieldofficer = models.ForeignKey(UserFieldOfficers,on_delete=models.CASCADE,null=True)
    device = models.ForeignKey(Devices,on_delete=models.CASCADE,null=True)
    variety = models.ForeignKey(ProduceVariety,on_delete=models.CASCADE,null=True)
    gross_weight  = models.CharField(max_length=20)
    net_weight  = models.CharField(max_length=20)
    tare_weight  = models.CharField(max_length=20,null=True)
    number_of_bags = models.CharField(max_length=20,null=True)
    total_amount = models.CharField(max_length=20,null=True)
    amount_deductable = models.CharField(max_length=20,null=True)
    amount_payable = models.CharField(max_length=20,null=True)
    tx_date  = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Farmers Transactions"

class SmallHolderEstateTransactions(models.Model):
    name = models.CharField(max_length=50, blank=True)
    smallholderestate = models.ForeignKey(UserSmallHolderEstates,on_delete=models.CASCADE,null=True)
    variety = models.ForeignKey(ProduceVariety,on_delete=models.CASCADE,null=True)
    delivery  = models.CharField(max_length=20)
    tare_weight  = models.CharField(max_length=20,null=True)
    net_weight  = models.CharField(max_length=20)
    number_of_bags = models.CharField(max_length=20,null=True)
    total_amount = models.CharField(max_length=20,null=True)
    amount_deductable = models.CharField(max_length=20,null=True)
    amount_payable = models.CharField(max_length=20,null=True)
    tx_date  = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Small Holder Estates Transactions"

class FarmerIncomeSource(models.Model):
    name = models.DateTimeField(auto_now_add=True, blank=True)
    farmer = models.ForeignKey(UserFarmers,on_delete=models.CASCADE)
    source = models.CharField(max_length=50)
    total_amount = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Farmer Income Source"

class FarmerDebts(models.Model):
    name = models.DateTimeField(auto_now_add=True, blank=True)
    farmer = models.ForeignKey(UserFarmers,on_delete=models.CASCADE)
    institution = models.CharField(max_length=50)
    total_amount = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Farmer Debts"


class SmallHolderEstateIncomeSource(models.Model):
    name = models.DateTimeField(auto_now_add=True, blank=True)
    smallholderestate = models.ForeignKey(UserSmallHolderEstates,on_delete=models.CASCADE)
    source = models.CharField(max_length=50)
    total_amount = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Small Holder Estate Income Source"

class SmallHolderEstateDebts(models.Model):
    name = models.CharField(max_length=50, blank=True)
    smallholderestate = models.ForeignKey(UserSmallHolderEstates,on_delete=models.CASCADE)
    institution = models.CharField(max_length=50)
    total_amount = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Smaller Holder Estate Debts"

class FarmInputs(models.Model):
    name = models.CharField(max_length=50, blank=True)
    
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Farm Inputs"

class FarmerInputRequest(models.Model):
    name = models.CharField(max_length=50, blank=True)
    farmer = models.ForeignKey(UserFarmers,on_delete=models.CASCADE,null=True)
    cooperative = models.ForeignKey(Cooperatives,on_delete=models.CASCADE,null=True)
    inputid = models.ForeignKey(FarmInputs,on_delete=models.CASCADE,null=True)
    desc = models.CharField(max_length=50)
    cost_per_unit = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    reason = models.CharField(max_length=50)
    total_amount = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Farm Input Request"

class SmallHolderEstateInputRequest(models.Model):
    name = models.CharField(max_length=50, blank=True)
    smallholderestate = models.ForeignKey(UserSmallHolderEstates,on_delete=models.CASCADE,null=True)
    union = models.ForeignKey(Unions,on_delete=models.CASCADE,null=True)
    inputid = models.ForeignKey(FarmInputs,on_delete=models.CASCADE,null=True)
    desc = models.CharField(max_length=50)
    cost_per_unit = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    reason = models.CharField(max_length=50)
    total_amount = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Farm Input Request"

class Payment(models.Model):
    name = models.CharField(max_length=50, blank=True)
    payment_code = models.CharField(max_length=50)
    tx_reference = models.ForeignKey(FarmersTransactions,on_delete=models.CASCADE,null=True)
    method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50)
    payment_date = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Payment"

class Audits(models.Model):
    name = models.CharField(max_length=50)
    action = models.TextField()
    user = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Audits"

############################# KILOSAHIHI END #############################################

