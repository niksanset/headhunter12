from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import TemplateView,ListView,DetailView,DeleteView,UpdateView,CreateView
from headhunter_app.models import *
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout




class StartPageView(TemplateView):
    template_name = 'headhunter_app/start_page.html'


class UserLoginView(LoginView):
    template_name = 'headhunter_app/login.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('start_page')

def user_logout(request):
    logout(request)
    return redirect('start_page')

class SignUpView(CreateView):
    template_name = 'headhunter_app/sign_up.html'
    
    form_class = UserCreationForm
    success_url = reverse_lazy('start_page')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('start_page')
        return super().get(request, *args, **kwargs)
    
@login_required
def list_view(request):
    resumes = Resume.objects.all()
    vacancy = Vacancy.objects.all()

    context = {'vacancy_list': vacancy}
    if request.user.is_staff:
        context = {'resume_list': resumes }
    return render(request, 'headhunter_app/list.html',
                  context=context)


@login_required
def detail_view(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    context = {'vacancy': vacancy}
    if request.user.is_staff:
        resume = get_object_or_404(Resume, pk=pk)
        context = {'resume': resume}
    return render(request, 'headhunter_app/detail.html', context)


class VacancyCreateView(CreateView):
    template_name = 'headhunter_app/vacancy_create.html'
    model = Vacancy
    fields = ('__all__')
    success_url = reverse_lazy('list')

class ResumeCreateView(CreateView):
    template_name = 'headhunter_app/resume_create.html'
    model = Resume
    fields = ('__all__')
    success_url = reverse_lazy('list')

class VacancyUpdateView(UpdateView):
    template_name = 'headhunter_app/vacancy_update.html'
    model = Vacancy
    fields = ('__all__')
    success_url = reverse_lazy('list')
class ResumeUpdateView(UpdateView):
    template_name = 'headhunter_app/resume_update.html'
    model = Resume
    fields = ('__all__')
    success_url = reverse_lazy('list')

class VacancyDeleteView(DeleteView):
    template_name = 'headhunter_app/vacancy_delete.html'
    model = Vacancy
    success_url = reverse_lazy('list')
class ResumeDeleteView(DeleteView):
    template_name = 'headhunter_app/resume_delete.html'
    model = Resume
    success_url = reverse_lazy('list')