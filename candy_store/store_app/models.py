from django.db import models


class Raw(models.Model):
    raw_num = models.CharField(max_length=20, unique=True)
    raw_name = models.CharField(max_length=100)
    raw_cost = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f'ID: {self.id} | {self.raw_name} {self.raw_cost} руб'


class RawWarehouse(models.Model):
    warehouse_raw_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.warehouse_raw_name}'


class RawRest(models.Model):
    raw = models.ForeignKey(Raw, on_delete=models.CASCADE)
    warehouse_raw = models.ForeignKey(RawWarehouse, on_delete=models.CASCADE)
    raw_rest = models.DecimalField(max_digits=18, decimal_places=6, default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['raw', 'warehouse_raw'], name='unique_RawRest')
        ]

    def __str__(self):
        return f'Сырье: {self.raw} | Склад: {self.warehouse_raw} | Остаток: {self.raw_rest}'


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=100)
    supplier_address = models.CharField(max_length=200, null=True, blank=True)
    supplier_phone = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.supplier_name}'


class DocRawIn(models.Model):
    doc_raw_in_num = models.CharField(max_length=50, unique=True, verbose_name='Номер документа')
    doc_raw_in_date = models.DateField(verbose_name='Дата')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='Поставщик')
    raw_warehouse = models.ForeignKey(RawWarehouse, on_delete=models.CASCADE, default=1, verbose_name='Склад')
    doc_raw_in_sum = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, default=0, verbose_name='Сумма')

    def __str__(self):
        return f'№: {self.doc_raw_in_num} от {self.doc_raw_in_date}'


class DocRawInT(models.Model):
    doc_raw_in = models.ForeignKey(DocRawIn, on_delete=models.CASCADE, verbose_name='Номер документа')
    raw = models.ForeignKey(Raw, on_delete=models.CASCADE, verbose_name='Сырьё')
    doc_raw_in_cost = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена сырья')
    doc_raw_in_quantity = models.DecimalField(max_digits=18, decimal_places=6, verbose_name='Количество сырья')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['doc_raw_in', 'raw'], name='unique_RawInT')
        ]

    def __str__(self):
        return f'Документ {self.doc_raw_in} | Сырье: {self.raw} | Цена поставщика: {self.doc_raw_in_cost} | Количество сырья: {self.doc_raw_in_quantity}'


class Product(models.Model):
    product_num = models.CharField(max_length=20, unique=True)
    product_name = models.CharField(max_length=100)
    product_cost = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f'ID: {self.id} | {self.product_name} {self.product_cost} руб'


class ProductWarehouse(models.Model):
    warehouse_prod_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.warehouse_prod_name}'


class ProductRest(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse_prod = models.ForeignKey(ProductWarehouse, on_delete=models.CASCADE)
    product_rest = models.DecimalField(max_digits=18, decimal_places=6, default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['product', 'warehouse_prod'], name='unique_ProductRest')
        ]

    def __str__(self):
        return f'ГП: {self.product} | Склад: {self.warehouse_prod} | Остаток: {self.product_rest}'


class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=200, null=True, blank=True)
    customer_phone = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.customer_name}'


class DocProdOut(models.Model):
    doc_prod_out_num = models.CharField(max_length=50, unique=True, verbose_name='Номер документа')
    doc_prod_out_date = models.DateField(verbose_name='Дата')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Покупатель')
    prod_warehouse = models.ForeignKey(ProductWarehouse, on_delete=models.CASCADE, default=1, verbose_name='Склад')
    doc_prod_out_sum = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, default=0, verbose_name='Сумма')

    def __str__(self):
        return f'№: {self.doc_prod_out_num} от {self.doc_prod_out_date}'


class DocProdOutT(models.Model):
    doc_prod_out = models.ForeignKey(DocProdOut, on_delete=models.CASCADE, verbose_name='Номер документа')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Готовая продукция')
    doc_prod_out_cost = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена ГП')
    doc_prod_out_quantity = models.DecimalField(max_digits=18, decimal_places=6, verbose_name='Количество ГП')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['doc_prod_out', 'product'], name='unique_ProdOutT')
        ]

    def __str__(self):
        return f'Документ: {self.doc_prod_out} | ГП: {self.product} | Цена продажи: {self.doc_prod_out_cost} | Количество ГП: {self.doc_prod_out_quantity}'


class Recipe(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Готовая продукция')
    raw = models.ForeignKey(Raw, on_delete=models.CASCADE, verbose_name='Сырьё')
    raw_quantity = models.DecimalField(max_digits=18, decimal_places=6, verbose_name='Количество сырья')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['product', 'raw'], name='unique_Recipe')
        ]

    def __str__(self):
        return f'ГП: {self.product} | Сырье: {self.raw} | Кол-во: {self.raw_quantity}'


class DocProdIn(models.Model):
    doc_prod_in_num = models.CharField(max_length=50, unique=True, verbose_name='Номер документа')
    doc_prod_in_date = models.DateField(verbose_name='Дата')
    warehouse_raw = models.ForeignKey(RawWarehouse, on_delete=models.CASCADE, verbose_name='Склад сырья')
    warehouse_prod = models.ForeignKey(ProductWarehouse, on_delete=models.CASCADE, verbose_name='Склад готовой продукции')
    raw_sum = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, default=0, verbose_name='Сумма сырья')
    product_sum = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, default=0, verbose_name='Сумма ГП')

    def __str__(self):
        return f'№: {self.doc_prod_in_num} от {self.doc_prod_in_date}'


class DocProdInT1(models.Model):
    doc_prod_in = models.ForeignKey(DocProdIn, on_delete=models.CASCADE, verbose_name='Номер документа')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Готовая продукция')
    product_cost = models.DecimalField(max_digits=7, decimal_places=2, default=0, verbose_name='Цена ГП')
    product_quantity = models.DecimalField(max_digits=18, decimal_places=6, default=0, verbose_name='Количество ГП')
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['doc_prod_in', 'product'], name='unique_ProdInT1')
        ]

    def __str__(self):
        return f'Документ: {self.doc_prod_in} | Готовая продукция: {self.product} | Количество ГП: {self.product_quantity}'


class DocProdInT2(models.Model):
    doc_prod_in = models.ForeignKey(DocProdIn, on_delete=models.CASCADE, verbose_name='Номер документа')
    raw = models.ForeignKey(Raw, on_delete=models.CASCADE, verbose_name='Сырьё')
    raw_cost = models.DecimalField(max_digits=7, decimal_places=2, default=0, verbose_name='Цена сырья')
    raw_quantity = models.DecimalField(max_digits=18, decimal_places=6, default=0, verbose_name='Количество сырья')
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['doc_prod_in', 'raw'], name='unique_ProdInT2')
        ]

    def __str__(self):
        return f'Документ: {self.doc_prod_in} | Сырье: {self.raw} | Количество сырья: {self.raw_quantity}'