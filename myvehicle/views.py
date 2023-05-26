from django.shortcuts import render,get_object_or_404,redirect
from .models import Management_Data
from .forms import mydata,PostBlogForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import RegistrationForm

class index(CreateView):
    def get(self,request):
        return render(request,'myapp/index.html')
        
class add_data(SuccessMessageMixin,CreateView):
    form_class=mydata
    template_name='myapp/add_data.html'
    success_message = 'Data has been successfuly !!'
    success_url = reverse_lazy('view_data')

class view_data(CreateView):
    def get(self,request):
        data=Management_Data.objects.all()
        res={"data":data}
        return render(request,'myapp/view.html',res)

class main_data(CreateView):
    def get(self,request,pk):
        post_result=get_object_or_404(Management_Data,pk=pk)
        content={'post':post_result}
        return render(request,'myapp/post_detail.html',content)

class post_delete(CreateView):
    def get(self,request,pk):
        post_data=get_object_or_404(Management_Data,pk=pk)
        post_data.delete()
        messages.success(request,' Delete has been Successfuly')
        return redirect('view_data')
    
    def post(self,request,pk):
        post_data=get_object_or_404(Management_Data,pk=pk)
        post_data.delete()
        messages.success(request,' Delete has been Successfuly')
        return redirect('view_data')



class post_edit(CreateView):
    def get(self,request,pk):
        post_data=get_object_or_404(Management_Data,pk=pk)
        if request.method=='POST':
            form_data=PostBlogForm(request.POST,instance=post_data)
            if form_data.is_valid():
                form_data.save()
                messages.success(request,' update data Successfuly')
                return redirect('view_data')
        else:
            form_data=PostBlogForm(instance=post_data)
        return render(request,'myapp/post_edit.html',{'form_data':form_data})
    
    def post(self,request,pk):
        post_data=get_object_or_404(Management_Data,pk=pk)
        if request.method=='POST':
            form_data=PostBlogForm(request.POST,instance=post_data)
            if form_data.is_valid():
                form_data.save()
                messages.success(request,' update data Successfuly')
                return redirect('view_data')
        else:
            form_data=PostBlogForm(instance=post_data)
        return render(request,'myapp/post_edit.html',{'form_data':form_data})



class register(CreateView):
    def get(self,request):
        if request.method=='GET':
            form=RegistrationForm()
            return render(request,'registers.html',{'form':form})
    def post(self,request):
        if request.method=='POST':
            form=RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                username=form.cleaned_data.get('username')
                messages.success(request,'Account has been Successfuly created for '+username)
                return redirect('home')
            else:
                return render(request,'registers.html',{'form':form})
        return render(request,'registers.html',{'form':form})