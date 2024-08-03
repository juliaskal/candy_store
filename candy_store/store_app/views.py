from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from store_app.models import *
from store_app.forms import *

# from candy_store.store_app.models import RawWarehouse


def main_page(request):
    return render(request, 'main_page.html')

# -------------------------------------------------------


def new_raw(request):
    return render(request, 'new_raw.html')


def new_raw_warehouse(request):
    return render(request, 'new_raw_warehouse.html')


def new_supplier(request):
    return render(request, 'new_supplier.html')


def new_product(request):
    return render(request, 'new_product.html')


def new_prod_warehouse(request):
    return render(request, 'new_prod_warehouse.html')


def new_customer(request):
    return render(request, 'new_customer.html')

# ----------------------------------------------------------


def show_raws(request):
    raws = Raw.objects.all()
    return render(request, "show_raws.html", {"raws": raws})


def show_raw_warehouses(request):
    raw_warehouses = RawWarehouse.objects.all()
    return render(request, "show_raw_warehouses.html", {"raw_warehouses": raw_warehouses})


def show_raw_rests(request):
    rests = RawRest.objects.all()
    return render(request, "show_raw_rests.html", {"rests": rests})


def show_suppliers(request):
    suppliers = Supplier.objects.all()
    return render(request, "show_suppliers.html", {"suppliers": suppliers})


def show_products(request):
    products = Product.objects.all()
    return render(request, "show_products.html", {"products": products})


def show_prod_warehouses(request):
    prod_warehouses = ProductWarehouse.objects.all()
    return render(request, "show_prod_warehouses.html", {"prod_warehouses": prod_warehouses})


def show_customers(request):
    customers = Customer.objects.all()
    return render(request, "show_customers.html", {"customers": customers})


def show_prod_rests(request):
    rests = ProductRest.objects.all()
    return render(request, "show_prod_rests.html", {"rests": rests})


def show_recipes(request):
    recipes = Recipe.objects.all()
    return render(request, "show_recipes.html", {"recipes": recipes})

# ---------------------------------------------------------------------------------------------


def success(request, category):
    if category == 'raw':
        raw_num = request.POST.get('raw_num')
        raw_name = request.POST.get('raw_name')
        raw_cost = request.POST.get('raw_cost')

        r = Raw(raw_num=raw_num, raw_name=raw_name, raw_cost=raw_cost)
        r.save()

        whs = RawWarehouse.objects.all()
        for wh in whs:
            RawRest(raw=r, warehouse_raw=wh, raw_rest=0).save()

    if category == 'raw_warehouse':
        warehouse_raw_name = request.POST.get('warehouse_raw_name')

        wh = RawWarehouse(warehouse_raw_name=warehouse_raw_name)
        wh.save()

        rs = Raw.objects.all()
        for r in rs:
            RawRest(raw=r, warehouse_raw=wh, raw_rest=0).save()

    if category == 'supplier':
        supplier_name = request.POST.get('supplier_name')
        supplier_address = request.POST.get('supplier_address')
        supplier_phone = request.POST.get('supplier_phone')
        element = Supplier(supplier_name=supplier_name, supplier_address=supplier_address, supplier_phone=supplier_phone)
        element.save()

    if category == 'product':
        product_num = request.POST.get('product_num')
        product_name = request.POST.get('product_name')
        product_cost = request.POST.get('product_cost')

        p = Product(product_num=product_num, product_name=product_name, product_cost=product_cost)
        p.save()

        whs = ProductWarehouse.objects.all()
        for wh in whs:
            ProductRest(product=p, warehouse_prod=wh, product_rest=0).save()

    if category == 'prod_warehouse':
        warehouse_prod_name = request.POST.get('warehouse_prod_name')

        wh = ProductWarehouse(warehouse_prod_name=warehouse_prod_name)
        wh.save()

        ps = Product.objects.all()
        for p in ps:
            ProductRest(product=p, warehouse_prod=wh, product_rest=0).save()

    if category == 'customer':
        customer_name = request.POST.get('customer_name')
        customer_address = request.POST.get('customer_address')
        customer_phone = request.POST.get('customer_phone')
        element = Customer(customer_name=customer_name, customer_address=customer_address, customer_phone=customer_phone)
        element.save()

    return render(request, "success.html")

# -----------------------------------------------------


def new_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/new_recipe/')
    else:
        form = RecipeForm()

    rec = Recipe.objects.all()
    data = {'rec': rec, 'form': form}

    return render(request, 'new_recipe.html', data)


def new_doc_raw_in(request):
    if request.method == 'POST':
        form = DocRawInForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/new_doc_raw_in_tab/')
    else:
        form = DocRawInForm()

    data = {'form': form}

    return render(request, 'new_doc_raw_in.html', data)


def new_doc_raw_in_tab(request):
    doc_raw_in = DocRawIn.objects.last()
    if request.method == 'POST':
        form = DocRawInTabForm(request.POST)
        if form.is_valid():
            tab = form.save(commit=False)
            tab.doc_raw_in = doc_raw_in
            tab.doc_raw_in_cost = tab.raw.raw_cost
            tab.save()

            r = tab.raw
            wh = doc_raw_in.raw_warehouse
            q = tab.doc_raw_in_quantity
            rawrest = RawRest.objects.get(raw=r, warehouse_raw=wh)
            rawrest.raw_rest = rawrest.raw_rest + q
            rawrest.save()

            s = tab.doc_raw_in_cost * tab.doc_raw_in_quantity
            doc_raw_in.doc_raw_in_sum = doc_raw_in.doc_raw_in_sum + s
            doc_raw_in.save()

            return HttpResponseRedirect('/new_doc_raw_in_tab/')
    else:
        form = DocRawInTabForm()

    data = {'form': form}

    return render(request, 'new_doc_raw_in_tab.html', data)


