from django.urls import path
from .views import Student_list,Create_Student,Update_Student,Delete_Student,Single_Student


urlpatterns=[
    path('students/',Student_list,name="list"),
    path('students/<int:id>/',Single_Student,name="student_list"),
    path('create/',Create_Student,name="create"),
    path('update/<int:id>/',Update_Student,name="update"),
    path('delete/<int:id>/',Delete_Student,name="delete")
]