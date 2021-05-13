# Generated by Django 3.0.5 on 2021-05-12 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
                ('unit_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('stock', models.IntegerField(default=0)),
                ('image', models.ImageField(null=True, upload_to='product_images')),
            ],
        ),
    ]