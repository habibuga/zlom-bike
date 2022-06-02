# Generated by Django 4.0.4 on 2022-06-02 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bike_app', '0006_offer_date_added_offer_status_remove_offer_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='status',
            field=models.IntegerField(choices=[(1, 'Aktywne'), (2, 'Sprzedane'), (3, 'Zarchiwizowane')], default=1),
        ),
        migrations.AlterField(
            model_name='offer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
