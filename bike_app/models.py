from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


TRANSACTION_STATUSES = (
    (1, "Aktywne"),
    (2, "Sprzedane"),
    (3, "Zarchiwizowane"),
)


MESSAGE_STATUSES = (
    (1, "Przeczytane"),
    (2, "Nieprzeczytane"),
    (3, "Draft"),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50, blank=True)
    tel_num = models.IntegerField(null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)


class Offer(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ManyToManyField(User, through="Transaction")


class Transaction(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=TRANSACTION_STATUSES)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Message(models.Model):
    msg_text = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=MESSAGE_STATUSES)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='recipient_user', null=True, on_delete=models.CASCADE)

