from rest_framework import serializers
from .models import Project, Task
from django.contrib.auth import get_user_model

User = get_user_model()

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "name", "description", "created_by", "created_at", "updated_at"]
        read_only_fields = ["id", "created_by", "created_at", "updated_at"]

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "project",
            "assigned_to",
            "status",
            "priority",
            "due_date",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_status(self, value):
        instance = self.instance

        # If task is already overdue, it cannot move back to in_progress
        if instance and instance.status == "overdue" and value == "in_progress":
            raise serializers.ValidationError(
                "Overdue task cannot be moved back to in_progress"
            )

        return value
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email"]


class AssignedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email"]

class TaskReadSerializer(serializers.ModelSerializer):
    assigned_to = AssignedUserSerializer(read_only=True)
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "status",
            "priority",
            "due_date",
            "assigned_to",
        ]

class ProjectWithTasksSerializer(serializers.ModelSerializer):
    tasks = TaskReadSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ["id", "name", "description", "tasks"]
