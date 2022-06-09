from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

TRANSACTION_STATUSES = (
    (1, "Aktywne"),
    (2, "Zakończone"),
    (3, "Zarchiwizowane"),
)


MESSAGE_STATUSES = (
    (1, "Przeczytane"),
    (2, "Nieprzeczytane"),
    (3, "Wersja robocza"),
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
    slug = models.SlugField(max_length=64)

    def __str__(self):
        return self.name


class Offer(models.Model):
    name = models.CharField(max_length=64, verbose_name='Nazwa')
    description = models.TextField(max_length=1000, verbose_name='Opis')
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Cena')
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=TRANSACTION_STATUSES, default=1)
    category = models.ManyToManyField(Category, verbose_name='Kategoria')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def category_names(self):
        return ', '.join([c.name for c in self.category.all()])

    def get_absolute_url(self):
        return reverse('offer_detail', args=[self.id])


class Message(models.Model):
    msg_text = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=MESSAGE_STATUSES)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='recipient_user', null=True, on_delete=models.CASCADE)
