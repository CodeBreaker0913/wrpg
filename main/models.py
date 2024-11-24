from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Skills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="skills", null=True)
    name = models.CharField(max_length=200)
    level = models.IntegerField(default=1)
    current_exp = models.IntegerField(default=0)
    rank = models.CharField(max_length=200)
    exp_required = models.IntegerField(default=150)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update_exp_required()
        self.update_rank()

    def is_highest_level(self):
        highest_level = Skills.objects.filter(name=self.name).exclude(pk=self.pk).aggregate(models.Max('level'))['level__max']
        return highest_level is None or self.level >= highest_level

    def update_rank(self):
        
        if self.level < 10:
            self.rank = "novice"
        elif self.level < 20:
            self.rank = "apprentice"
        elif self.level < 30:
            self.rank = "journeyman"
        elif self.level < 40:
            self.rank = "adept"
        elif self.level < 40:
            self.rank = "expert"
        elif self.level < 50:
            self.rank = "master"
        else:
            if self.is_highest_level():
                self.rank = "sage"
            else:
                self.rank = "grandmaster"

    def set_level(self, new_level):
        self.level = new_level
        self.update_exp_required()
        self.update_rank() 
    
    def add_exp(self, added_exp):
        self.current_exp += added_exp
        if self.current_exp >= self.exp_required:
            next_level = self.level + 1
            self.set_level(new_level=next_level)
    
    def update_exp_required(self):
        self.exp_required = int(100 * (1.5 ** int(self.level)))

    def __str__(self):
        return self.name


'''
class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
'''
