# Generated by Django 3.2.12 on 2023-01-16 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20230116_1850'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name': 'Historia', 'verbose_name_plural': 'Historias'},
        ),
    ]
