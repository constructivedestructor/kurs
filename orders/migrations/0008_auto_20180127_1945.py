# Generated by Django 2.0 on 2018-01-27 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_productinorder_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='adres',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя покупателя'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Status'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='nmb',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='Количество товара в заказе'),
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='size',
            field=models.IntegerField(blank=True, default=30, null=True, verbose_name='Размер(см)'),
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True),
        ),
    ]
