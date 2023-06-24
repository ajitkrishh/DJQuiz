# Generated by Django 4.2.2 on 2023-06-23 08:22

from django.db import migrations, models
import myauth.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.CharField(default=myauth.models.stringUUID, editable=False, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.CharField(default=myauth.models.stringUUID, editable=False, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('question', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionSet',
            fields=[
                ('id', models.CharField(default=myauth.models.stringUUID, editable=False, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('is_true', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.CharField(default=myauth.models.stringUUID, editable=False, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.CharField(default=myauth.models.stringUUID, editable=False, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('result', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('question', models.ManyToManyField(to='Quiz.question')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
