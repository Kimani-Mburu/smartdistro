# Generated by Django 3.2.9 on 2021-12-20 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_units_unit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='availability_wef_date',
            new_name='product_availability_wef_date',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='availability_wet_date',
            new_name='product_availability_wet_date',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='product_category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='created_on',
            new_name='product_created_on',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='product_description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='farmer',
            new_name='product_farmer_id',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='images',
            new_name='product_images',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='is_featured',
            new_name='product_is_featured',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='location',
            new_name='product_location',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='other_image',
            new_name='product_other_image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='other_image1',
            new_name='product_other_image1',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='unit',
            new_name='product_unit',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='unit_price',
            new_name='product_unit_price',
        ),
    ]