from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.db.models import Sum
from rest_framework.decorators import authentication_classes, permission_classes
from .models import *
from kilosahihi.serializers import *
from rest_framework.decorators import api_view
from .filters import UserFarmersFilter
from django.core.paginator import Paginator

import datetime
import csv



def home(request):
    # get
    farmers = UserFarmers.objects.all()
    allfarmers = UserFarmers.objects.all()[0:5]
    variety = ProduceVariety.objects.all()
    inputrequest = FarmerInputRequest.objects.all()

    # count
    total_farmers = farmers.count()
    total_variety = variety.count()
    total_input = inputrequest.count()

    # display
    context = {'allfarmers' :allfarmers, 'total_farmers':total_farmers, 'total_variety':total_variety, 'total_input':total_input}

    # render
    return render(request, "kilosahihi/index.html", context)

def farmers(request):
    # get
    farmers = UserFarmers.objects.all()
    allfarmers = UserFarmers.objects.all()
    variety = ProduceVariety.objects.all()
    inputrequest = FarmerInputRequest.objects.all()

    # Paginator
    p = Paginator(UserFarmers.objects.all(), 10)
    page = request.GET.get('page')
    farmers_number = p.get_page(page)

    # count
    total_farmers = farmers.count()
    total_variety = variety.count()
    total_input = inputrequest.count()

    # filters
    myFilter = UserFarmersFilter(request.GET, queryset=allfarmers)
    allfarmers = myFilter.qs

    # display
    context = {'farmers_number':farmers_number, 'allfarmers' :allfarmers, 'total_farmers':total_farmers, 'total_variety':total_variety, 'total_input':total_input, 'myFilter': myFilter}

    # render
    return render(request, "kilosahihi/farmers.html", context)


def print_farmers(request):
    
    response = HTTPResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=Farmers' + \
        str(datetime.datetime.now())+'.pdf'



 ################################### KILOSAHIHI  ################################### 

 ###################################              USERS              ############################### 

@api_view(['GET', 'POST', 'DELETE'])

