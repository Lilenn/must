from rest_framework import generics
from courses.models import Subject,Module,Course
from courses.api.serializers import  SubjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.authentication import BasicAuthentication

class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

# class ModuleListView(generics.ListAPIView):
#     queryset = Module.objects.all()
#     serializer_class = ModuleSerializer


class CourseEnrollView(APIView):
    authentication_classes = (BasicAuthentication,)
    def post(self,request,pk,format=None):
        course = get_object_or_404(Course,pk=pk)
        course.students.add(request.user)
        return Response({"enrolled":True})