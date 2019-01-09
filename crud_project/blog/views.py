from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Comment, Product
from .forms import PostForm, CommentForm, ProductForm, CreateUserForm
# Create your views here.
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm 
from django.core.urlresolvers import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.core.urlresolvers import reverse_lazy # generic view에서는 reverse_lazy를 사용한다.



#create
@login_required
def post_new(request): 
    if request.method == 'POST':
        Postform=PostForm(request.POST)
        Productform=ProductForm(request.POST)
        if Postform.is_valid():
            
            post = Postform.save()
            product = Productform.save()
            
            return HttpResponse('새 글 생성 완료')

    else:
        Postform = PostForm()
        Productform = ProductForm()
    
    return render(request, 'blog/post_new.html', {
        'Productform':Productform,
        'Postform':Postform,
    })
    
#read
def post_detail(request, post_id): #두 번째 파라미터는 패턴명post_id
    
    post = Post.objects.get(id = post_id) #클래스명.Objects.get ->하나 가져올거니까
    form = CommentForm()
    # Productform = ProductForm

    # print(post.comment_set.all())
    return render(request, 'blog/post_detail.html',{
        "post":post,
        "form":form,
        # "ProductForm":ProductForm,
    })




# #edit
# @login_required
# def post_edit(request, post_id):
#     post = get_object_or_404(Post, id=post_id) #모델, id를 적어
#     if request.method == 'POST':
#         form=PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save()
#             return HttpResponse('수정완료')
#             # return redirect(po)

#     else: #edit: 빈폼이 아니고 그 객체 가져왕야돼
#         form = PostForm(instance=post)
    
#     return render(request, 'blog/post_new.html', {
#         'form':form,
#     })

#edit
@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id) #모델, id를 적어
    product = get_object_or_404(Product, post_id=post_id) 
    if request.method == 'POST':
        Postform=PostForm(request.POST, instance=post)
        Productform=ProductForm(request.POST, instance=product)
        if Postform.is_valid():
            product = Productform.save()
            post = Productform.save()
            
            return HttpResponse('수정완료')
            # return redirect(po)

    else: #edit: 빈폼이 아니고 그 객체 가져왕야돼
        Postform = PostForm(instance=post)
        Productform = ProductForm(instance=product)
    
    return render(request, 'blog/post_new.html', {
        'Productform':Productform,
        'Postform':Postform,
    })


#post_delete
@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return render(request,'blog/post_index.html')





def comment_new(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit = False)
        comment.post = post
        comment = form.save()

    return redirect(post)

@login_required
def comment_delete(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect(comment.post)

def post_index(request):
    post_all = Post.objects.all()

    return render(request, 'blog/post_index.html',{
        "post_all": post_all,
    })


def post_main(request):
    post_all = Post.objects.all()

    return render(request, 'blog/post_main.html',{
        "post_all": post_all,
    })



def post_login_done(request):

    return render(request, 'blog/post_login_done.html',{
        
    })





class IndexView(View): #로그인 하지 않은 상태
    def get(self, request, *args, **kwargs):
        context = {'parm1': 'hello', 'parm2': 'django', 'auth': request.user.is_authenticated}
        print(request.user)
        return render(request, 'index.html', context=context)


def profile(request): #로그인 한 상태
    if not request.user.is_authenticated:
        data = {'username': request.user, 'is_authenticated': request.user.is_authenticated}
    else:
        data = {'last_login': request.user.last_login, 'username': request.user.username,
                'password': request.user.password, 'is_authenticated': request.user.is_authenticated}
    return render(request, 'profile.html', context={'data': data})



class CreateUserView(CreateView): # generic view중에 CreateView를 상속받는다.
    template_name = 'registration/signup.html' # 템플릿은?
    form_class =  CreateUserForm # 푸슨 폼 사용? >> 내장 회원가입 폼을 커스터마지징 한 것을 사용하는 경우
    # form_class = UserCreationForm >> 내장 회원가입 폼 사용하는 경우
    success_url = reverse_lazy('blog:create_user_done') # 성공하면 어디로?

class RegisteredView(TemplateView): # generic view중에 TemplateView를 상속받는다.
    template_name = 'registration/sign_done.html' # 템플릿은?




def permission_denied(request):
    return render(request, 'registration/permission_denied.html',{
        
    })


