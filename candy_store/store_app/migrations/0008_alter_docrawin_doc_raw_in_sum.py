# Generated by Django 4.2.9 on 2024-04-06 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0007_docrawin_raw_warehouse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docrawin',
            name='doc_raw_in_sum',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True, verbose_name='Сумма'),
        ),
    ]
