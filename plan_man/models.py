from django.db import models
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist


class User(models.Model):
    user_id = models.TextField(max_length=30, primary_key=True)
    password = models.TextField(max_length=30)
    name = models.TextField(max_length=30)

    def __str__(self):
        return self.user_id

    def create(self, user_id, password, name):
        u = User(user_id, password, name)
        u.save()

    def read(self, user_id):
        u = User.objects.get(user_id=user_id)
        return u

    def update(self, user_id, password, name):
        u = User.objects.get(user_id=user_id)
        u.password = password
        u.name = name
        u.save()

    def dele(self, user_id):
        u = User.objects.get(user_id=user_id)
        u.delete()

    def is_exist(self, user_id):
        exist = True
        try:
            User.objects.get(user_id=user_id)
        except ObjectDoesNotExist:
            exist = False
        return exist


class Plan(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=200)
    iteration_type = models.IntegerField()
    frequency = models.TextField(max_length=13)
    object_time = models.IntegerField()
    complete_day = models.IntegerField(default=0)
    start_day = models.DateField(default=timezone.now())

    class Meta:
        unique_together = (("user_id", "name"),)

    def __str__(self):
        return self.user_id.__str__() + "." + self.name

    def create(self, user_id, name, iteration_type, frequency, object_time, complete_day=0):
        # start_day는 default값인 datetime.today() 들어감
        user = User()
        p = Plan(user_id=user.read(user_id=user_id),
                 name=name,
                 iteration_type=iteration_type,
                 frequency=frequency,
                 object_time=object_time,
                 complete_day=complete_day,
                 start_day=timezone.now())
        p.save()

    def read(self, user_id, name):
        p = Plan.objects.get(user_id=user_id, name=name)
        return p

    def update(self, user_id, prev_name, name, iteration_type, frequency, object_time, complete_day):
        # start_day는 default값인 datetime.today() 들어감
        p = Plan.objects.get(user_id=user_id, name=prev_name)
        p.name = name
        p.iteration_type = iteration_type
        p.frequency = frequency
        p.object_time = object_time
        p.complete_day = complete_day
        p.save()

    def dele(self, user_id, name):
        p = Plan.objects.get(user_id=user_id, name=name)
        p.delete()

    def is_exist(self, user_id, name):
        exist = True
        try:
            Plan.objects.get(user_id=user_id, name=name)
        except ObjectDoesNotExist:
            exist = False
        return exist


class Work(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.ForeignKey(Plan, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now())
    complete_time = models.IntegerField(default=0)

    class Meta:
        unique_together = (("user_id", "name", "date"),)

    def __str__(self):
        return self.user_id.__str__() + "." + \
               self.name.__str__() + "." + str(self.date)

    def create(self, user_id, name, date, complete_time):
        plan = Plan()
        user = User()
        w = Work.objects.create(user_id=user.read(user_id=user_id),
                                name=plan.read(user_id=user_id, name=name),
                                date=date,
                                complete_time=complete_time)  # date는 default값인 datetime.today() 들어감
        w.save()

    def read(self, user_id, name, date):
        user = User()
        plan = Plan()
        print(User.objects.get(user_id=user_id))
        w = Work.objects.get(user_id=user.read(user_id=user_id),
                             name=plan.read(user_id=user_id, name=name)
                             , date=date)
        return w

    def update(self, user_id, name, date, complete_time):
        user = User()
        plan = Plan()
        w = Work.objects.get(user_id=user.read(user_id=user_id),
                             name=plan.read(user_id=user_id, name=name),
                             date=date)
        print(w.user_id.user_id, w.name.name, w.date, w.complete_time)
        w.complete_time = complete_time
        # date는 default값인 datetime.today() 들어감
        w.save()

    def dele(self, user_id, name, date):
        user = User()
        plan = Plan()
        w = Work.objects.get(user_id=user.read(user_id=user_id),
                             name=plan.read(user_id=user_id, name=name),
                             date=date)
        w.delete()

    def is_exist(self, user_id, name, date):
        exist = True
        user = User()
        plan = Plan()
        try:
            Work.objects.get(user_id=user.read(user_id=user_id),
                             name=plan.read(user_id=user_id, name=name),
                             date=date)
        except ObjectDoesNotExist:
            exist = False
        return exist