def show_doc_raw_in(request):
    docs = DocRawIn.objects.all()
    return render(request, "show_doc_raw_in.html", {"docs": docs})


def show_selected_doc_raw_in(request, id):
    doc = DocRawIn.objects.get(id=id)
    tabs = DocRawInT.objects.filter(doc_raw_in=doc)

    data = {'doc': doc, 'tabs': tabs}

    return render(request, 'show_selected_doc_raw_in.html', data)


def new_doc_prod_in(request):
    if request.method == 'POST':
        form = DocProdInForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/new_doc_prod_in_tab1/')
    else:
        form = DocProdInForm()

    data = {'form': form}

    return render(request, 'new_doc_prod_in.html', data)


def new_doc_prod_in_tab1(request):
    doc_prod_in = DocProdIn.objects.last()
    if request.method == 'POST':
        form = DocProdInTab1Form(request.POST)
        if form.is_valid():
            tab = form.save(commit=False)  # создаем экземпляр объекта для DocProdInT1 с готовой продукцией
            tab.doc_prod_in = doc_prod_in
            tab.product_cost = tab.product.product_cost
            tab.save()

            p = tab.product
            raws = Recipe.objects.filter(product=p)
            r_wh = doc_prod_in.warehouse_raw
            p_quant = tab.product_quantity

            for r in raws:
                quant_raw = p_quant * r.raw_quantity
                r_rest = RawRest.objects.get(raw=r.raw, warehouse_raw=r_wh)
                if r_rest.raw_rest < quant_raw:
                    return HttpResponseBadRequest("Недостаточно сырья на складе")

            for r in raws:
                quant_raw = p_quant * r.raw_quantity
                r_rest = RawRest.objects.get(raw=r.raw, warehouse_raw=r_wh)
                r_rest.raw_rest = r_rest.raw_rest - quant_raw
                r_rest.save()
                r_cost = r.raw.raw_cost
                if DocProdInT2.objects.filter(doc_prod_in=doc_prod_in, raw=r.raw).exists():
                    t2 = DocProdInT2.objects.get(doc_prod_in=doc_prod_in, raw=r.raw)
                    t2.raw_quantity = t2.raw_quantity + quant_raw
                    t2.save()
                else:
                    DocProdInT2(doc_prod_in=doc_prod_in, raw=r.raw, raw_cost=r_cost, raw_quantity=quant_raw).save()

                sum_raw = r_cost * quant_raw
                doc_prod_in.raw_sum = doc_prod_in.raw_sum + sum_raw
                doc_prod_in.save()

            p_wh = doc_prod_in.warehouse_prod
            prodrest = ProductRest.objects.get(product=p, warehouse_prod=p_wh)
            prodrest.product_rest = prodrest.product_rest + p_quant
            prodrest.save()

            sum_prod = tab.product_cost * tab.product_quantity
            doc_prod_in.product_sum = doc_prod_in.product_sum + sum_prod
            doc_prod_in.save()

            return HttpResponseRedirect('/new_doc_prod_in_tab1/')
    else:
        form = DocProdInTab1Form()

    data = {'form': form}

    return render(request, 'new_doc_prod_in_tab1.html', data)


def show_doc_prod_in(request):
    docs = DocProdIn.objects.all()
    return render(request, "show_doc_prod_in.html", {"docs": docs})


def show_selected_doc_prod_in(request, id):
    doc = DocProdIn.objects.get(id=id)
    prods = DocProdInT1.objects.filter(doc_prod_in=doc)
    raws = DocProdInT2.objects.filter(doc_prod_in=doc)

    data = {'doc': doc, 'prods': prods, 'raws': raws}

    return render(request, 'show_selected_doc_prod_in.html', data)


def new_doc_prod_out(request):
    if request.method == 'POST':
        form = DocProdOutForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/new_doc_prod_out_tab/')
    else:
        form = DocProdOutForm()

    data = {'form': form}

    return render(request, 'new_doc_prod_out.html', data)


def new_doc_prod_out_tab(request):
    doc_prod_out = DocProdOut.objects.last()
    if request.method == 'POST':
        form = DocProdOutTabForm(request.POST)
        if form.is_valid():
            tab = form.save(commit=False)
            tab.doc_prod_out = doc_prod_out
            tab.doc_prod_out_cost = tab.product.product_cost
            tab.save()

            p = tab.product
            wh = doc_prod_out.prod_warehouse
            q = tab.doc_prod_out_quantity

            p_rest = ProductRest.objects.get(product=p, warehouse_prod=wh)
            if p_rest.product_rest < q:
                d = DocProdOutT.objects.get(doc_prod_out=doc_prod_out, product=p)
                d.delete()
                return HttpResponseBadRequest("Недостаточно готовой продукции на складе")
            else:
                p_rest.product_rest = p_rest.product_rest - q
                p_rest.save()

            s = tab.doc_prod_out_cost * tab.doc_prod_out_quantity
            doc_prod_out.doc_prod_out_sum = doc_prod_out.doc_prod_out_sum + s
            doc_prod_out.save()

            return HttpResponseRedirect('/new_doc_prod_out_tab/')
    else:
        form = DocProdOutTabForm()

    data = {'form': form}

    return render(request, 'new_doc_prod_out_tab.html', data)


def show_doc_prod_out(request):
    docs = DocProdOut.objects.all()
    return render(request, "show_doc_prod_out.html", {"docs": docs})


def show_selected_doc_prod_out(request, id):
    doc = DocProdOut.objects.get(id=id)
    tabs = DocProdOutT.objects.filter(doc_prod_out=doc)

    data = {'doc': doc, 'tabs': tabs}

    return render(request, 'show_selected_doc_prod_out.html', data)
