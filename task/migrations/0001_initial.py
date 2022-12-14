# Generated by Django 4.0.6 on 2022-08-14 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('state', models.CharField(choices=[('Incomplete', 'Incomplete'), ('Complete', 'Complete'), ('Ongoing', 'Ongoing')], max_length=10)),
                ('limit', models.IntegerField(default=2)),
                ('completion_date', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.users')),
            ],
        ),
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=False)),
                ('priority', models.CharField(choices=[('high', 'high'), ('medium', 'medium'), ('low', 'low')], max_length=6)),
                ('ctvalue', models.IntegerField()),
                ('ctunit', models.CharField(choices=[('hours', 'hours'), ('minutes', 'minutes'), ('seconds', 'seconds')], max_length=7)),
                ('creation', models.DateTimeField(auto_now_add=True)),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.goal')),
            ],
        ),
    ]
