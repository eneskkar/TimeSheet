from curses.ascii import HT
from logging import log
from sqlite3 import Time
from unicodedata import name
from django.http.response import JsonResponse
from Timeaapp.models import  Timesheet, Employee, Customer
from Timeaapp.serializer import TimesheetSerializer
from django.http import HttpResponse
from django.template import loader


# Create your views here.


def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())  

def get_timesheet(request,employee_id,date,hour1,hour2,customer,project,activity,description):

    if request.method=='GET':
      timesheets= Timesheet.objects.all()
      timesheet_Serializer = TimesheetSerializer(timesheets, many=True)
      return JsonResponse(timesheet_Serializer.data,safe=False)
    
    
    
def getTimeSheet(request, targetDate):
  ourResponse = {}
  if request.method != "GET":
    ourResponse["code"] = 1
    ourResponse["message"] = "Invalid request method. It must be (GET)"
    return JsonResponse(ourResponse)
  emplId = request.session["emplId"]
  tsResult = Timesheet.objects.filter(employee_id=emplId, date=targetDate)
  if tsResult.count() == 0:
    ourResponse["code"] = 2
    ourResponse["message"] = "Given date or employee id is invalid"
    return JsonResponse(ourResponse)
  
  tsResultObj = tsResult.all()
  outputList = []
  for i in tsResultObj:
    innerDict = {}
    innerDict["id"]= i.id
    innerDict["project"] = i.project 
    innerDict["hour1"] = i.hour1
    innerDict["hour2"] = i.hour2
    innerDict["activity"] = i.activity
    innerDict["description"] = i.description
    customerResult = Customer.objects.filter(id=i.customer_id)
    customerInfoDict = {"customerID": customerResult.first().id, "customerName": customerResult.first().customer_name}
    innerDict["customerInfo"] = customerInfoDict
    outputList.append(innerDict)

  ourResponse[targetDate] = outputList
  ourResponse["code"] = 0
  ourResponse["message"] = "Query successful"
  return JsonResponse(ourResponse)




def get_id_timesheet(request, emplId):
  ourResponse = {}
  
  if request.method != "GET":
    ourResponse["code"] = 1
    ourResponse["message"] = "Invalid request method. It must be (GET)"
    return JsonResponse(ourResponse)

  tsResult = Timesheet.objects.filter(employee_id=emplId)
  if tsResult.count() == 0:
    ourResponse["code"] = 2
    ourResponse["message"] = "Given date or employee id is invalid"
    return JsonResponse(ourResponse)

  tsResultObj = tsResult.all()
  
  outputList=[]
  for i in tsResultObj:
    innerDict = {}
    innerDict["id"]=i.id
    innerDict["date"]= i.date
    innerDict["project"] = i.project 
    innerDict["hour1"] = i.hour1
    innerDict["hour2"] = i.hour2
    innerDict["activity"] = i.activity
    innerDict["description"] = i.description
    customerResult = Customer.objects.filter(id=i.customer_id)
    customerInfoDict = {"customerID": customerResult.first().id, "customerName": customerResult.first().customer_name}
    innerDict["customerInfo"] = customerInfoDict
    outputList.append(innerDict)

  ourResponse[emplId] = outputList
  ourResponse["code"] = 0
  ourResponse["message"] = "Query successful"
  return JsonResponse(ourResponse)  




def LogIn(request,emplName, emplSurname):
  ourResponse = {}
  
  if request.method != "GET":
    ourResponse["code"] = 1
    ourResponse["message"] = "Invalid request method. It must be (GET)"
    return JsonResponse(ourResponse)

  employeesName = Employee.objects.filter(name=emplName)
  employeesSurname = Employee.objects.filter(name=emplSurname)

  if employeesName.count() == 0 and employeesSurname.count() == 0 :
    ourResponse["code"] = 2
    ourResponse["message"] = "Employee name Not Found"
    return JsonResponse(ourResponse)
    
  request.session["emplId"] = employeesName.first().id
  request.session["emplname"] = emplName
  request.session["emplSurname"] = emplSurname

  ourResponse["code"] = 0
  ourResponse["message"] = "Logged in successfully" 
  return JsonResponse(ourResponse) 




def LogOut(request):
  ourResponse = {}

  if request.session["emplId"] == None:
    ourResponse["code"] = 4
    ourResponse["message"] = "User is not logged in"
    return JsonResponse(ourResponse)

  request.session["emplId"] = None
  request.session["emplName"] = None
  request.session["emplSurname"] = None

  ourResponse["code"] = 0
  ourResponse["Message"] = "Logged out successfully"

  return JsonResponse(ourResponse)



def AddTimeSheet(request, date, h1, h2, custom, proj, activ, desc):
  ourResponse = {}
  
  if request.session.get("emplId") == None:
    ourResponse["code"] = 3
    ourResponse["message"] = "Employee must be logged in"
    return JsonResponse(ourResponse)

  customerObj = Customer.objects.filter(customer_name=custom)

  if customerObj.count() == 0:
    customerObj = Customer()
    customerObj.customer_name = custom
    customerObj.save()

  else:
    customerObj = customerObj.first()

  newTimeSheet = Timesheet()
  newTimeSheet.date = date
  newTimeSheet.hour1 = h1
  newTimeSheet.hour2 = h2  
  newTimeSheet.customer = customerObj
  newTimeSheet.project = proj
  newTimeSheet.activity = activ
  newTimeSheet.description = desc
  newTimeSheet.employee_id = request.session["emplId"]

  newTimeSheet.save()

  ourResponse["code"] = 0
  ourResponse["message"] = "Timesheet created successfully"
  return JsonResponse(ourResponse)


def EditTimesheet(request,id,date, h1, h2, customer, proj, activ, desc):
  ourResponse={}

  
  if request.session.get("emplId") == None:
    ourResponse["code"] = 3
    ourResponse["message"] = "Employee must be logged in"
    return JsonResponse(ourResponse)

  idRes=Timesheet.objects.filter(id=id)  
  customerObj = Customer.objects.filter(customer_name=customer)


  if idRes.count() == 0:
    ourResponse["code"] = 5
    ourResponse["message"] = "Not Found Row"
    return JsonResponse(ourResponse)
  print(customerObj)
  EdtTimesheet= idRes.first()
  EdtTimesheet.date = date
  EdtTimesheet.hour1= h1
  EdtTimesheet.hour2= h2 
  EdtTimesheet.customer= customerObj.first()
  EdtTimesheet.project= proj
  EdtTimesheet.activity= activ
  EdtTimesheet.description= desc
  EdtTimesheet.employee_id= request.session["emplId"]

  EdtTimesheet.save()
  ourResponse["code"] = 0
  ourResponse["message"] = "Timesheet edited successfully"
  print(EdtTimesheet.customer)

  return JsonResponse(ourResponse)  


def DeleteTimesheet(request, id):
  ourResponse={}  
   
  idRes=Timesheet.objects.filter(id=id) 

  if idRes.count() == 0:
    ourResponse["code"] = 5
    ourResponse["message"] = "Not Found Row"
    return JsonResponse(ourResponse)

  idRes.first().delete()  
  ourResponse["code"] = 0
  ourResponse["message"] = "Timesheet deleted successfully"
  return JsonResponse(ourResponse) 



def CheckLoginState(request):
  ourResponse = {}

  if request.session.get("emplId") == None:
    ourResponse["code"] = 1
    return JsonResponse(ourResponse)

  ourResponse["code"] = 0
  return JsonResponse(ourResponse)