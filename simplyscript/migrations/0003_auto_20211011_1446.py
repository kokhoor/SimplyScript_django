# Generated by Django 3.2.7 on 2021-10-11 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simplyscript', '0002_auto_20211011_1444'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='groupactionpermission',
            constraint=models.UniqueConstraint(fields=('group', 'permission'), name='groupactionpermission_permission'),
        ),
        migrations.AddConstraint(
            model_name='useractionpermission',
            constraint=models.UniqueConstraint(fields=('user', 'permission'), name='useractionpermission_permission'),
        ),
    ]