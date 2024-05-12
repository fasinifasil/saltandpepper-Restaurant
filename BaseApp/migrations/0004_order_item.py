# Generated by Django 5.0.6 on 2024-05-11 21:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BaseApp', '0003_burgermodel'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemNumber', models.CharField(max_length=60)),
                ('bill', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateField(auto_now_add=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('size', models.CharField(max_length=60)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BaseApp.order')),
            ],
        ),
    ]
