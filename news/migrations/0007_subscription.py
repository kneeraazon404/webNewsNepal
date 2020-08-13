# Generated by Django 3.0.8 on 2020-08-10 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=150)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]