# Generated by Django 4.2.2 on 2023-06-24 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0003_remove_test_question_remove_test_result_test_score_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='topic',
            field=models.ForeignKey(default='60e8a3b2-3da7-4ddf-9ae6-b7d37b3b79bf', on_delete=django.db.models.deletion.CASCADE, to='Quiz.topic'),
            preserve_default=False,
        ),
    ]
