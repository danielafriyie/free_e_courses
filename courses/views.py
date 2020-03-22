from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.core.paginator import Paginator
from django.contrib import messages as msg
from django.contrib.auth.decorators import login_required

from .models import ECourses, Contact


class IndexView(View):

    def get(self, request):
        courses = ECourses.objects.order_by('-date').all()
        paginator = Paginator(courses, 6)
        page = request.GET.get('page')
        paginator_pages = paginator.get_page(page)
        context = {
            'paginator_pages': paginator_pages
        }
        return render(request, 'courses/index.html', context)


def course_detail(request, pk, name):
    course = get_object_or_404(ECourses, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})


def search_course(request):
    context = {}
    if 'search' in request.GET:
        search = request.GET['search']
        search_result = ECourses.objects.order_by('title').filter(title__icontains=search).all()
        if search_result:
            paginator = Paginator(search_result, 6)
            page = request.GET.get('page')
            paginator_pages = paginator.get_page(page)
            context['paginator_pages'] = paginator_pages
        else:
            msg.info(request, 'What you searched for does not exist!')
            return redirect('courses:search')

    return render(request, 'courses/search_page.html', context)


def category_filter(request):
    context = {}
    if 'category' in request.GET:
        category = request.GET['category']
        search_result = ECourses.objects.order_by('category').filter(category__icontains=category)
        if search_result:
            paginator = Paginator(search_result, 6)
            page = request.GET.get('page')
            paginator_pages = paginator.get_page(page)
            context['paginator_pages'] = paginator_pages
        else:
            # msg.info(request, 'What you searched for does not exist!')
            return redirect('courses:category')
    return render(request, 'courses/category_filter.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        sub = request.POST['subject']
        message = request.POST['message']
        Contact.objects.create(
            name=name,
            email=email,
            subject=sub,
            message=message
        )

        msg.success(request, 'Thanks for getting in touch with us!')
        return redirect('courses:contact')

    return render(request, 'courses/contact.html')


def terms_condition(request):
    return render(request, 'courses/terms_condition.html')


def privacy(request):
    return render(request, 'courses/privacy_policy.html')


@login_required
def add_course(request):
    user = request.user
    if user.is_superuser:
        if request.method == 'POST':
            image = bytearray(request.FILES['image']),
            title = request.POST['title']
            des = request.POST['desc']
            cat = request.POST['cat']
            torrent = bytearray(request.FILES['torrent'])

            ECourses.objects.create(
                image_binary=image,
                title=title,
                description=des,
                category=cat,
                torrent_binary=torrent
            )
            msg.success(request, 'Course added successfully')
            return redirect('courses:add_course')
        return render(request, 'courses/add_course.html')
