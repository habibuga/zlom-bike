# Generated by Django 4.0.4 on 2022-06-02 09:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bike_app', '0005_remove_category_description_category_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='status',
            field=models.IntegerField(choices=[(1, 'Aktywne'), (2, 'Sprzedane'), (3, 'Zarchiwizowane')], default=1),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='offer',
            name='category',
        ),
        migrations.AddField(
            model_name='offer',
            name='category',
            field=models.ManyToManyField(to='bike_app.category'),
        ),
        migrations.RemoveField(
            model_name='offer',
            name='user',
        ),
        migrations.AddField(
            model_name='offer',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
