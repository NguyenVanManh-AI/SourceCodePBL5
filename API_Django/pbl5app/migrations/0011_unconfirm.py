# Generated by Django 4.1.7 on 2023-05-26 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pbl5app', '0010_attendanceimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unconfirm',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_user', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
