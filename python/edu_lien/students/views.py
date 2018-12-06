from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView,FormView
from django.views.generic.list import ListView
from django.contrib.auth import authenticate,login
from courses.models import Course
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CourseEnrollForm
# Create your views here.


class StudentRegisterationView(CreateView):
    # 需要渲染的模板位置
    template_name = 'student/register.html'
    # form_class 必须是ModelForm 对象，这里用的是django内置的建立新用户的表单
    form_class = UserCreationForm
    # 成功后跳转的url，通过反相解析获取url
    success_url = reverse_lazy('course_list')

    # 重写form_valid方法，使用户在成功注册后就登录
    def form_valid(self, form):
        result = super(StudentRegisterationView,self).form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'],password = cd['password1'])
        login(self.request,user)
        return result

class StudentEnrollCourseView(LoginRequiredMixin,FormView):
    # 设置course属性用于保存学生选择的课程对象
    # 当表单验证通过的时候，取得当前用户设置多对多的关系，让偶调用父类的方法保存数据
    course = None
    form_class = CourseEnrollForm

    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user)
        return super(StudentEnrollCourseView, self).form_valid(form)

    def get_success_url(self):
        # TODO
        return reverse_lazy('student_course_list')

class StudentCourseListView(LoginRequiredMixin,ListView):
    '''这个视图是用来给学生展示所有的课程'''
    model = Course
    template_name = 'student/course_list.html'

    # 重写get_queryset 方法，过滤出当前学生所选课程
    def get_queryset(self):
        qs = super(StudentCourseListView, self).get_queryset()
        return qs.filter(students__in=[self.request.user])

class StudentCourseDetailView(DetailView):
    '''用于向学生展示他们选的课程和章节'''
    model = Course
    template_name = 'student/course_detail.html'

    def get_queryset(self):
        qs = super(StudentCourseDetailView, self).get_queryset()
        return qs.filter(students__in=[self.request.user])

    def get_context_data(self, **kwargs):
        context = super(StudentCourseDetailView, self).get_context_data(**kwargs)
        course = self.object()

        if 'moduel_id' in self.kwargs:
            context['module'] = course.modules.get(id=self.kwargs['module_id'])
        else:
            context['module'] = course.modules.all()[0]

        return context




