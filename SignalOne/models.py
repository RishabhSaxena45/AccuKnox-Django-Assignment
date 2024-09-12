from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
import time

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name
    


@receiver(post_save , sender=Student)
def after_save(sender , instance , **kwargs):
    print("Post save signal started")
    time.sleep(5)
    print("Post save signal completed")
    

def signal_test():
    print("Saving Model Data")
    start_time = datetime.now()
    
    instance = Student(name="Rishabh" , age=22)
    instance.save()

    end_time = datetime.now()
    elapsed_time = (end_time - start_time).total_seconds()
    print(f"Total time for saving instance: {elapsed_time} seconds")
    
signal_test()