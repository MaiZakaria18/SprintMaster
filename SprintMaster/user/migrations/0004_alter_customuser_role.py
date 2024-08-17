# Generated by Django 5.0.6 on 2024-08-16 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_customuser_managers_alter_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('manager', 'Manager'), ('junior', 'junior'), ('senior', 'senior')], default='employee', max_length=20),
        ),
    ]
