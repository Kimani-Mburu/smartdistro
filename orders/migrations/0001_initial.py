# Generated by Django 3.2.9 on 2021-12-14 13:19

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UserInformation', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('reference_no', models.CharField(blank=True, max_length=12, null=True)),
                ('delivery_address', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vendor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserInformation.customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderOtherCharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_charges_total_price', models.IntegerField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
        ),
        migrations.CreateModel(
            name='OtherCharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=50)),
                ('rate', models.FloatField(default='0')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('total_value', models.FloatField()),
                ('status', models.CharField(choices=[('Shipped', 'Shipped'), ('Canceled', 'Canceled'), ('On-route', 'On-route'), ('Delivered', 'Delivered')], max_length=10)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_orders', to='orders.order')),
                ('other_Charges', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.orderothercharge')),
            ],
        ),
        migrations.AddField(
            model_name='orderothercharge',
            name='other_Charges',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.othercharge'),
        ),
        migrations.CreateModel(
            name='Order_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('total_cost', models.FloatField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]