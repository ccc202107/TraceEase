# Generated by Django 4.2.9 on 2024-04-02 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trace_app', '0003_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_progress',
            field=models.CharField(choices=[('Model training', 'MODEL_TRAINING'), ('Completed', 'COMPLETED'), ('Anomaly labeling', 'ANOMALY_LABELING'), ('Root Cause labeling', 'ROOT_CAUSE_LABELING')], default='Model training', max_length=100),
        ),
    ]
