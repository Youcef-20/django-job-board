# Generated by Django 3.1.2 on 2020-10-05 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_job_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='description',
            new_name='Description',
        ),
        migrations.AddField(
            model_name='job',
            name='Experience',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='Published_at',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='job',
            name='Salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='Vacancy',
            field=models.IntegerField(default=1),
        ),
    ]
