from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TaskViewSet, UserViewSet, ProjectTasksView, RunOverdueCheckView
from django.urls import path

router = DefaultRouter()
router.register(r"projects", ProjectViewSet, basename="projects")
router.register(r"tasks", TaskViewSet, basename="tasks")
router.register("users", UserViewSet, basename="users")


urlpatterns = [
    path("projects-with-tasks/", ProjectTasksView.as_view()),
    path("run-overdue-check/", RunOverdueCheckView.as_view())
] + router.urls
