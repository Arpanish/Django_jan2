# Generated by Django 4.1.4 on 2022-12-20 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0005_alter_computer_computer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='computer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='computer.computerspecification'),
        ),
    ]
