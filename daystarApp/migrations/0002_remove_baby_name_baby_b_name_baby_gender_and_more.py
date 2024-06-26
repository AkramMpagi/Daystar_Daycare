# Generated by Django 5.0.4 on 2024-04-25 14:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daystarApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baby',
            name='name',
        ),
        migrations.AddField(
            model_name='baby',
            name='b_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='baby',
            name='gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='baby',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='baby',
            name='sponsor',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='baby',
            name='timeIn',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='baby',
            name='timeOut',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='baby',
            name='age',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('pay_no', models.IntegerField(blank=True, null=True)),
                ('currency', models.CharField(blank=True, default='Ugx', max_length=3, null=True)),
                ('c_pay', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='daystarApp.categorystay')),
                ('payee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='daystarApp.baby')),
            ],
        ),
    ]
