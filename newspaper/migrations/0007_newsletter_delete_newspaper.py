# Generated by Django 4.2.3 on 2023-08-06 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0006_newspaper'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='NewsPaper',
        ),
    ]
