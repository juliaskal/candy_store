from django import forms
from .models import *


class RecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].empty_label = 'Не выбрано'
        self.fields['raw'].empty_label = 'Не выбрано'

    class Meta:
        model = Recipe
        fields = ['product', 'raw', 'raw_quantity']


class DocRawInForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['supplier'].empty_label = 'Не выбрано'

    class Meta:
        model = DocRawIn
        fields = ['doc_raw_in_num', 'doc_raw_in_date', 'supplier', 'raw_warehouse']


class DocRawInTabForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['raw'].empty_label = 'Не выбрано'

    class Meta:
        model = DocRawInT
        fields = ['raw', 'doc_raw_in_quantity']


class DocProdInForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['warehouse_raw'].empty_label = 'Не выбрано'
        self.fields['warehouse_prod'].empty_label = 'Не выбрано'

    class Meta:
        model = DocProdIn
        fields = ['doc_prod_in_num', 'doc_prod_in_date', 'warehouse_raw', 'warehouse_prod']


class DocProdInTab1Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].empty_label = 'Не выбрано'

    class Meta:
        model = DocProdInT1
        fields = ['product', 'product_quantity']


class DocProdOutForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].empty_label = 'Не выбрано'
        self.fields['prod_warehouse'].empty_label = 'Не выбрано'

    class Meta:
        model = DocProdOut
        fields = ['doc_prod_out_num', 'doc_prod_out_date', 'customer', 'prod_warehouse']


class DocProdOutTabForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].empty_label = 'Не выбрано'

    class Meta:
        model = DocProdOutT
        fields = ['product', 'doc_prod_out_quantity']