# Generated by Django 4.2.13 on 2024-05-15 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daystarApp', '0015_sitter_nin_sitter_recommender_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitter',
            name='level_of_education',
            field=models.CharField(choices=[('Degree', 'Degree'), ('Diploma', 'Diploma'), ('UACE', 'UACE'), ('UCE', 'UCE')], default=True, max_length=100),
            preserve_default=False,
        ),
    ]
