# Generated by Django 4.1.3 on 2022-11-26 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentarios',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comentarios',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AlterField(
            model_name='comentarios',
            name='nombre',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='comentarios',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Posts.post'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='nombre',
            field=models.CharField(max_length=40),
        ),
    ]
