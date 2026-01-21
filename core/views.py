from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer, UserSerializer, ProjectWithTasksSerializer
from .permissions import IsAdmin
from rest_framework.exceptions import PermissionDenied
from django.utils.timezone import now
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Prefetch


User = get_user_model()

class ProjectViewSet(ModelViewSet):
    '''Admins can create and manage projects.'''
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class TaskViewSet(ModelViewSet):
    '''
        Admins can create tasks.
        Users can update only their assigned tasks.
    '''
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Only admin can create tasks
        if self.request.user.role != "admin":
            raise PermissionDenied("Only admin can create tasks")

        serializer.save()

    def perform_update(self, serializer):
        task = self.get_object()
        user = self.request.user
        new_status = self.request.data.get("status")

        # If task is overdue, only admin can mark it as done
        if task.status == "overdue" and new_status == "done":
            if user.role != "admin":
                raise PermissionDenied("Only admin can close overdue tasks")

        serializer.save()

class UserViewSet(ReadOnlyModelViewSet):
    '''Read-only view for listing users.'''
    queryset = User.objects.filter(role="user").only("id", "email")
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class ProjectTasksView(APIView):
    '''
        Admins see all tasks.
        Users see only tasks assigned to them.
    '''
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        task_qs = Task.objects.select_related("assigned_to")

        if user.role != "admin":
            task_qs = task_qs.filter(assigned_to=user)

        projects = Project.objects.prefetch_related(
            Prefetch("tasks", queryset=task_qs)
        )

        serializer = ProjectWithTasksSerializer(projects, many=True)
        return Response(serializer.data)
    
class RunOverdueCheckView(APIView):
    '''
        Admin-only endpoint to mark overdue tasks.
        Tasks past due date and not completed are marked as overdue.
    '''
    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request):
        updated_count = Task.objects.filter(
            due_date__lt=now(),
            status="in_progress"
        ).update(status="overdue")

        return Response({
            "message": "Overdue task check completed",
            "tasks_marked_overdue": updated_count
        })