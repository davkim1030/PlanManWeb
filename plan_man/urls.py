from django.urls import path

from plan_man import apis
from . import views

app_name = 'plan_man'
urlpatterns = [
    # ex: 127.0.0.1/plan_detail/davkim&work%20out/
    # path('plan_detail/<str:user_id>&<str:name>/', views.detail, name='detail'),

    # ex: 127.0.0.1/
    path('', views.main, name='main'),
    path('login/', views.login, name='login'),
    path('login_action/', views.login_action, name='login_action'),
    path('logout/', views.logout, name='logout'),

    # views
    # ex: 127.0.0.1/create_user/
    path('sign_up/', views.create_user, name='create_user'),
    path('detail_user/', views.detail_user, name='detail_user'),
    path('update_user/', views.update_user, name='update_user'),

    path('create_plan/', views.create_plan, name='create_plan'),
    path('detail_plan/', views.detail_plan, name='detail_plan'),
    path('select_plan/', views.select_plan, name='select_plan'),
    path('update_plan/', views.update_plan, name='update_plan'),

    path('create_work/', views.create_work, name='create_work'),
    path('detail_work/', views.detail_work, name='detail_work'),
    path('select_work/', views.select_work, name='select_work'),
    path('update_work/', views.update_work, name='update_work'),

    # apis
    # ex: 127.0.0.1/api/<str:model_name>/<str:method>/    with POST method
    path('api/user/create/', apis.user_create, name='create_user_api'),
    path('api/user/read/', apis.user_read, name='read_user_api'),
    path('api/user/update/', apis.user_update, name='update_user_api'),
    path('api/user/delete/', apis.user_delete, name='delete_user_api'),

    path('api/plan/create/', apis.plan_create, name='create_plan_api'),
    path('api/plan/read/', apis.plan_read, name='read_plan_api'),
    path('api/plan/update/', apis.plan_update, name='update_plan_api'),
    path('api/plan/delete/', apis.plan_delete, name='delete_plan_api'),

    path('api/work/create/', apis.work_create, name='create_work_api'),
    path('api/work/read/', apis.work_read, name='read_work_api'),
    path('api/work/update/', apis.work_update, name='update_work_api'),
    path('api/work/delete/', apis.work_delete, name='delete_work_api'),
]
