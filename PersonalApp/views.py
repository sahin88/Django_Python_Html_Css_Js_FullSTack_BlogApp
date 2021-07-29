from django.shortcuts import render
from  .models import home_model, about_model,contactinfo_model, post_detail_model,contacts_model
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
# Create your views here.


def home(request):
    home_page_items= home_model.objects.filter(id=1).get()
    return render(request, 'home.html',{'home_page_items': home_page_items})

def about(request):
    about_model_items=about_model.objects.filter(id=1).get()


    return render(request, 'about.html',{'about_model_items':about_model_items})


def contact(request):
    contact_info =contactinfo_model.objects.get(id=1)
    return  render(request, 'contact.html',{'contact_info':contact_info})

class PostListView(ListView):
    model=post_detail_model
    template_name='post.html'
    context_object_name='posts'
    paginate_by=3


    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = self.model.objects.all()
        print("querrry  :",query)
        if query:
            object_list = object_list.filter( )
            
        return object_list


    
def post_detail(request, id):
    query = request.GET.get('q')
    print("query",query)
    if query:
        post_detail_items=post_detail_model.objects.filter(Q(post_text_one__icontains=query) & Q(id=id))
        try:
            post_detail_items=post_detail_items.get()
        except:
            post_detail_items= None
    else:
        post_detail_items= post_detail_model.objects.filter(id=id).get()
    

    about_model_items=about_model.objects.filter(id=1).get()
    last_three_post = post_detail_model.objects.all().order_by('-id')[:3]
    try:
        post_topics= post_detail_items.related_topics.all()
    except Exception as err:
        post_topics=None
        print("err", err)
    
    return render(request, 'post_detail.html',{'post_detail_items':post_detail_items,'about_model_items':about_model_items,'last_three_post':last_three_post,'post_topics':post_topics})

@csrf_protect
def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    name = request.POST.get('name', '')
    phone = request.POST.get('phone', '')
    from_email = request.POST.get('email', '')
    message= message+'\n'+'sender :{}'.format(from_email)
    print("views.py 74",subject, name,phone, from_email)
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ["msahinnihasm@gmail.com"])
            contacts_model.objects.create(name=name,email=from_email,subject=subject,phone_nr=phone,message=message)
        except Exception  as e:
            print("exceptions ", e)
            return HttpResponse('Invalid header found.')
        return HttpResponse('Your message has been succesfully delivered')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')

