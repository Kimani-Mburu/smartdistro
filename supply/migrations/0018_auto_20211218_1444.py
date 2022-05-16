# Generated by Django 3.2.9 on 2021-12-18 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20211218_1417'),
        ('supply', '0017_auto_20211214_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='other_Charges',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order_other_charge'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='status',
            field=models.CharField(blank=True, choices=[('Shipped', 'Shipped'), ('Canceled', 'Canceled'), ('On-route', 'On-route'), ('Delivered', 'Delivered')], max_length=10, null=True),
        ),
    ]