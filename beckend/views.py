
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer
# Create your views here.
@api_view(['GET'])
def Student_list(request):
    students=Student.objects.all()
    serializer=StudentSerializer(students,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Single_Student(request,id):
    student=Student.objects.get(id=id)
    serializer=StudentSerializer(student)
    return Response(serializer.data)

@api_view(['POST'])
def Create_Student(request):
    serializer=StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
@api_view(['PUT','PATCH'])
def Update_Student(request,id):
    try:
        student=Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='PATCH':
        serializer=StudentSerializer(student,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def Delete_Student(request,id):
    student=Student.objects.get(id=id)
    delete=student.delete()
    return Response(delete)
    