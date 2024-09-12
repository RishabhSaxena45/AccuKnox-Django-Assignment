from django.db import models
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name
    
@receiver(post_save , sender=Student)
def after_save(sender , instance , **kwargs):
    print(f'Signal thread id : {threading.get_ident()}')
    
def signal_test():
    print(f'Caller Thread id : {threading.get_ident()}')
    
    instance = Student(name="Dhruv" , age=16)
    instance.save()
    
signal_test()