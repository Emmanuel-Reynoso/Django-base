from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    # Path to access admin panel
    path('admin/', admin.site.urls),
    # Path to render home page
    path('', views.home, name="home"),
    
    # Path to ADD employee
    path('add_employee', views.add_employee, name="add_employee"),
    # Path to VIEW employee data individually
    path('employee/<str:employee_id>', views.employee, name="employee"),
    # Path to EDIT employee
    path('edit_employee', views.edit_employee, name="edit_employee"),
    # Path to DELETE employee
    path('delete_employee/<str:employee_id>', views.delete_employee, name="delete_employee"),
    # ----- Login / Logout ----- \
    path('login/', views.Login, name="login"),
    path('login_user', views.LoginUser, name="login_user"),
    path('logout/', views.LogoutUser, name="logout"),
]
