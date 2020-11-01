# Generated by Django 3.0.6 on 2020-06-24 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=124)),
                ('principal', models.CharField(max_length=124)),
                ('location', models.CharField(max_length=124)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=124)),
                ('age', models.PositiveIntegerField()),
                ('School', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='basic_app.School')),
            ],
        ),
    ]