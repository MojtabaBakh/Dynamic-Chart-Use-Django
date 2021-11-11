# Generated by Django 3.2.9 on 2021-11-11 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Lessonscore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Score', models.IntegerField()),
                ('Lesson', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.lesson')),
            ],
        ),
    ]
