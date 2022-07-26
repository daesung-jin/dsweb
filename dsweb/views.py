from django.shortcuts import render, redirect
from .models import Inquiry
from .forms import InquiryForm
from django.utils import timezone


def index(request):
    inquiry_list = Inquiry.objects.order_by('-create_date')
    context = {'inquiry_list': inquiry_list}
    return render(request, 'dsweb/inquiry_list.html', context)


def detail(request, inquiry_id):
    inquiry = Inquiry.objects.get(id=inquiry_id)
    context = {'inquiry': inquiry}
    return render(request, 'dsweb/inquiry_detail.html', context)


def inquiry_create(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.create_date = timezone.now()
            inquiry.save()
            return redirect('dsweb:index')
    else:
        form = InquiryForm()
    context = {'form': form}
    return render(request, 'dsweb/inquiry_form.html', context)


def main(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.create_date = timezone.now()
            inquiry.save()
            return redirect('dsweb:main')
    else:
        form = InquiryForm()
    context = {'form': form}
    return render(request, 'dsweb/main.html', context)
