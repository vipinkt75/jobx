from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from. models import form ,jobList
from .forms import ApplyForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.shortcuts import render
from django.core.mail import EmailMessage
from email.mime.base import MIMEBase
from email import encoders
import os
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from django.views import View




class Index(LoginRequiredMixin, ListView):
    model = jobList
    template_name = "index.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        location = self.request.GET.get('location')

        if category:
            queryset = queryset.filter(name=category)
        if location:
            queryset = queryset.filter(location=location)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = jobList.objects.values_list('name', flat=True).distinct()
        context['locations'] = jobList.objects.values_list('location', flat=True).distinct()
        return context
    

class Form(LoginRequiredMixin, CreateView):
    model= form
    template_name = "contact.html"
    fields = "__all__"
    success_url =reverse_lazy("web:contact")


class jobLists(LoginRequiredMixin, ListView):
    model = jobList
    template_name = "job-list.html"




class about(LoginRequiredMixin, TemplateView):
    template_name = "about.html"


class category(LoginRequiredMixin, TemplateView):
    template_name = "category.html"

class testimonial(LoginRequiredMixin, TemplateView):
    template_name = "testimonial.html"

class postjob(LoginRequiredMixin, CreateView):
    model = jobList
    template_name = "post_job.html"
    fields = "__all__"



class SearchListView(LoginRequiredMixin, ListView):
    model = jobList
    template_name = "search.html"
    context_object_name = "job_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        location = self.request.GET.get('location')

        if category:
            queryset = queryset.filter(name=category)
        if location:
            queryset = queryset.filter(location=location)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = jobList.objects.values_list('name', flat=True).distinct()
        context['locations'] = jobList.objects.values_list('location', flat=True).distinct()
        return context
    

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        location = self.request.GET.get('location')
        keyword = self.request.GET.get('keyword')

        if category:
            queryset = queryset.filter(name=category)
        if location:
            queryset = queryset.filter(location=location)
        if keyword:
            queryset = queryset.filter(Q(name__icontains=keyword) | Q(location__icontains=keyword))

        return queryset
    


# class JobDetailView(DetailView):
#     model = jobList
#     context_object_name = "job_detail"
#     template_name = "job-detail.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['apply_form'] = ApplyForm(initial={'job': self.object.name})  # Pre-fill job field
#         return context

#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()

#         apply_form = ApplyForm(request.POST, request.FILES)
#         if apply_form.is_valid():
#             apply_form.instance.job = self.object.name
#             application = apply_form.save()

#             # Construct email content
#             email_content = render_to_string(
#                 "email_templates/email_service.html",
#                 {
#                     'job': application.job,
#                     'name': application.name,
#                     'email': application.email,
                    
#                 },
#             )

#             # Send email
#             send_mail(
#                 "Nayel service enquire",
#                 "",  
#                 application.email,  
#                 ["vipinkt13@gmail.com"],
#                 html_message=email_content,
#                 fail_silently=False,
#             )

#             context = self.get_context_data(**kwargs)
#             return render(request, self.template_name, context)

#         context = self.get_context_data(**kwargs)
#         return render(request, self.template_name, context)



# class JobDetailView(DetailView):
#     model = jobList
#     context_object_name = "job_detail"
#     template_name = "job-detail.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['apply_form'] = ApplyForm(
#             initial={'job': self.object.name, 'sender_email': self.object.sender_email}
#         )
#         return context

#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()

#         apply_form = ApplyForm(request.POST, request.FILES)
#         if apply_form.is_valid():
#             apply_form.instance.job = self.object.name
#             application = apply_form.save()

#             # Construct email content
#             email_content = render_to_string(
#                 "email_templates/email_service.html",
#                 {
#                     'job': application.job,
#                     'name': application.name,
#                     'email': application.email,
#                 },
#             )

#             # Send email with dynamically determined sender email
#             send_mail(
#                 "Nayel service enquire",
#                 "",  
#                 self.object.sender_email,
#                 [application.email],
#                 html_message=email_content,
#                 fail_silently=False,
#             )
           
#             context = self.get_context_data(**kwargs)
#             return render(request, self.template_name, context)

#         context = self.get_context_data(**kwargs)
#         return render(request, self.template_name, context)


        

class JobDetailView(LoginRequiredMixin, DetailView):
    model = jobList
    context_object_name = "job_detail"
    template_name = "job-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['apply_form'] = ApplyForm(
            initial={'job': self.object.name, 'sender_email': self.object.sender_email}
        )
        return context


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        apply_form = ApplyForm(request.POST, request.FILES)
        if apply_form.is_valid():
            application = apply_form.save()

            # Construct email content
            email_content = render_to_string(
                "email_templates/email_service.html",
                {
                    'job': application.job,
                    'name': application.name,
                    'email': application.email,
                    'website': application.website,
                },
            )

            # Create an EmailMessage object
            email = EmailMessage(
                "job details",
                email_content,
                application.email,
                [self.object.sender_email],  # Send to the specified sender_email
            )

            # Attach the file
            if application.file:
                file_path = application.file.path
                file_name = os.path.basename(file_path)
                with open(file_path, 'rb') as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename= {file_name}')
                email.attach(part)

            # Send the email
            email.send(fail_silently=False)

            context = self.get_context_data(**kwargs)
            return render(request, self.template_name, context)

        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)
    



class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = UserProfile.objects.get_or_create(user=self.request.user)[0]
        return context

class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'profile_update.html'
    success_url =reverse_lazy("web:profile")  