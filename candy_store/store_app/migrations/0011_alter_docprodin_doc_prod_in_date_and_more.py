# Generated by Django 4.2.9 on 2024-04-06 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0010_docprodout_prod_warehouse_alter_docprodout_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docprodin',
            name='doc_prod_in_date',
            field=models.DateField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='docprodin',
            name='doc_prod_in_num',
            field=models.CharField(max_length=50, unique=True, verbose_name='Номер документа'),
        ),
        migrations.AlterField(
            model_name='docprodin',
            name='product_sum',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True, verbose_name='Сумма ГП'),
        ),
        migrations.AlterField(
            model_name='docprodin',
            name='raw_sum',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True, verbose_name='Сумма сырья'),
        ),
        migrations.AlterField(
            model_name='docprodin',
            name='warehouse_prod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.productwarehouse', verbose_name='Склад ГП'),
        ),
        migrations.AlterField(
            model_name='docprodin',
            name='warehouse_raw',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.rawwarehouse', verbose_name='Склад сырья'),
        ),
        migrations.AlterField(
            model_name='docprodint1',
            name='doc_prod_in',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.docprodin', verbose_name='Номер документа'),
        ),
        migrations.AlterField(
            model_name='docprodint1',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.product', verbose_name='Готовая продукция'),
        ),
        migrations.AlterField(
            model_name='docprodint1',
            name='product_quantity',
            field=models.DecimalField(decimal_places=6, max_digits=18, verbose_name='Количество ГП'),
        ),
        migrations.AlterField(
            model_name='docprodint2',
            name='doc_prod_in',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.docprodin', verbose_name='Номер документа'),
        ),
        migrations.AlterField(
            model_name='docprodint2',
            name='raw',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.raw', verbose_name='Сырьё'),
        ),
        migrations.AlterField(
            model_name='docprodint2',
            name='raw_quantity',
            field=models.DecimalField(decimal_places=6, max_digits=18, verbose_name='Количество сырья'),
        ),
    ]
