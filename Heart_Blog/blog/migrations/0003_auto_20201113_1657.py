# Generated by Django 3.1.3 on 2020-11-13 15:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201111_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogarticle',
            name='date_to',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogarticle',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='blog-pics'),
        ),
    ]