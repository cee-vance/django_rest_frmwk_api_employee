from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from rest_framework import permissions
from .serializers import EmployeeSerializer
from .models import Employee

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allows Employees to be viewed
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

# Create your views here.
# try generic apidetail
class EmployeeDetail( mixins.RetrieveModelMixin,
                      generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args,**kwargs)



class EmployeeCreate( mixins.CreateModelMixin,
                      generics.GenericAPIView):
    """
    Generic APIView for creating an Employee
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def post(self,request, *args,**kwargs):
        return self.create(request, *args, **kwargs)


class EmployeeUpdate( mixins.UpdateModelMixin,
                      generics.GenericAPIView):
    """
    Generic APIView for updating an Employee
    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def put(self,request, *args,**kwargs):
        return self.update(request, *args, **kwargs)


class EmployeeDelete(mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    """
    generic APIView for deleting Employee
    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def delete(self, request, *args,**kwargs):
        return self.destroy(request,*args,**kwargs)



