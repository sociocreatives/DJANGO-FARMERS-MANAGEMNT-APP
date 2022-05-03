from rest_framework import serializers 
from kilosahihi.models import *
from django.contrib.auth.models import User


############################# KILOSAHIHI #############################################

class UsersViewSerializer(serializers.ModelSerializer): #Has view
    class Meta:
        model = User
        fields = '__all__'
      

class UsersSerializer(serializers.ModelSerializer): #Has view
    class Meta:
        model = User
        fields = '__all__'
        

class PaymentSerializer(serializers.ModelSerializer): #Has view
    class Meta:
        model = Payment
        fields = '__all__'

class PaymentViewSerializer(serializers.ModelSerializer): #Has view
    class Meta:
        model = Payment
        fields = '__all__'
        

class AuditsViewSerializer(serializers.ModelSerializer): #Has view
    class Meta:
        model = Audits
        fields = '__all__'
       
class UserPermissionsSerializer(serializers.ModelSerializer): #has view
    class Meta:
        model = UserPermissions
        fields = '__all__'
        

class UserRolesSerializer(serializers.ModelSerializer): #has view
    class Meta:
        model = UserRoles
        fields = '__all__'
        

class UserAttributesSerializer(serializers.ModelSerializer):#has view
    class Meta:
        model = UserAttributes
        fields = '__all__'
        

class ProduceSerializer(serializers.ModelSerializer):#has view
    class Meta:
        model = Produce
        fields = '__all__'
       

class ProduceVarietySerializer(serializers.ModelSerializer):#has view
    class Meta:
        model = ProduceVariety
        fields = '__all__'
       

class BanksSerializer(serializers.ModelSerializer):#has view
    class Meta:
        model = Banks
        fields = '__all__'
        

class UserBankAccountsSerializer(serializers.ModelSerializer):#has view
    class Meta:
        model = UserBankAccounts
        fields = '__all__'
       

class UnionsSerializer(serializers.ModelSerializer):#has view
    class Meta:
        model = Unions
        fields = '__all__'
       

class CooperativesSerializer(serializers.ModelSerializer):#has view
    class Meta:
        model = Cooperatives
        fields = '__all__'
       

class FactoriesSerializer(serializers.ModelSerializer):#has view
    class Meta:
        model = Factories
        fields = '__all__'
          

class SmallHolderEstatesSerializer(serializers.ModelSerializer):#has view
    class Meta:
        model = SmallHolderEstates
        fields = '__all__'
           

class UserUnionsSerializer(serializers.ModelSerializer):#has view
    class Meta:
        model = UserUnions
        fields = '__all__'
       

class UserSmallHolderEstatesSerializer(serializers.ModelSerializer): #has view
    class Meta:
        model = UserSmallHolderEstates
        fields = '__all__'
        
class UserCooperativeSerializer(serializers.ModelSerializer): #has view
    class Meta:
        model = UserCooperative
        fields = '__all__'
      

class UserFieldOfficersSerializer(serializers.ModelSerializer):#has view
    class Meta:
        model = UserFieldOfficers
        fields = '__all__'
 

class UserFarmersSerializer(serializers.ModelSerializer):#has view
    class Meta:
        # cooperative = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        # factory = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        # permission = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        model = UserFarmers
        fields = '__all__'
        

class FarmsSerializer(serializers.ModelSerializer):#has view
    class Meta:
        model = Farms
        fields = '__all__'
    

class DevicesSerializer(serializers.ModelSerializer):#has view
    class Meta:
        model = Devices
        fields = '__all__'
     

class FarmersTransactionsSerializer(serializers.ModelSerializer):#has view
    class Meta:
        model = FarmersTransactions
        fields = '__all__'
        

class SmallHolderEstateTransactionsSerializer(serializers.ModelSerializer):#has view
    class Meta:
        model = FarmersTransactions
        fields = '__all__'
    

class FarmerIncomeSourceSerializer(serializers.ModelSerializer):#has view
    class Meta:
        model = FarmerIncomeSource
        fields = '__all__'
     

class FarmerDebtsSerializer(serializers.ModelSerializer):#has view
    class Meta:
        model = FarmerDebts
        fields = '__all__'

class SmallHolderEstateIncomeSourceSerializer(serializers.ModelSerializer):#has view
    class Meta:
        model = SmallHolderEstateIncomeSource
        fields = '__all__'
  

class SmallHolderEstateDebtsSerializer(serializers.ModelSerializer):#has view
    class Meta:
        model = SmallHolderEstateDebts
        fields = '__all__'
     

class FarmInputsSerializer(serializers.ModelSerializer):#has view
    class Meta:
        model = FarmInputs
        fields = '__all__'
        

class FarmerInputRequestSerializer(serializers.ModelSerializer):#has view
    class Meta:
        model = FarmerInputRequest
        fields = '__all__'
       

class SmallHolderEstateInputRequestSerializer(serializers.ModelSerializer):#has view
    class Meta:
        model = SmallHolderEstateInputRequest
        fields = '__all__'
      

############################# KILOSAHIHI END #############################################
