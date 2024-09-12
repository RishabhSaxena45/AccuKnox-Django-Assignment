from django.db import models , transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=20)
    empid = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Review(models.Model):
    content = models.CharField(max_length=50)
    
@receiver(post_save, sender=Review)
def after_save(sender, instance, **kwargs):
    print("Signal handler: Creating Review log...")
    Review.objects.create(action=f"Created Review with id {instance.id}")

def signal_test():
    try:
        with transaction.atomic():
            print("Caller: Creating Employee instance...")
            instance = Employee(name="Raman" , empid=254)
            instance.save()

            print("Caller: Raising exception to force rollback...")
            raise Exception("Forcing rollback!")
    except Exception as e:
        print(f"Exception: {e}")
    review_logs = Review.objects.all()
    if review_logs.exists():
        print("Review entries exist (signal was not rolled back)")
    else:
        print("No Review entries (signal was rolled back)")

signal_test()