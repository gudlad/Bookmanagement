# Generated by Django 3.2.6 on 2021-12-09 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_books_publication_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='publication_date',
            field=models.DateField(),
        ),
    ]
