# Generated by Django 4.2.13 on 2024-05-15 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daystarApp', '0012_alter_baby_father_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitter',
            name='location',
            field=models.CharField(choices=[('Kabalagala', 'Kabalagala'), ('', '')], default=True, max_length=100),
            preserve_default=False,
        ),
    ]