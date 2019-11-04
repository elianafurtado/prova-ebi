from django.shortcuts import render, redirect
from .models import Company, ServiceOrder
from .forms import CompanyForm

def list_companies(request):
    for_search = request.GET.get('pesquisa', None)

    if for_search:
        companies = Company.objects.all()
        companies = companies.filter(name=for_search)
    else:
        companies = Company.objects.all()
    return render(request,'companies.html',{'companies':companies})

def create_company(request):
    form = CompanyForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_companies')

    return render(request,'company-form.html',{'form':form})

def update_company(request, id):
    company = Company.objects.get(id=id)
    form = CompanyForm(request.POST or None, instance=company)

    if form.is_valid():
        form.save()
        return redirect('list_companies')

    return render(request,'company-form.html',{'form':form, 'company':company})

def delete_company(request, id):
    company = Company.objects.get(id=id)

    if request.method == 'POST':
        company.delete()
        return redirect('list_companies')

    return render(request,'company-delete-confirm.html',{'company':company})

def list_service_orders(request, id):
    services_orders = ServiceOrder.objects.all()
    services_orders = services_orders.filter(company_id=id)

    return render(request,'service-orders.html',{'services_orders':services_orders})

def list_services(request, id):
    company = Company.objects.get(id=id)
    services = company.services.all()

    return render(request,'service-orders.html',{'services_orders':services_orders})
