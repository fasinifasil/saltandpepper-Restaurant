# Generated by Django 5.0.6 on 2024-05-08 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BaseApp', '0002_alter_pizzamodel_pizzapricel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BurgerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BurgerName', models.CharField(max_length=20)),
                ('BurgerpriceM', models.DecimalField(decimal_places=2, max_digits=5)),
                ('BurgerpriceL', models.DecimalField(decimal_places=2, max_digits=5)),
                ('BurgerImage', models.URLField()),
            ],
        ),
    ]
