# Generated by Django 3.0.8 on 2020-08-10 09:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0004_auto_20200805_1301'),
        ('news', '0004_auto_20200809_1819'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='news.Post')),
            ],
            bases=('news.post',),
        ),
        migrations.CreateModel(
            name='Health',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='news.Post')),
            ],
            bases=('news.post',),
        ),
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='news.Post')),
            ],
            bases=('news.post',),
        ),
        migrations.RenameModel(
            old_name='Trending',
            new_name='Education',
        ),
        migrations.RemoveField(
            model_name='post',
            name='body',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
