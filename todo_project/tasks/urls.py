from django.urls import path
from django.contrib.auth import views as auth_views
from .views import task_list, add_task, complete_task, delete_task, edit_task, register

urlpatterns = [
    path("", task_list, name="task_list"),
    path("add/", add_task, name="add_task"),
    path("complete/<int:task_id>/", complete_task, name="complete_task"),
    path("delete/<int:task_id>/", delete_task, name="delete_task"),
    path('edit/<int:task_id>/', edit_task, name='edit_task'),

    path("register/", register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="tasks/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="task_list"), name="logout"),
]