# Generated by Django 4.2.9 on 2024-04-06 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0005_alter_customer_customer_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docrawin',
            name='doc_raw_in_date',
            field=models.DateField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='docrawin',
            name='doc_raw_in_num',
            field=models.CharField(max_length=50, verbose_name='Номер документа'),
        ),
        migrations.AlterField(
            model_name='docrawin',
            name='doc_raw_in_sum',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Сумма'),
        ),
        migrations.AlterField(
            model_name='docrawin',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.supplier', verbose_name='Поставщик'),
        ),
        migrations.AlterField(
            model_name='docrawint',
            name='doc_raw_in',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.docrawin', verbose_name='Номер документа'),
        ),
        migrations.AlterField(
            model_name='docrawint',
            name='doc_raw_in_cost',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена сырья'),
        ),
        migrations.AlterField(
            model_name='docrawint',
            name='doc_raw_in_quantity',
            field=models.DecimalField(decimal_places=6, max_digits=18, verbose_name='Количество сырья'),
        ),
        migrations.AlterField(
            model_name='docrawint',
            name='raw',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.raw', verbose_name='Сырьё'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.product', verbose_name='Готовая продукция'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='raw',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.raw', verbose_name='Сырьё'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='raw_quantity',
            field=models.DecimalField(decimal_places=6, max_digits=18, verbose_name='Количество сырья'),
        ),
    ]
