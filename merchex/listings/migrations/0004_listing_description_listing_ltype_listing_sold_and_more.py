# Generated by Django 5.0.3 on 2024-03-20 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_band_active_band_biography_band_genre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='listing',
            name='ltype',
            field=models.CharField(choices=[('RD', 'Record'), ('CL', 'Clothing'), ('PT', 'Posters'), ('MS', 'Miscellaneous')], default='RD', max_length=5),
        ),
        migrations.AddField(
            model_name='listing',
            name='sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='listing',
            name='year',
            field=models.IntegerField(default=2000),
        ),
        migrations.AlterField(
            model_name='listing',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
