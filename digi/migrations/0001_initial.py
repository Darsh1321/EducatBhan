# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 02:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssgProfessor',
            fields=[
                ('assgid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('forwarded', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='AssgStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField(default=999)),
                ('uploaded', models.BooleanField()),
                ('assgas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi.AssgProfessor')),
            ],
        ),
        migrations.CreateModel(
            name='Classes_taught',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FE_A', models.BooleanField()),
                ('SE_A', models.BooleanField()),
                ('TE_A', models.BooleanField()),
                ('BE_A', models.BooleanField()),
                ('FE_B', models.BooleanField()),
                ('SE_B', models.BooleanField()),
                ('TE_B', models.BooleanField()),
                ('BE_B', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('mobileno', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=20)),
                ('sap', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('mobileno', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=20)),
                ('div', models.CharField(max_length=20)),
                ('sap', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='classes_taught',
            name='sapct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi.Professor'),
        ),
        migrations.AddField(
            model_name='assgstudent',
            name='sapas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi.Student'),
        ),
        migrations.AddField(
            model_name='assgprofessor',
            name='sapap',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi.Professor'),
        ),
    ]