def users_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
           users = users.filter(name__icontains=name)
        
        users_serializer = UsersViewSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        users_data = JSONParser().parse(request)
        users_serializer = UsersViewSerializer(data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse(users_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #elif request.method == 'DELETE':
    #   count = User.objects.all().delete()
    #   return JsonResponse({'message': '{} Users were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def users_detail(request, pk):
    try: 
        users = User.objects.get(pk=pk) 
    except User.DoesNotExist: 
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        users_serializer = UsersViewSerializer(users) 
        return JsonResponse(users_serializer.data) 
 
    elif request.method == 'PUT': 
        users_data = JSONParser().parse(request) 
        users_serializer = UsersViewSerializer(users, data=users_data)
        if users_serializer.is_valid(): 
            users_serializer.save() 
            return JsonResponse(users_serializer.data) 
        return JsonResponse(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        users.delete() 
        return JsonResponse({'message': 'Users was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
      
@api_view(['GET'])

def users_list_active(request):
    users = User.objects.filter(status="Active")
        
    if request.method == 'GET': 
        users_serializer = UsersViewSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)


 ###################################               USERS              ############################### 

  ###################################              USER ROLES             ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def userroles_list(request):
    if request.method == 'GET':
        userroles = UserRoles.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
           userroles = UserRoles.filter(name__icontains=name)
        
        userroles_serializer = UserRolesSerializer(userroles, many=True)
        return JsonResponse(userroles_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        userroles_data = JSONParser().parse(request)
        userroles_serializer = UserRolesSerializer(data=userroles_data)
        if userroles_serializer.is_valid():
            userroles_serializer.save()
            return JsonResponse(userroles_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(userroles_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = UserRoles.objects.all().delete()
        return JsonResponse({'message': '{} User roles were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def userroles_detail(request, pk):
    try: 
        userroles = UserRoles.objects.get(pk=pk) 
    except UserRoles.DoesNotExist: 
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        userroles_serializer = UserRolesSerializer(userroles) 
        return JsonResponse(userroles_serializer.data) 
 
    elif request.method == 'PUT': 
        userroles_data = JSONParser().parse(request) 
        userroles_serializer = UserRolesSerializer(userroles, data=userroles_data)
        if userroles_serializer.is_valid(): 
            userroles_serializer.save() 
            return JsonResponse(userroles_serializer.data) 
        return JsonResponse(userroles_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        userroles.delete() 
        return JsonResponse({'message': 'Users roles was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
      
@api_view(['GET'])

def userroles_list_active(request):
    userroles = UserRoles.objects.filter(status="Active")
        
    if request.method == 'GET': 
        userroles_serializer = UserRolesSerializer(userroles, many=True)
        return JsonResponse(userroles_serializer.data, safe=False)


 ###################################               USER ROLES             ############################### 

 ###################################              USERPERMISSIONS          ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def userpermissions_list(request):
    if request.method == 'GET':
        userpermissions = UserPermissions.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
           userpermissions = UserPermissions.filter(name__icontains=name)
        
        userpermissions_serializer = UserPermissionsSerializer(userpermissions, many=True)
        return JsonResponse(userpermissions_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        userpermissions_data = JSONParser().parse(request)
        userpermissions_serializer = UserPermissionsSerializer(data=userpermissions_data)
        if userpermissions_serializer.is_valid():
            userpermissions_serializer.save()
            return JsonResponse(userpermissions_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(userpermissions_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count =UserPermissions.objects.all().delete()
        return JsonResponse({'message': '{} User Permissions were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def userpermissions_detail(request, pk):
    try: 
        userpermissions =  UserPermissions.objects.get(pk=pk) 
    except userpermissions.DoesNotExist: 
        return JsonResponse({'message': 'The user permission does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        userpermissions_serializer = UserPermissionsSerializer(userpermissions) 
        return JsonResponse(userpermissions_serializer.data) 
 
    elif request.method == 'PUT': 
        userpermissions_data = JSONParser().parse(request) 
        userpermissions_serializer = UserPermissionsSerializer(userpermissions, data=userpermissions_data)
        if userpermissions_serializer.is_valid(): 
            userpermissions_serializer.save() 
            return JsonResponse(userpermissions_serializer.data) 
        return JsonResponse(userpermissions_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        userpermissions.delete() 
        return JsonResponse({'message': 'Users permissions was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
      
@api_view(['GET'])

def userpermissions_list_active(request):
    userpermissions = UserPermissions.objects.filter(status="Active")
        
    if request.method == 'GET': 
        userpermissions_serializer = UserPermissionsSerializer(userpermissions, many=True)
        return JsonResponse(userpermissions_serializer.data, safe=False)


 ###################################               USERPERMISSIONS            ############################### 

   ###################################              USER ATTRIBUTES             ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def userattributes_list(request):
    if request.method == 'GET':
        userattributes = UserAttributes.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
           userattributes = UserAttributes.filter(name__icontains=name)
        
        userattributes_serializer = UserAttributesSerializer(userattributes, many=True)
        return JsonResponse(userattributes_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        userattributes_data = JSONParser().parse(request)
        userattributes_serializer = UserAttributesSerializer(data=userattributes_data)
        if userattributes_serializer.is_valid():
            userattributes_serializer.save()
            return JsonResponse(userattributes_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(userattributes_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = UserAttributes.objects.all().delete()
        return JsonResponse({'message': '{} User Attributes were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def userattributes_detail(request, pk):
    try: 
        userattributes = UserAttributes.objects.get(pk=pk) 
    except UserAttributes.DoesNotExist: 
        return JsonResponse({'message': 'The user attribute does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        userattributes_serializer = UserAttributesSerializer(userattributes) 
        return JsonResponse(userattributes_serializer.data) 
 
    elif request.method == 'PUT': 
        userattributes_data = JSONParser().parse(request) 
        userattributes_serializer = UserRolesSerializer(userattributes, data=userattributes_data)
        if userattributes_serializer.is_valid(): 
            userattributes_serializer.save() 
            return JsonResponse(userattributes_serializer.data) 
        return JsonResponse(userattributes_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        userattributes.delete() 
        return JsonResponse({'message': 'Users attributes was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
      
@api_view(['GET'])

def userattributes_list_active(request):
    userattributes = UserAttributes.objects.filter(status="Active")
        
    if request.method == 'GET': 
        userattributes_serializer = UserRolesSerializer(userattributes, many=True)
        return JsonResponse(userattributes_serializer.data, safe=False)


 ###################################               USER ROLES             ############################### 

 ###################################              COOPERATIVES              ############################### 

@api_view(['GET', 'POST', 'DELETE'])
@authentication_classes([])
@permission_classes([])

def cooperatives_list(request):
    if request.method == 'GET':
        cooperatives = Cooperatives.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
           cooperatives = cooperatives.filter(name__icontains=name)
        
        cooperatives_serializer = CooperativesSerializer(cooperatives, many=True)
        return JsonResponse(cooperatives_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        cooperatives_data = JSONParser().parse(request)
        cooperatives_serializer = CooperativesSerializer(data=cooperatives_data)
        if cooperatives_serializer.is_valid():
            cooperatives_serializer.save()
            return JsonResponse(cooperatives_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(cooperatives_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Cooperatives.objects.all().delete()
        return JsonResponse({'message': '{} Cooperatives were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def cooperatives_detail(request, pk):
    try: 
        cooperatives = Cooperatives.objects.get(pk=pk) 
    except Cooperatives.DoesNotExist: 
        return JsonResponse({'message': 'The cooperative does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        cooperatives_serializer = CooperativesSerializer(cooperatives) 
        return JsonResponse(cooperatives_serializer.data) 
 
    elif request.method == 'PUT': 
        cooperatives_data = JSONParser().parse(request) 
        cooperatives_serializer = CooperativesSerializer(cooperatives, data=cooperatives_data)
        if cooperatives_serializer.is_valid(): 
            cooperatives_serializer.save() 
            return JsonResponse(cooperatives_serializer.data) 
        return JsonResponse(cooperatives_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        cooperatives.delete() 
        return JsonResponse({'message': 'Cooperative was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
      
@api_view(['GET'])

def cooperatives_list_active(request):
    cooperatives = Cooperatives.objects.filter(status="Active")
        
    if request.method == 'GET': 
        cooperatives_serializer = CooperativesSerializer(cooperatives, many=True)
        return JsonResponse(cooperatives_serializer.data, safe=False)


 ###################################               COOPERATIVES               ###############################

 ###################################             USER COOPERATIVES              ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def usercooperatives_list(request):
    if request.method == 'GET':
        usercooperatives = UserCooperative.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
           usercooperatives = usercooperatives.filter(name__icontains=name)
        
        usercooperatives_serializer = UserCooperativeSerializer(usercooperatives, many=True)
        return JsonResponse(usercooperatives_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        usercooperatives_data = JSONParser().parse(request)
        usercooperatives_serializer = UserCooperativeSerializer(data=usercooperatives_data)
        if usercooperatives_serializer.is_valid():
            usercooperatives_serializer.save()
            return JsonResponse(usercooperatives_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(usercooperatives_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = UserCooperative.objects.all().delete()
        return JsonResponse({'message': '{} Cooperative Users were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def usercooperatives_detail(request, pk):
    try: 
        usercooperatives = UserCooperative.objects.get(pk=pk) 
    except UserCooperative.DoesNotExist: 
        return JsonResponse({'message': 'The cooperative User does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        usercooperatives_serializer = UserCooperativeSerializer(usercooperatives) 
        return JsonResponse(usercooperatives_serializer.data) 
 
    elif request.method == 'PUT': 
        usercooperatives_data = JSONParser().parse(request) 
        usercooperatives_serializer = UserCooperativeSerializer(usercooperatives, data=usercooperatives_data)
        if usercooperatives_serializer.is_valid(): 
            usercooperatives_serializer.save() 
            return JsonResponse(usercooperatives_serializer.data) 
        return JsonResponse(usercooperatives_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        usercooperatives.delete() 
        return JsonResponse({'message': 'Cooperative user was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
      
@api_view(['GET'])

def usercooperatives_list_active(request):
    usercooperatives = UserCooperative.objects.filter(status="Active")
        
    if request.method == 'GET': 
        usercooperatives_serializer = UserCooperativeSerializer(usercooperatives, many=True)
        return JsonResponse(usercooperatives_serializer.data, safe=False)


 ###################################               COOPERATIVES               ###############################

  ###################################              AUDITS              ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def audits_list(request):
    if request.method == 'GET':
        audits = Audits.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
           audits = audits.filter(name__icontains=name)
        
        audits_serializer = AuditsViewSerializer(audits, many=True)
        return JsonResponse(audits_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        audits_data = JSONParser().parse(request)
        audits_serializer = AuditsViewSerializer(data=audits_data)
        if audits_serializer.is_valid():
            audits_serializer.save()
            return JsonResponse(audits_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(audits_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Audits.objects.all().delete()
        return JsonResponse({'message': '{} Audits were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def audits_detail(request, pk):
    try: 
        audits = Audits.objects.get(pk=pk) 
    except Audits.DoesNotExist: 
        return JsonResponse({'message': 'The audits does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        audits_serializer = AuditsViewSerializer(audits) 
        return JsonResponse(audits_serializer.data) 
 
    elif request.method == 'PUT': 
        audits_data = JSONParser().parse(request) 
        audits_serializer = AuditsViewSerializer(audits, data=audits_data)
        if audits_serializer.is_valid(): 
            audits_serializer.save() 
            return JsonResponse(audits_serializer.data) 
        return JsonResponse(audits_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        audits.delete() 
        return JsonResponse({'message': 'Audits was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
      
@api_view(['GET'])

def audits_list_active(request):
    audits = Audits.objects.filter(status="Active")
        
    if request.method == 'GET': 
        audits_serializer = AuditsViewSerializer(audits, many=True)
        return JsonResponse(audits_serializer.data, safe=False)


 ###################################               AUDITS              ############################### 


###################################              PRODUCE              ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def produce_list(request):
    if request.method == 'GET':
        produce = Produce.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
           produce = produce.filter(name__icontains=name)
        
        produce_serializer = ProduceSerializer(produce, many=True)
        return JsonResponse(produce_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        produce_data = JSONParser().parse(request)
        produce_serializer = ProduceSerializer(data=produce_data)
        if produce_serializer.is_valid():
            produce_serializer.save()
            return JsonResponse(produce_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(produce_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Produce.objects.all().delete()
        return JsonResponse({'message': '{} Produce were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def produce_detail(request, pk):
    try: 
        produce = Produce.objects.get(pk=pk) 
    except Produce.DoesNotExist: 
        return JsonResponse({'message': 'The produce does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        produce_serializer = ProduceSerializer(produce) 
        return JsonResponse(produce_serializer.data) 
 
    elif request.method == 'PUT': 
        produce_data = JSONParser().parse(request) 
        produce_serializer = ProduceSerializer(produce, data=produce_data)
        if produce_serializer.is_valid(): 
            produce_serializer.save() 
            return JsonResponse(produce_serializer.data) 
        return JsonResponse(produce_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        produce.delete() 
        return JsonResponse({'message': 'Produce was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
      
@api_view(['GET'])

def produce_list_active(request):
    sku = Produce.objects.filter(status="Active")
        
    if request.method == 'GET': 
        produce_serializer = ProduceSerializer(sku, many=True)
        return JsonResponse(produce_serializer.data, safe=False)


 ###################################               PRODUCE END               ############################### 

   ###################################              BANKS              ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def banks_list(request):
    if request.method == 'GET':
        banks = Banks.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
           banks = Banks.filter(name__icontains=name)
        
        banks_serializer = BanksSerializer(banks, many=True)
        return JsonResponse(banks_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        banks_data = JSONParser().parse(request)
        banks_serializer = BanksSerializer(data=banks_data)
        if banks_serializer.is_valid():
            banks_serializer.save()
            return JsonResponse(banks_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(banks_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Banks.objects.all().delete()
        return JsonResponse({'message': '{} Banks were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def banks_detail(request, pk):
    try: 
        banks = Banks.objects.get(pk=pk) 
    except Banks.DoesNotExist: 
        return JsonResponse({'message': 'The bank does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        banks_serializer = BanksSerializer(banks) 
        return JsonResponse(banks_serializer.data) 
 
    elif request.method == 'PUT': 
        banks_data = JSONParser().parse(request) 
        banks_serializer = BanksSerializer(banks, data=banks_data)
        if banks_serializer.is_valid(): 
            banks_serializer.save() 
            return JsonResponse(banks_serializer.data) 
        return JsonResponse(banks_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        banks.delete() 
        return JsonResponse({'message': 'Bank was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
      
@api_view(['GET'])

def banks_list_active(request):
    banks = Banks.objects.filter(status="Active")
        
    if request.method == 'GET': 
        banks_serializer = BanksSerializer(banks, many=True)
        return JsonResponse(banks_serializer.data, safe=False)


 ###################################               BANKS              ############################### 

   ###################################             USER BANK ACCOUNT              ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def userbankaccounts_list(request):
    if request.method == 'GET':
        userbankaccounts = UserBankAccounts.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
           userbankaccounts = UserBankAccounts.filter(name__icontains=name)
        
        userbankaccounts_serializer = UserBankAccountsSerializer(userbankaccounts, many=True)
        return JsonResponse(userbankaccounts_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        userbankaccounts_data = JSONParser().parse(request)
        userbankaccounts_serializer = UserBankAccountsSerializer(data=userbankaccounts_data)
        if userbankaccounts_serializer.is_valid():
            userbankaccounts_serializer.save()
            return JsonResponse(userbankaccounts_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(userbankaccounts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = UserBankAccounts.objects.all().delete()
        return JsonResponse({'message': '{} User Bank Accounts were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def userbankaccounts_detail(request, pk):
    try: 
        userbankaccounts = UserBankAccounts.objects.get(pk=pk) 
    except UserBankAccounts.DoesNotExist: 
        return JsonResponse({'message': 'The user bank account does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        userbankaccounts_serializer = UserBankAccountsSerializer(userbankaccounts) 
        return JsonResponse(userbankaccounts_serializer.data) 
 
    elif request.method == 'PUT': 
        userbankaccounts_data = JSONParser().parse(request) 
        userbanksaccounts_serializer = BanksSerializer(userbankaccounts, data=userbankaccounts_data)
        if userbanksaccounts_serializer.is_valid(): 
            userbanksaccounts_serializer.save() 
            return JsonResponse(userbanksaccounts_serializer.data) 
        return JsonResponse(userbanksaccounts_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        userbankaccounts_data.delete() 
        return JsonResponse({'message': 'User bank account was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
      
@api_view(['GET'])
def userbankaccounts_list_active(request):
    userbankaccounts = UserBankAccounts.objects.filter(status="Active")
        
    if request.method == 'GET': 
        userbankaccounts_serializer = UserBankAccountsSerializer(userbankaccounts, many=True)
        return JsonResponse(userbankaccounts_serializer.data, safe=False)


 ###################################               USER BANK ACCOUNTS              ###############################


   ###################################              UNIONS              ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def unions_list(request):
    if request.method == 'GET':
        unions = Unions.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
           unions = Unions.filter(name__icontains=name)
        
        unions_serializer = UnionsSerializer(unions, many=True)
        return JsonResponse(unions_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        unions_data = JSONParser().parse(request)
        unions_serializer = UnionsSerializer(data=unions_data)
        if unions_serializer.is_valid():
            unions_serializer.save()
            return JsonResponse(unions_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(unions_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Unions.objects.all().delete()
        return JsonResponse({'message': '{} Unions were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def unions_detail(request, pk):
    try: 
        unions = Unions.objects.get(pk=pk) 
    except Unions.DoesNotExist: 
        return JsonResponse({'message': 'The Union does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        unions_serializer = UnionsSerializer(unions) 
        return JsonResponse(unions_serializer.data) 
 
    elif request.method == 'PUT': 
        unions_data = JSONParser().parse(request) 
        unions_serializer = UnionsSerializer(unions, data=unions_data)
        if unions_serializer.is_valid(): 
            unions_serializer.save() 
            return JsonResponse(unions_serializer.data) 
        return JsonResponse(unions_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        unions.delete() 
        return JsonResponse({'message': 'Union was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
      
@api_view(['GET'])

def unions_list_active(request):
    unions = Unions.objects.filter(status="Active")
        
    if request.method == 'GET': 
        unions_serializer = UnionsSerializer(unions, many=True)
        return JsonResponse(unions_serializer.data, safe=False)


 ###################################                UNIONS              ############################### 
 
###################################               FACTORIES            ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def factories_list(request):
    if request.method == 'GET':
        factories = Factories.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
            factories = factories.filter(name__icontains=name)
        
        factories_serializer = FactoriesSerializer(factories, many=True)
        return JsonResponse(factories_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        factories_data = JSONParser().parse(request)
        factories_serializer = FactoriesSerializer(data=factories_data)
        if factories_serializer.is_valid():
            factories_serializer.save()
            return JsonResponse(factories_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(factories_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Factories.objects.all().delete()
        return JsonResponse({'message': '{} Factories were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def factories_detail(request, pk):
    try: 
        factories = Factories.objects.get(pk=pk) 
    except Factories.DoesNotExist: 
        return JsonResponse({'message': 'The factory does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        factories_serializer = FactoriesSerializer(factories) 
        return JsonResponse(factories_serializer.data) 
 
    elif request.method == 'PUT': 
        factories_data = JSONParser().parse(request) 
        factories_serializer = FactoriesSerializer(factories, data=factories_data) 
        if factories_serializer.is_valid(): 
            factories_serializer.save() 
            return JsonResponse(factories_serializer.data) 
        return JsonResponse(factories_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        factories.delete() 
        return JsonResponse({'message': 'Factory was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def factories_list_active(request):
    factories = Factories.objects.filter(published=True)
        
    if request.method == 'GET': 
        factories_serializer = FactoriesSerializer(factories, many=True)
        return JsonResponse(factories_serializer.data, safe=False)


###################################               DEVICES            ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def devices_list(request):
    if request.method == 'GET':
        devices = Devices.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
            devices = devices.filter(name__icontains=name)
        
        devices_serializer = DevicesSerializer(devices, many=True)
        return JsonResponse(devices_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        devices_data = JSONParser().parse(request)
        devices_serializer = DevicesSerializer(data=devices_data)
        if devices_serializer.is_valid():
            devices_serializer.save()
            return JsonResponse(devices_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(devices_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Devices.objects.all().delete()
        return JsonResponse({'message': '{} Devices were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def devices_detail(request, pk):
    try: 
        devices = Devices.objects.get(pk=pk) 
    except Devices.DoesNotExist: 
        return JsonResponse({'message': 'The device does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        devices_serializer = DevicesSerializer(devices) 
        return JsonResponse(devices_serializer.data) 
 
    elif request.method == 'PUT': 
        devices_data = JSONParser().parse(request) 
        devices_serializer = DevicesSerializer(devices, data=devices_data) 
        if devices_serializer.is_valid(): 
            devices_serializer.save() 
            return JsonResponse(devices_serializer.data) 
        return JsonResponse(devices_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        devices.delete() 
        return JsonResponse({'message': 'The device was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def devices_list_active(request):
    devices = Devices.objects.filter(published=True)
        
    if request.method == 'GET': 
        devices_serializer = DevicesSerializer(devices, many=True)
        return JsonResponse(devices_serializer.data, safe=False)


   ###################################              SMALL HOLDER ESTATES           ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def smallholderestates_list(request):
    if request.method == 'GET':
        smallholderestates = SmallHolderEstates.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
           smallholderestates = SmallHolderEstates.filter(name__icontains=name)
        
        smallholderestates_serializer = SmallHolderEstatesSerializer(smallholderestates, many=True)
        return JsonResponse(smallholderestates_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        smallholderestates_data = JSONParser().parse(request)
        smallerholderestates_serializer = SmallHolderEstatesSerializer(data=smallholderestates_data)
        if smallerholderestates_serializer.is_valid():
            smallerholderestates_serializer.save()
            return JsonResponse(smallerholderestates_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(smallerholderestates_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = SmallHolderEstates.objects.all().delete()
        return JsonResponse({'message': '{} Small Holder Estates were deleted successfully !'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def smallholderestates_detail(request, pk):
    try: 
        smallholderestates = SmallHolderEstates.objects.get(pk=pk) 
    except SmallHolderEstates.DoesNotExist: 
        return JsonResponse({'message': 'The Small Holder Estates does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        smallholderestates_serializer = SmallHolderEstatesSerializer(smallholderestates) 
        return JsonResponse(smallholderestates_serializer.data) 
 
    elif request.method == 'PUT': 
        smallholderestates_data = JSONParser().parse(request) 
        smallholderestates_serializer = SmallHolderEstatesSerializer(smallholderestates, data=smallholderestates_data)
        if smallholderestates_serializer.is_valid(): 
            smallholderestates_serializer.save() 
            return JsonResponse(smallholderestates_serializer.data) 
        return JsonResponse(smallholderestates_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        smallholderestates.delete() 
        return JsonResponse({'message': 'Small Holder Estate was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
      
@api_view(['GET'])

def smallholderestates_list_active(request):
    smallholderestate = SmallHolderEstates.objects.filter(status="Active")
        
    if request.method == 'GET': 
        smallholderestates_serializer = SmallHolderEstatesSerializer(smallholderestate, many=True)
        return JsonResponse(smallholderestates_serializer.data, safe=False)


 ###################################                SMALL HOLDER ESTATES              ############################### 

   ###################################              SMALL HOLDER ESTATES USER           ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def usersmallholderestates_list(request):
    if request.method == 'GET':
        usersmallholderestates = UserSmallHolderEstates.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
           usersmallholderestates = UserSmallHolderEstates.filter(name__icontains=name)
        
        usersmallholderestates_serializer = UserSmallHolderEstatesSerializer(usersmallholderestates, many=True)
        return JsonResponse(usersmallholderestates_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        usersmallholderestates_data = JSONParser().parse(request)
        usersmallerholderestates_serializer = UserSmallHolderEstatesSerializer(data=usersmallholderestates_data)
        if usersmallerholderestates_serializer.is_valid():
            usersmallerholderestates_serializer.save()
            return JsonResponse(usersmallerholderestates_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(usersmallerholderestates_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = UserSmallHolderEstates.objects.all().delete()
        return JsonResponse({'message': '{} User Small Holder Estates were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def usersmallholderestates_detail(request, pk):
    try: 
        usersmallholderestates = UserSmallHolderEstates.objects.get(pk=pk) 
    except UserSmallHolderEstates.DoesNotExist: 
        return JsonResponse({'message': 'The Small Holder Estates User does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        usersmallholderestates_serializer = SmallHolderEstates(usersmallholderestates) 
        return JsonResponse(usersmallholderestates_serializer.data) 
 
    elif request.method == 'PUT': 
        usersmallholderestates_data = JSONParser().parse(request) 
        usersmallholderestates_serializer = UserSmallHolderEstatesSerializer(usersmallholderestates, data=usersmallholderestates_data)
        if usersmallholderestates_serializer.is_valid(): 
            usersmallholderestates_serializer.save() 
            return JsonResponse(usersmallholderestates_serializer.data) 
        return JsonResponse(usersmallholderestates_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        usersmallholderestates.delete() 
        return JsonResponse({'message': 'Small Holder Estate User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
      
@api_view(['GET'])
def usersmallholderestates_list_active(request):
    usersmallholderestate = UserSmallHolderEstates.objects.filter(status="Active")
        
    if request.method == 'GET': 
        usersmallholderestates_serializer = UserSmallHolderEstatesSerializer(usersmallholderestate, many=True)
        return JsonResponse(usersmallholderestates_serializer.data, safe=False)


 ###################################                USER SMALLHOLDER ESTATES              ############################### 

 ###################################              SMALL HOLDER ESTATES           ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def smallholderestatestransactions_list(request):
    if request.method == 'GET':
        smallholderestatestransactions = smallholderestatestransactions.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
           smallholderestatestransactions = smallholderestatestransactions.filter(name__icontains=name)
        
        smallholderestatestransactions_serializer = SmallHolderEstateTransactionsSerializer(smallholderestatestransactions, many=True)
        return JsonResponse(smallholderestatestransactions_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        smallholderestatestransactions_data = JSONParser().parse(request)
        smallerholderestatestransactions_serializer = SmallHolderEstateTransactionsSerializer(data=smallholderestatestransactions_data)
        if smallerholderestatestransactions_serializer.is_valid():
            smallerholderestatestransactions_serializer.save()
            return JsonResponse(smallerholderestatestransactions_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(smallerholderestatestransactions_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = SmallHolderEstateTransactions.objects.all().delete()
        return JsonResponse({'message': '{} Small Holder Estates Transactions were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def smallholderestatestransactions_detail(request, pk):
    try: 
        smallholderestatestransactions = SmallHolderEstateTransactions.objects.get(pk=pk) 
    except SmallHolderEstateTransactions.DoesNotExist: 
        return JsonResponse({'message': 'The Small Holder Estates Transactionns does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        smallholderestatestransactions_serializer = SmallHolderEstateTransactionsSerializer(smallholderestatestransactions) 
        return JsonResponse(smallholderestatestransactions_serializer.data) 
 
    elif request.method == 'PUT': 
        smallholderestatestransactions_data = JSONParser().parse(request) 
        smallholderestatestransactions_serializer = SmallHolderEstateTransactionsSerializer(smallholderestatestransactions, data=smallholderestatestransactions_data)
        if smallholderestatestransactions_serializer.is_valid(): 
            smallholderestatestransactions_serializer.save() 
            return JsonResponse(smallholderestatestransactions_serializer.data) 
        return JsonResponse(smallholderestatestransactions_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        smallholderestatestransactions.delete() 
        return JsonResponse({'message': 'Small Holder Estate Transaction was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
      
@api_view(['GET'])

def smallholderestatestransactions_list_active(request):
    smallholderestatetransactions = SmallHolderEstateTransactions.objects.filter(status="Active")
        
    if request.method == 'GET': 
        smallholderestatestransactions_serializer = SmallHolderEstateTransactionsSerializer(smallholderestatetransactions, many=True)
        return JsonResponse(smallholderestatestransactions_serializer.data, safe=False)


 ###################################                SMALL HOLDER ESTATES              ############################### 
 ###################################              SMALL HOLDER ESTATES INCOME SOURCE           ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def smallholderestateincomesource_list(request):
    if request.method == 'GET':
        smallholderestateincomesource = SmallHolderEstateIncomeSource.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
           smallholderestateincomesource = SmallHolderEstateIncomeSource.filter(name__icontains=name)
        
        smallholderestateincomesource_serializer = SmallHolderEstateIncomeSourceSerializer(smallholderestateincomesource, many=True)
        return JsonResponse(smallholderestateincomesource_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        smallholderestateincomesource_data = JSONParser().parse(request)
        smallerholderestateincomesource_serializer = SmallHolderEstateIncomeSourceSerializer(data=smallholderestateincomesource_data)
        if smallerholderestateincomesource_serializer.is_valid():
            smallerholderestateincomesource_serializer.save()
            return JsonResponse(smallerholderestateincomesource_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(smallerholderestateincomesource_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = SmallHolderEstateIncomeSource.objects.all().delete()
        return JsonResponse({'message': '{} Small Holder Estates were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def smallholderestateincomesource_detail(request, pk):
    try: 
        smallholderestateincomesource = SmallHolderEstateIncomeSource.objects.get(pk=pk) 
    except SmallHolderEstateIncomeSource.DoesNotExist: 
        return JsonResponse({'message': 'The Small Holder Estates Income Source does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        smallholderestateincomesource_serializer = SmallHolderEstateIncomeSourceSerializer(smallholderestateincomesource) 
        return JsonResponse(smallholderestateincomesource_serializer.data) 
 
    elif request.method == 'PUT': 
        smallholderestateincomesource_data = JSONParser().parse(request) 
        smallholderestateincomesource_serializer = SmallHolderEstateIncomeSourceSerializer(smallholderestateincomesource, data=smallholderestateincomesource_data)
        if smallholderestateincomesource_serializer.is_valid(): 
            smallholderestateincomesource_serializer.save() 
            return JsonResponse(smallholderestateincomesource_serializer.data) 
        return JsonResponse(smallholderestateincomesource_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        smallholderestateincomesource.delete() 
        return JsonResponse({'message': 'Small Holder Estate Income Source was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
      
@api_view(['GET'])
def smallholderestateincomesource_list_active(request):
    smallholderestateincomesource = SmallHolderEstateIncomeSource.objects.filter(status="Active")
        
    if request.method == 'GET': 
        smallholderestateincomesource_serializer = SmallHolderEstateIncomeSourceSerializer(smallholderestateincomesource, many=True)
        return JsonResponse(smallholderestateincomesource_serializer.data, safe=False)


 ###################################                SMALL HOLDER ESTATES INCOME SOURCE             ############################### 
  
     ###################################              SMALL HOLDER ESTATES DEBTS          ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def smallholderestates_list(request):
    if request.method == 'GET':
        smallholderestates = SmallHolderEstates.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
           smallholderestates = SmallHolderEstates.filter(name__icontains=name)
        
        smallholderestates_serializer = SmallHolderEstatesSerializer(smallholderestates, many=True)
        return JsonResponse(smallholderestates_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        smallholderestates_data = JSONParser().parse(request)
        smallerholderestates_serializer = SmallHolderEstatesSerializer(data=smallholderestates_data)
        if smallerholderestates_serializer.is_valid():
            smallerholderestates_serializer.save()
            return JsonResponse(smallerholderestates_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(smallerholderestates_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = SmallHolderEstates.objects.all().delete()
        return JsonResponse({'message': '{} Small Holder Estates were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def smallholderestates_detail(request, pk):
    try: 
        smallholderestates = SmallHolderEstates.objects.get(pk=pk) 
    except SmallHolderEstates.DoesNotExist: 
        return JsonResponse({'message': 'The Small Holder Estates does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        smallholderestates_serializer = SmallHolderEstatesSerializer(smallholderestates) 
        return JsonResponse(smallholderestates_serializer.data) 
 
    elif request.method == 'PUT': 
        smallholderestates_data = JSONParser().parse(request) 
        smallholderestates_serializer = SmallHolderEstatesSerializer(smallholderestates, data=smallholderestates_data)
        if smallholderestates_serializer.is_valid(): 
            smallholderestates_serializer.save() 
            return JsonResponse(smallholderestates_serializer.data) 
        return JsonResponse(smallholderestates_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        smallholderestates.delete() 
        return JsonResponse({'message': 'Small Holder Estate was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
      
@api_view(['GET'])

def smallholderestates_list_active(request):
    smallholderestate = SmallHolderEstates.objects.filter(status="Active")
        
    if request.method == 'GET': 
        smallholderestates_serializer = SmallHolderEstatesSerializer(smallholderestate, many=True)
        return JsonResponse(smallholderestates_serializer.data, safe=False)


 ###################################                SMALL HOLDER ESTATES              ############################### 

     ###################################              SMALL HOLDER ESTATES INPUT REQUEST        ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def smallholderestateinputrequest_list(request):
    if request.method == 'GET':
        smallholderestatesinputrequest = SmallHolderEstateInputRequest.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
           smallholderestatesinputrequest = SmallHolderEstateInputRequest.filter(name__icontains=name)
        
        smallholderestateinputrequest_serializer = SmallHolderEstateInputRequestSerializer(smallholderestatesinputrequest, many=True)
        return JsonResponse(smallholderestateinputrequest_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        smallholderestateinputrequest_data = JSONParser().parse(request)
        smallerholderestateinputrequest_serializer = SmallHolderEstateInputRequestSerializer(data=smallholderestateinputrequest_data)
        if smallerholderestateinputrequest_serializer.is_valid():
            smallerholderestateinputrequest_serializer.save()
            return JsonResponse(smallerholderestateinputrequest_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(smallerholderestateinputrequest_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = SmallHolderEstateInputRequest.objects.all().delete()
        return JsonResponse({'message': '{} Small Holder Estates Input Request were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def smallholderestateinputrequest_detail(request, pk):
    try: 
        smallholderestateinputrequest= SmallHolderEstateInputRequest.objects.get(pk=pk) 
    except SmallHolderEstateInputRequest.DoesNotExist: 
        return JsonResponse({'message': 'The Small Holder Estate Input Request does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        smallholderestateinputrequest_serializer = SmallHolderEstateInputRequestSerializer(smallholderestateinputrequest) 
        return JsonResponse(smallholderestateinputrequest_serializer.data) 
 
    elif request.method == 'PUT': 
        smallholderestateinputrequest_data = JSONParser().parse(request) 
        smallholderestateinputrequest_serializer = SmallHolderEstateInputRequestSerializer(smallholderestateinputrequest, data=smallholderestateinputrequest_data)
        if smallholderestateinputrequest_serializer.is_valid(): 
            smallholderestateinputrequest_serializer.save() 
            return JsonResponse(smallholderestateinputrequest_serializer.data) 
        return JsonResponse(smallholderestateinputrequest_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        smallholderestateinputrequest.delete() 
        return JsonResponse({'message': 'Small Holder Estate Input Request was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
      
@api_view(['GET'])

def smallholderestateinputrequest_list_active(request):
    smallholderestateinputrequest = SmallHolderEstateInputRequest.objects.filter(status="Active")
        
    if request.method == 'GET': 
        smallholderestateinputrequest_serializer = SmallHolderEstateInputRequestSerializer(smallholderestateinputrequest, many=True)
        return JsonResponse(smallholderestateinputrequest_serializer.data, safe=False)


 ###################################                SMALL HOLDER ESTATES INPUT REQUEST             ############################### 
    ###################################              SMALL HOLDER ESTATES           ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def smallholderestatedebts_list(request):
    if request.method == 'GET':
        smallholderestatedebts = SmallHolderEstateDebts.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
           smallholderestatedebts = SmallHolderEstateDebts.filter(name__icontains=name)
        
        smallholderestatedebts_serializer = SmallHolderEstateDebtsSerializer(smallholderestatedebts, many=True)
        return JsonResponse(smallholderestatedebts_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        smallholderestatedebts_data = JSONParser().parse(request)
        smallerholderestatedebts_serializer = SmallHolderEstateDebtsSerializer(data=smallholderestatedebts_data)
        if smallerholderestatedebts_serializer.is_valid():
            smallerholderestatedebts_serializer.save()
            return JsonResponse(smallerholderestatedebts_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(smallerholderestatedebts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = SmallHolderEstateDebts.objects.all().delete()
        return JsonResponse({'message': '{} Small Holder Estates Debts were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def smallholderestatedebts_detail(request, pk):
    try: 
        smallholderestatedebts = SmallHolderEstateDebts.objects.get(pk=pk) 
    except SmallHolderEstateDebts.DoesNotExist: 
        return JsonResponse({'message': 'The Small Holder Estates Debts does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        smallholderestatedebts_serializer = SmallHolderEstateDebtsSerializer(smallholderestatedebts) 
        return JsonResponse(smallholderestatedebts_serializer.data) 
 
    elif request.method == 'PUT': 
        smallholderestatedebts_data = JSONParser().parse(request) 
        smallholderestatedebts_serializer = SmallHolderEstateDebtsSerializer(smallholderestatedebts, data=smallholderestatedebts_data)
        if smallholderestatedebts_serializer.is_valid(): 
            smallholderestatedebts_serializer.save() 
            return JsonResponse(smallholderestatedebts_serializer.data) 
        return JsonResponse(smallholderestatedebts_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        smallholderestatedebts.delete() 
        return JsonResponse({'message': 'Small Holder Estate debt was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
      
@api_view(['GET'])
def smallholderestatedebts_list_active(request):
    smallholderestatedebts = SmallHolderEstateDebts.objects.filter(status="Active")
        
    if request.method == 'GET': 
        smallholderestatedebts_serializer = SmallHolderEstateDebtsSerializer(smallholderestatedebts, many=True)
        return JsonResponse(smallholderestatedebts_serializer.data, safe=False)


 ###################################                SMALL HOLDER DEBTS ESTATES              ############################### 
  
   ###################################              USER UNIONS              ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def userunions_list(request):
    if request.method == 'GET':
        userunions = UserUnions.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
           userunions = UserUnions.filter(name__icontains=name)
        
        userunions_serializer = UserUnionsSerializer(userunions, many=True)
        return JsonResponse(userunions_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        userunions_data = JSONParser().parse(request)
        userunions_serializer = UserUnionsSerializer(data=userunions_data)
        if userunions_serializer.is_valid():
            userunions_serializer.save()
            return JsonResponse(userunions_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(userunions_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = UserUnions.objects.all().delete()
        return JsonResponse({'message': '{} Union Users were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def userunions_detail(request, pk):
    try: 
        userunions = UserUnions.objects.get(pk=pk) 
    except UserUnions.DoesNotExist: 
        return JsonResponse({'message': 'The Union User does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        userunions_serializer = UserUnionsSerializer(userunions) 
        return JsonResponse(userunions_serializer.data) 
 
    elif request.method == 'PUT': 
        userunions_data = JSONParser().parse(request) 
        userunions_serializer = UserUnionsSerializer(userunions, data=userunions_data)
        if userunions_serializer.is_valid(): 
            userunions_serializer.save() 
            return JsonResponse(userunions_serializer.data) 
        return JsonResponse(userunions_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        userunions.delete() 
        return JsonResponse({'message': 'User Union was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
      
@api_view(['GET'])

def userunions_list_active(request):
    userunions = UserUnions.objects.filter(status="Active")
        
    if request.method == 'GET': 
        userunions_serializer = UserUnionsSerializer(userunions, many=True)
        return JsonResponse(userunions_serializer.data, safe=False)


 ###################################                UNIONS              ############################### 


###################################               USER FIELD OFFICER            ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def userfieldofficers_list(request):
    if request.method == 'GET':
        userfieldofficers = UserFieldOfficers.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
            userfieldofficers = UserFieldOfficers.filter(name__icontains=name)
        
        userfieldofficers_serializer = UserFieldOfficersSerializer(userfieldofficers, many=True)
        return JsonResponse(userfieldofficers_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        userfieldofficers_data = JSONParser().parse(request)
        userfieldofficers_serializer = UserFieldOfficersSerializer(data=userfieldofficers_data)
        if userfieldofficers_serializer.is_valid():
            userfieldofficers_serializer.save()
            return JsonResponse(userfieldofficers_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(userfieldofficers_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = UserFieldOfficers.objects.all().delete()
        return JsonResponse({'message': '{} Field Officers were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def userfieldofficers_detail(request, pk):
    try: 
        userfieldofficers = UserFieldOfficers.objects.get(pk=pk) 
    except UserFieldOfficers.DoesNotExist: 
        return JsonResponse({'message': 'The Field officer does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        userfieldofficers_serializer = UserFieldOfficersSerializer(userfieldofficers) 
        return JsonResponse(userfieldofficers_serializer.data) 
 
    elif request.method == 'PUT': 
        userfieldofficers_data = JSONParser().parse(request) 
        userfieldofficers_serializer = UserFieldOfficersSerializer(userfieldofficers, data=userfieldofficers_data) 
        if userfieldofficers_serializer.is_valid(): 
            userfieldofficers_serializer.save() 
            return JsonResponse(userfieldofficers_serializer.data) 
        return JsonResponse(userfieldofficers_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        userfieldofficers_serializer.delete() 
        return JsonResponse({'message': 'The field officer was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def userfieldofficers_list_active(request):
    userfieldofficers = UserFieldOfficers.objects.filter(published=True)
        
    if request.method == 'GET': 
        userfieldofficers_serializer = UserFieldOfficersSerializer(userfieldofficers, many=True)
        return JsonResponse(userfieldofficers_serializer.data, safe=False)


###################################               USER FIELD OFFICERS          ###############################  


###################################               USER FARMER            ############################### 

@api_view(['GET', 'POST', 'DELETE'])
@authentication_classes([])
@permission_classes([])

def userfarmers_list(request):
    if request.method == 'GET':
        userfarmers = UserFarmers.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
            userfarmers = userfarmers.filter(name__icontains=name)
        
        userfarmers_serializer = UserFarmersSerializer(userfarmers, many=True)
        return JsonResponse(userfarmers_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        userfarmers_data = JSONParser().parse(request)
        userfarmers_serializer = UserFarmersSerializer(data=userfarmers_data)
        if userfarmers_serializer.is_valid():
            userfarmers_serializer.save()
            return JsonResponse(userfarmers_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(userfarmers_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = UserFarmers.objects.all().delete()
        return JsonResponse({'message': '{} Farmers were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([])
@permission_classes([])

def userfarmers_detail(request, pk):
    try: 
        userfarmers = UserFarmers.objects.get(pk=pk) 
    except UserFarmers.DoesNotExist: 
        return JsonResponse({'message': 'The farmer does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        userfarmers_serializer = UserFarmersSerializer(userfarmers) 
        return JsonResponse(userfarmers_serializer.data) 
 
    elif request.method == 'PUT': 
        farmers_data = JSONParser().parse(request) 
        userfarmers_serializer = UserFarmersSerializer(userfarmers, data=farmers_data) 
        if userfarmers_serializer.is_valid(): 
            userfarmers_serializer.save() 
            return JsonResponse(userfarmers_serializer.data) 
        return JsonResponse(userfarmers_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        userfarmers.delete() 
        return JsonResponse({'message': 'The farmer was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def userfarmers_list_active(request):
    userfarmers = UserFarmers.objects.filter(published=True)
        
    if request.method == 'GET': 
        userfarmers_serializer = UserFarmersSerializer(userfarmers, many=True)
        return JsonResponse(userfarmers_serializer.data, safe=False)

@api_view(['GET'])
def userfarmers_username(request,username):
    userfarmers = UserFarmers.objects.filter(username=username)
        
    if request.method == 'GET': 
        userfarmers_serializer = UserFarmersSerializer(userfarmers, many=True)
        return JsonResponse(userfarmers_serializer.data, safe=False)

###################################               FARMS           ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def farms_list(request):
    if request.method == 'GET':
        farms = Farms.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
            farms = Farms.filter(name__icontains=name)
        
        farms_serializer = FarmsSerializer(farms, many=True)
        return JsonResponse(farms_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        farms_data = JSONParser().parse(request)
        farms_serializer = FarmsSerializer(data=farms_data)
        if farms_serializer.is_valid():
            farms_serializer.save()
            return JsonResponse(farms_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(farms_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Farms.objects.all().delete()
        return JsonResponse({'message': '{} Farms were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def farms_detail(request, pk):
    try: 
        farms = Farms.objects.get(pk=pk) 
    except Farms.DoesNotExist: 
        return JsonResponse({'message': 'The farm does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        farms_serializer = FarmsSerializer(farms) 
        return JsonResponse(farms_serializer.data) 
 
    elif request.method == 'PUT': 
        farms_data = JSONParser().parse(request) 
        farms_serializer = FarmsSerializer(farms, data=farms_data) 
        if farms_serializer.is_valid(): 
            farms_serializer.save() 
            return JsonResponse(farms_serializer.data) 
        return JsonResponse(farms_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        farms.delete() 
        return JsonResponse({'message': 'The Farm was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def farms_list_active(request):
    farms = Farms.objects.filter(published=True)
        
    if request.method == 'GET': 
        farms_serializer = FarmsSerializer(farms, many=True)
        return JsonResponse(farms_serializer.data, safe=False)


###################################               FARMERS TRANSACTIONS            ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def farmerstransactions_list(request):
    if request.method == 'GET':
        farmerstransactions = FarmersTransactions.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
            farmerstransactions = farmerstransactions.filter(name__icontains=name)
        
        farmerstransactions_serializer = FarmersTransactionsSerializer(farmerstransactions, many=True)
        return JsonResponse(farmerstransactions_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        farmerstransactions_data = JSONParser().parse(request)
        farmerstransactions_serializer = FarmersTransactionsSerializer(data=farmerstransactions_data)
        if farmerstransactions_serializer.is_valid():
            farmerstransactions_serializer.save()
            return JsonResponse(farmerstransactions_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(farmerstransactions_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = FarmersTransactions.objects.all().delete()
        return JsonResponse({'message': '{} Transactions were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def farmerstransactions_detail(request, pk):
    try: 
        farmerstransactions = FarmersTransactions.objects.get(pk=pk) 
    except FarmersTransactions.DoesNotExist: 
        return JsonResponse({'message': 'The transaction does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        farmerstransactions_serializer = FarmersTransactionsSerializer(farmerstransactions) 
        return JsonResponse(farmerstransactions_serializer.data) 
 
    elif request.method == 'PUT': 
        farmerstransactions_data = JSONParser().parse(request) 
        farmerstransactions_serializer = FarmersTransactionsSerializer(farmerstransactions, data=farmerstransactions_data) 
        if farmerstransactions_serializer.is_valid(): 
            farmerstransactions_serializer.save() 
            return JsonResponse(farmerstransactions_serializer.data) 
        return JsonResponse(farmerstransactions_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        farmerstransactions.delete() 
        return JsonResponse({'message': 'The transaction was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def farmerstransactions_list_active(request):
    farmerstransactions = FarmersTransactions.objects.filter(published=True)
        
    if request.method == 'GET': 
        farmerstransactions_serializer = FarmersTransactionsSerializer(farmerstransactions, many=True)
        return JsonResponse(farmerstransactions_serializer.data, safe=False)


###################################               FARMER DEBTS          ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def farmerdebts_list(request):
    if request.method == 'GET':
        farmerdebts = FarmerDebts.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
            farmerdebts = FarmerDebts.filter(name__icontains=name)
        
        farmerdebts_serializer = FarmerDebtsSerializer(farmerdebts, many=True)
        return JsonResponse(farmerdebts_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        farmerdebts_data = JSONParser().parse(request)
        farmerdebts_serializer = FarmerDebtsSerializer(data=farmerdebts_data)
        if farmerdebts_serializer.is_valid():
            farmerdebts_serializer.save()
            return JsonResponse(farmerdebts_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(farmerdebts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = FarmerDebts.objects.all().delete()
        return JsonResponse({'message': '{} Farmer Debts were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def farmerdebts_detail(request, pk):
    try: 
        farmerdebts= FarmerDebts.objects.get(pk=pk) 
    except FarmerDebts.DoesNotExist: 
        return JsonResponse({'message': 'The farmer debt does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        farmerdebts_serializer = FarmerDebtsSerializer(farmerdebts) 
        return JsonResponse(farmerdebts_serializer.data) 
 
    elif request.method == 'PUT': 
        farmerdebts_data = JSONParser().parse(request) 
        farmerdebts_serializer = FarmerDebtsSerializer(farmerdebts, data=farmerdebts_data) 
        if farmerdebts_serializer.is_valid(): 
            farmerdebts_serializer.save() 
            return JsonResponse(farmerdebts_serializer.data) 
        return JsonResponse(farmerdebts_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        farmerdebts.delete() 
        return JsonResponse({'message': 'The Farmer debt was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def farmerdebts_list_active(request):
    farmerdebts = FarmerDebts.objects.filter(published=True)
        
    if request.method == 'GET': 
        farmerdebts_serializer = FarmerDebtsSerializer(farmerdebts, many=True)
        return JsonResponse(farmerdebts_serializer.data, safe=False)

###################################               FARMS  INPUTS          ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def farminputs_list(request):
    if request.method == 'GET':
        farminputs = FarmInputs.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
            farminputs = FarmInputs.filter(name__icontains=name)
        
        farminputs_serializer = FarmInputsSerializer(farminputs, many=True)
        return JsonResponse(farminputs_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        farminputs_data = JSONParser().parse(request)
        farminputs_serializer = FarmInputsSerializer(data=farminputs_data)
        if farminputs_serializer.is_valid():
            farminputs_serializer.save()
            return JsonResponse(farminputs_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(farminputs_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = FarmInputs.objects.all().delete()
        return JsonResponse({'message': '{} Farms Inputs were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def farminputs_detail(request, pk):
    try: 
        farminputs = FarmInputs.objects.get(pk=pk) 
    except FarmInputs.DoesNotExist: 
        return JsonResponse({'message': 'The farm input does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        farminputs_serializer = FarmInputsSerializer(farminputs) 
        return JsonResponse(farminputs_serializer.data) 
 
    elif request.method == 'PUT': 
        farminputs_data = JSONParser().parse(request) 
        farminputs_serializer = FarmInputsSerializer(farminputs, data=farminputs_data) 
        if farminputs_serializer.is_valid(): 
            farminputs_serializer.save() 
            return JsonResponse(farminputs_serializer.data) 
        return JsonResponse(farminputs_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        farminputs.delete() 
        return JsonResponse({'message': 'The Farm Inputs was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def farminputs_list_active(request):
    farminputs = FarmInputs.objects.filter(published=True)
        
    if request.method == 'GET': 
        farminputs_serializer = FarmInputsSerializer(farminputs, many=True)
        return JsonResponse(farminputs_serializer.data, safe=False)

###################################               FARMS INCOME SOURCE          ############################### 


@api_view(['GET', 'POST', 'DELETE'])
def farmerincomesource_list(request):
    if request.method == 'GET':
        farmerincomesource = FarmerIncomeSource.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
            farmerincomesource = FarmerIncomeSource.filter(name__icontains=name)
        
        farmerincomesource_serializer = FarmerIncomeSourceSerializer(farmerincomesource, many=True)
        return JsonResponse(farmerincomesource_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        farmerincomesource_data = JSONParser().parse(request)
        farmerincomesource_serializer = FarmerIncomeSourceSerializer(data=farmerincomesource_data)
        if farmerincomesource_serializer.is_valid():
            farmerincomesource_serializer.save()
            return JsonResponse(farmerincomesource_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(farmerincomesource_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = FarmerIncomeSource.objects.all().delete()
        return JsonResponse({'message': '{} Farmer Income Sources were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def farmerincomesource_detail(request, pk):
    try: 
        farmerincomesource = FarmerIncomeSource.objects.get(pk=pk) 
    except FarmerIncomeSource.DoesNotExist: 
        return JsonResponse({'message': 'The farmer income source does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        farmerincomesource_serializer = FarmerIncomeSourceSerializer(farmerincomesource) 
        return JsonResponse(farmerincomesource_serializer.data) 
 
    elif request.method == 'PUT': 
        farmerincomesource_data = JSONParser().parse(request) 
        farmerincomesource_serializer = FarmerIncomeSourceSerializer(farmerincomesource,data=farmerincomesource_data) 
        if farmerincomesource_serializer.is_valid(): 
            farmerincomesource_serializer.save() 
            return JsonResponse(farmerincomesource_serializer.data) 
        return JsonResponse(farmerincomesource_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        farmerincomesource.delete() 
        return JsonResponse({'message': 'The Farm was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def farmerincomesource_list_active(request):
    farmerincomesource = FarmerIncomeSource.objects.filter(published=True)
        
    if request.method == 'GET': 
        farmerincomesource_serializer = FarmerIncomeSourceSerializer(farmerincomesource, many=True)
        return JsonResponse(farmerincomesource_serializer.data, safe=False)

###################################               PAYMENT            ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def payment_list(request):
    if request.method == 'GET':
        payment = Payment.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
            payment = payment.filter(name__icontains=name)
        
        payment_serializer = PaymentViewSerializer(payment, many=True)
        return JsonResponse(payment_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        payment_data = JSONParser().parse(request)
        payment_serializer = PaymentSerializer(data=payment_data)
        if payment_serializer.is_valid():
            payment_serializer.save()
            return JsonResponse(payment_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(payment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Payment.objects.all().delete()
        return JsonResponse({'message': '{} Payments were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def payment_detail(request, pk):
    try: 
        payment = Payment.objects.get(pk=pk) 
    except Payment.DoesNotExist: 
        return JsonResponse({'message': 'The payment does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        payment_serializer = PaymentSerializer(payment) 
        return JsonResponse(payment_serializer.data) 
 
    elif request.method == 'PUT': 
        payment_data = JSONParser().parse(request) 
        payment_serializer = PaymentSerializer(payment, data=payment_data) 
        if payment_serializer.is_valid(): 
            payment_serializer.save() 
            return JsonResponse(payment_serializer.data) 
        return JsonResponse(payment_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        payment.delete() 
        return JsonResponse({'message': 'The payment was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def payment_list_active(request):
    payment = Payment.objects.filter(published=True)
        
    if request.method == 'GET': 
        payment_serializer = PaymentSerializer(payment, many=True)
        return JsonResponse(payment_serializer.data, safe=False)

###################################              FARMER INPUT REQUEST              ############################### 

@api_view(['GET', 'POST', 'DELETE'])
def farmerinputrequest_list(request):
    if request.method == 'GET':
        farmerinputrequest = FarmerInputRequest.objects.all()
        
        title = request.query_params.get('name', None)
        if title is not None:
           farmerinputrequest = FarmerInputRequest.filter(name__icontains=name)
        
        farmerinputrequest_serializer = FarmerInputRequestSerializer(farmerinputrequest, many=True)
        return JsonResponse(farmerinputrequest_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        farmerinputrequest_data = JSONParser().parse(request)
        farmerinputrequest_serializer = FarmerInputRequestSerializer(data=farmerinputrequest_data)
        if farmerinputrequest_serializer.is_valid():
            farmerinputrequest_serializer.save()
            return JsonResponse(farmerinputrequest_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(farmerinputrequest_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = FarmerInputRequest.objects.all().delete()
        return JsonResponse({'message': '{} Farmer Input Request were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def farmerinputrequest_detail(request, pk):
    try: 
        farmerinputrequest = FarmerInputRequest.objects.get(pk=pk) 
    except FarmerInputRequest.DoesNotExist: 
        return JsonResponse({'message': 'The Farmer Input Request does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        farmerinputrequest_serializer = FarmerInputRequestSerializer(farmerinputrequest) 
        return JsonResponse(farmerinputrequest_serializer.data) 
 
    elif request.method == 'PUT': 
        farmerinputrequest_data = JSONParser().parse(request) 
        farmerinputrequest_serializer = FarmerInputRequestSerializer(farmerinputrequest, data=farmerinputrequest_data)
        if farmerinputrequest_serializer.is_valid(): 
            farmerinputrequest_serializer.save() 
            return JsonResponse(farmerinputrequest_serializer.data) 
        return JsonResponse(farmerinputrequest_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        farmerinputrequest.delete() 
        return JsonResponse({'message': 'Farmer Input Request was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
      
@api_view(['GET'])

def farmerinputrequest_list_active(request):
    farmerinputrequest = FarmerInputRequest.objects.filter(status="Active")
        
    if request.method == 'GET': 
       farmerinputrequest_serializer = FarmerInputRequestSerializer(farmerinputrequest, many=True)
    return JsonResponse(farmerinputrequest_serializer.data, safe=False)


 ###################################               FARMER INPUT REQUEST              ############################### 
##################################### REPORTS ###############################################
@api_view(['GET'])
def farmerstransactions_total(request,pk):
    cumulative_weight = FarmersTransactions.objects.filter(farmer=pk).aggregate(Sum('net_weight'))['weight__sum']
        
    if request.method == 'GET': 
        #transactions_serializer = TransactionsTotalSerializer(transactions, many=True)
        #return JsonResponse(transactions_serializer.data, safe=False)
        return JsonResponse({'cumulative_weight': cumulative_weight if cumulative_weight else 0,'farmer':pk})

@api_view(['GET'])
def farmerstransactions_perproduct_perperiod(request,pk,product_id,start_date,end_date):
    cumulative_weight = FarmersTransactions.objects.filter(farmer=pk).tx_date__range=(start_date, end_date).aggregate(Sum('net_weight'))['weight__sum']
        
    if request.method == 'GET': 
        #transactions_serializer = TransactionsTotalSerializer(transactions, many=True)
        #return JsonResponse(transactions_serializer.data, safe=False)
        return JsonResponse({'cumulative_weight': cumulative_weight if cumulative_weight else 0,'farmer':pk,'product': product_id})



 ################################### KILOSAHIHI END #######################################################