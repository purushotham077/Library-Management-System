# Generated by Django 5.0.1 on 2024-03-06 06:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0019_alter_book_issue_due_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_issue',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 14, 12, 0, 50, 578644), help_text='Date the book is due to'),
        ),
    ]