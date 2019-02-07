import json
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.template import loader

from plan_man import apis
from .models import *


def main(request):
    template = loader.get_template('plan_man/main.html')
    return HttpResponse(template.render({}, request))


def plan_listt(request):
    p_list = Plan.objects.all()
    template = loader.get_template('plan_man/plan_list.html')
    context = {
        'plan_list': p_list
    }
    return HttpResponse(template.render(context, request))


def login(request):
    template = loader.get_template('plan_man/login.html')
    return HttpResponse(template.render({}, request))


def logout(request):
    del request.session['user_id']
    return redirect('plan_man:main')


def login_action(request):
    user_data = json.loads(apis.request_bytes_to_json(request))
    try:
        # id, password가 모두 일치하는 object가 있는지 체크 없으면 exception 있으면 세션에 값 추가
        User.objects.get(user_id=user_data['user_id'], password=user_data['password'])
        request.session['user_id'] = user_data['user_id']
    except ObjectDoesNotExist:
        return HttpResponse("Wrong ID or Password!")
    return redirect('plan_man:main')


################## user


def create_user(request):
    template = loader.get_template('plan_man/create_user.html')
    return HttpResponse(template.render({}, request))


def select_user(request):
    template = loader.get_template('plan_man/select_user.html')
    return HttpResponse(template.render({}, request))

def detail_user(request):
    template = loader.get_template('plan_man/detail_user.html')
    data = User.objects.get(user_id=request.session['user_id'])
    context = {
        'user_id': data.user_id,
        'name': data.name,
    }
    return HttpResponse(template.render(context, request))


def update_user(request):
    template = loader.get_template('plan_man/update_user.html')
    data = apis.bytes_to_dict(apis.user_read(request).content)
    context = {
        'user_id': data["user_id"],
        'name': data["name"],
        'password': data["password"]
    }
    return HttpResponse(template.render(context, request))


def create_user_api(request):
    return HttpResponse(apis.user_create(request))


def update_user_api(request):
    return HttpResponse(apis.user_update(request))


def delete_user_api(request):
    return HttpResponse(apis.user_delete(request))


############### plan


def create_plan(request):
    template = loader.get_template('plan_man/create_plan.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def select_plan(request):
    template = loader.get_template('plan_man/select_plan.html')
    plan_list = Plan.objects.filter(user_id=request.session['user_id']).order_by('name')
    context = {'plan_list': plan_list}
    return HttpResponse(template.render(context, request))


def detail_plan(request):
    template = loader.get_template('plan_man/detail_plan.html')
    data = apis.bytes_to_dict(apis.plan_read(request).content)
    if data['Result'] == 'false':
        return HttpResponseNotFound("Object Does Not Exist.")
    work_list = Work.objects.filter(user_id=User().read(user_id=data['user_id']),
                                    name=Plan().read(user_id=data['user_id'], name=data['name'])) \
        .order_by('date')
    # date fromat error 때문에 YYYY-MM-DD 포멧의 str() list()로 캐스팅
    work_list = [w.date.strftime("%Y-%m-%d") for w in work_list]
    context = {
        'user_id': data["user_id"],
        'name': data["name"],
        'iteration_type': data["iteration_type"],
        'frequency': data["frequency"],
        'object_time': data["object_time"],
        'complete_day': data["complete_day"],
        'start_day': data["start_day"],
        'work_list': work_list
    }
    return HttpResponse(template.render(context, request))


def update_plan(request):
    template = loader.get_template('plan_man/update_plan.html')
    data = apis.bytes_to_dict(apis.plan_read(request).content)
    context = {
        'user_id': data["user_id"],
        'name': data["name"],
        'iteration_type': data["iteration_type"],
        'frequency': data["frequency"],
        'object_time': data["object_time"],
        'complete_day': data["complete_day"],
        'start_day': data["start_day"]
    }
    return HttpResponse(template.render(context, request))


def create_plan_api(request):
    return HttpResponse(apis.plan_create(request))


def update_plan_api(request):
    return HttpResponse(apis.plan_update(request))


def delete_plan_api(request):
    return HttpResponse(apis.plan_delete(request))


################## work


def create_work(request):
    template = loader.get_template('plan_man/create_work.html')
    data = apis.bytes_to_dict(apis.plan_read(request).content)
    context = {
        'user_id': data["user_id"],
        'name': data["name"],
    }
    return HttpResponse(template.render(context, request))


def select_work(request):
    template = loader.get_template('plan_man/select_work.html')
    return HttpResponse(template.render({}, request))


def detail_work(request):
    template = loader.get_template('plan_man/detail_work.html')
    data = apis.bytes_to_dict(apis.work_read(request).content)
    if data["Result"] == 'false':
        return HttpResponseNotFound("Object Does Not Exist.")
    context = {
        'user_id': data["user_id"],
        'name': data["name"],
        'date': data['date'],
        'complete_time': data["complete_time"],
    }
    return HttpResponse(template.render(context, request))


def update_work(request):
    template = loader.get_template('plan_man/update_work.html')
    data = apis.bytes_to_dict(apis.work_read(request).content)
    context = {
        'user_id': data["user_id"],
        'name': data["name"],
        'date': data["date"],
        'complete_time': data["complete_time"],
    }
    return HttpResponse(template.render(context, request))


def create_work_api(request):
    return HttpResponse(apis.work_create(request))


def read_work_api(request):
    return HttpResponse(apis.work_read(request))


def update_work_api(request):
    return HttpResponse(apis.work_update(request))


def delete_work_api(request):
    return HttpResponse(apis.work_delete(request))
