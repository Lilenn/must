from rest_framework import serializers
from courses.models import Subject,Course


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id','title','slug']

# class ModuleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Module
#         fields = ['title','description']


