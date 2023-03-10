# Generated by Django 4.1.7 on 2023-03-02 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0004_skills_relevant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='category',
        ),
        migrations.AlterField(
            model_name='skills',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='projects',
            name='category',
            field=models.ManyToManyField(to='model.skills'),
        ),
    ]
