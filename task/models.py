from django.db import models
from user.models import users
priority_choice=(("high","high"),("medium","medium"),("low","low"))
ctunit_choice=(("hours","hours"),("minutes","minutes"),("seconds","seconds"))
state_choice=(("Incomplete","Incomplete"),("Complete","Complete"),("Ongoing","Ongoing"))

class goal(models.Model):
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=10,choices=state_choice)
    limit = models.IntegerField(default=2)
    completion_date = models.DateTimeField()
    user=models.ForeignKey(users,on_delete=models.CASCADE)    

class task(models.Model):
    name = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    priority = models.CharField(max_length=6,choices=priority_choice)
    ctvalue= models.IntegerField()
    ctunit = models.CharField(max_length=7,choices=ctunit_choice)
    creation = models.DateTimeField(auto_now_add=True)
    goal=models.ForeignKey(goal,on_delete=models.CASCADE)
