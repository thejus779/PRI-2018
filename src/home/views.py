from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,ListView,DetailView, CreateView
from django.http import HttpResponse
from django.views import View
from django.db.models import Q
import json
import requests
from .models import Image
from .forms import ImageForm
from .forms import PostPartCreateForm, QueryCaseBaseForm,PartRequestCreateForm
from .models import Parts
from django.shortcuts import render, redirect
from notif.forms import BuyRequest
from core.models import Profile
from notif.models import Notification
from django.contrib import messages

@login_required(login_url='/login/')
def create_parts(request):
    if request.method == 'POST':
        form = PostPartCreateForm(request.POST, request.FILES)
        errors = None
        print(form)
        if form.is_valid():
            if request.user.is_authenticated():
                instance = form.save(commit=False)
                # customize and signals
                #  pre save
                instance.owner = request.user
                instance.save()
                # file = form.cleaned_data['image']
                # post save
                messages.success(request, 'Post created successfully')
                return redirect('post')
            else:
                return HttpResponseRedirect("/login/")
        if form.errors:
            errors = form.errors

        template_name = 'post.html'
        context = {"form": form, "errors": errors
                   }

        return render(request, template_name, context)

    else:
        template_name = 'post.html'
        context = {
                   }

        return render(request, template_name, context)

# class PartCreateView(LoginRequiredMixin, CreateView):
#     form_class = PostPartCreateForm
#     login_url = '/login/'
#     template_name = 'post.html'
#     success_url = 'home'
#
#     def form_valid(self, form):
#         print('Form is valid')
#         instance = form.save(commit=False)
#         instance.owner = self.request.user
#
#         return super(PartCreateView, self).form_valid(form)


def showimage(request):
    lastimage = Image.objects.last()

    imagefile = lastimage.imagefile

    form = ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context = {'imagefile': imagefile,
               'form': form
               }

    return render(request, 'Blog/images.html', context)


class PartsDetailsView(DetailView):


    # template_name = 'details.html'
    queryset = Parts.objects.all()
    print("")
    # filter(catergory__iexact='SWEET')
    # def get_context_data(self, **kwargs):
    #     print("test is success")


def display_buy_part(request,slug):

    if request.method == 'POST':
        if request.POST.get("login"):
            return redirect('login')

        else:
            form = BuyRequest(request.POST, request.FILES)
            errors = None
            print(form)
            if form.is_valid():
                print("Form action working")
                if request.user.is_authenticated():
                    instance = form.save(commit=False)
                    # custoize and signals
                    #  pre save
                    instance.owner = request.user
                    instance.save()
                    # file = form.cleaned_data['image']
                    # post save
                    print("INSIDE FORM")
                    return redirect('home')
            if form.errors:
                print("ERROR  IS ")
                errors = form.errors
            #
            print(errors)
            template_name = 'details.html'
            queryset = Parts.objects.get(slug__iexact=slug)
            if request.user.is_authenticated():
                profile = Profile.objects.get(user_id=request.user.id)
            else:
                profile = {""}
            context = {"form": form, "errors": errors, "part": queryset
                , "profile": profile}
            # print(context)
            # print(slug)
            return render(request, template_name, context)
    else:
        template_name = 'details.html'
        queryset = Parts.objects.get(slug__iexact=slug)
        if request.user.is_authenticated():
            profile = Profile.objects.get(user_id=request.user.id)
        else:
            profile = {""}
        context = {"part": queryset
            , "profile": profile}
        print(context)
        print(slug)
        return render(request, template_name, context)


def get_all_products(request):
    template_name = 'index.html'
    if request.user.is_authenticated:
        queryset = Parts.objects.filter(~Q(owner=request.user))
    else:
        queryset = Parts.objects.all()
    context = {"parts": queryset}
    print(context)

    return render(request, template_name, context)


@login_required(login_url='/login/')
def update_part(request,slug):

    if request.method == 'POST':

        form = PostPartCreateForm(request.POST or None, request.FILES or None, instance=request.user)
        # form = PostPartCreateForm(request.POST, request.FILES)
        part = Parts.objects.get(slug=slug)
        print(' form is')
        print(form)
        if form.is_valid():
            if request.user.is_authenticated():
                # edit = form.save(commit=False)
                # edit.save()
                # instance = form.save(commit=False)
                # custoize and signals
                #  pre save
                # instance.save()
                part.name = form.cleaned_data.get('name')
                part.category = form.cleaned_data.get('category')
                part.manufacturer = form.cleaned_data.get('manufacturer')
                part.modelName = form.cleaned_data.get('modelName')
                part.manufacturingYear = form.cleaned_data.get('manufacturingYear')
                part.usedDuration = form.cleaned_data.get('usedDuration')
                part.description = form.cleaned_data.get('description')
                if form.cleaned_data.get('images'):
                    part.images = form.cleaned_data.get('images')
                else:
                    part.images = part.images
                # if User.objects.filter(username=user_form.cleaned_data.get('username')).exists():
                # messages.error("Username already exists")
                # # raise forms.ValidationError(u'Username "%s" is not available.' % newusername)
                # else:
                #     if User.objects.filter(username=user_form.cleaned_data.get('email')).exists():
                #         messages.error("Username already exists")
                #     else:
                # user.username = user_form.cleaned_data.get('username')
                # user.email = user_form.cleaned_data.get('email')
                part.save()
                # user_profile.save()
                print(part.description)
                messages.success(request, 'Your part was successfully updated!')
                return HttpResponseRedirect(request.path_info)
        else:
            # messages.error(request, 'Update failed, try again.')
            return render(request, 'updatepost.html', {'form':form})


    else:
        template_name = 'updatepost.html'
        part = Parts.objects.get(slug=slug)
        context = {'part': part}
        return render(request, template_name, context)


def filter_section(request):
    return render(
        request,
        'filter.html'
    )

def search(request):
    """Our Search form easy thanks Django ORM and title__contains"""
    # gigs = Gig.objects.filter(title__contains=request.GET.get('title'))

    return render(
        request,
        'home.html',{}
        # {'gigs': gigs, 'media_url': MEDIA_URL}
    )

#@login_required(login_url=login_selection)
def search_results(request):
    import logging
    logging.basicConfig(filename='formlog.log', level=logging.DEBUG)
    # the request is a normal query
    if request.method == 'POST':
        form = QueryCaseBaseForm(request.POST)
        #profile = Profile.objects.get(user=request.user)

        logging.debug('form=%s', form)

        if form.is_valid():
            print('form issssss')
            print(form)

            print(form.data["drop_category"])

            print('data abpce')
            logging.debug('form is valid')

            payload = json.dumps({
                "Category": form.data["drop_category"],
                "Model": form.data["drop_model"],
                "Link": "_unknown_",
                # "Continent": form.data["drop_continent"],
                "Country": form.data["drop_country"],
                "Manufacturer": form.data["drop_manufacturer"],
                # "Language": form.data["drop_language"],
                #"VisualQuality": form.data["drop_visual"],
                #"MakeYear": form.data["drop_year"],

                "Zip": form.data["drop_zip"],
                "City": form.data["drop_city"],
                "UsageDuration": form.data["drop_duration"],


                # "Model": "Iphone5",
                # "Manufacturer": "Apple",
                # "Category": "Cell Phone",

                                     # http: // localhost:8080 / swagger - ui.html

            })
            headers = {
                'content-type': 'application/json'
            }
            r = requests.post(
                "http://localhost:8080/retrieval?casebase=spare&concept%20name=Spareparts&amalgamation%20function=default%20function",
            # r = requests.post("http://159.65.82.239:8080/retrieval?casebase=spare&concept%20name=Spareparts&amalgamation%20function=default%20function",
            #r = requests.post("http://159.65.82.239:8080/retrievalWithContent.json?casebase=spare&concept%20name=Spareparts&amalgamation%20function=default%20function",

                               data=payload,
                               headers=headers
                               ).json()["similarCases"]

            full_similar_cases = []
            parts=[]
            # if full_similar_cases
            # Filling each case with their full information, and formatting them
            for key, value in r.items():

                # Sorting out every case below 0.20 similarity
                if value > 0.80:
                    full_case = requests.get("http://localhost:8080//case?caseID=" + key).json()["case"]
                    full_case["Similarity"] = "%.3f" % value
                    # full_similar_cases.append(full_case)
                    full_similar_cases.append(full_case)
                    if Parts.objects.filter(id=full_case['Id']).exists():
                        parts.append(Parts.objects.get(id=full_case['Id']))

            # Sorting the case list based on similarity
            sorted_full_similar_cases = sorted(full_similar_cases, key=lambda k: k['Similarity'], reverse=True)
            if sorted_full_similar_cases:

                print(full_similar_cases)

                return render(request, 'search_results.html',
                               {'form': form, 'similar_cases': sorted_full_similar_cases[:3],'parts': parts,
                                })
            else:
                return redirect('no_search_result')
        else:
            print("Form error")
            form = QueryCaseBaseForm()

        return render(request, 'no_search_result.html', {'form': form})


def no_search_section(request):
    form = QueryCaseBaseForm()
    return render(
        request,
        'no_search_results.html',
        {"form": form}
    )

@login_required(login_url='/login/')
def register_post(request):

    if request.method == 'POST':
        form = PartRequestCreateForm(request.POST, request.FILES)
        errors = None
        print(form)
        if form.is_valid():
            if request.user.is_authenticated():
                instance = form.save(commit=False)
                # custoize and signals
                #  pre save
                instance.owner = request.user
                instance.save()
                # file = form.cleaned_data['image']
                # post save
                messages.success(request,'We will notify you when the part is available.')
                return redirect('register_post')
            else:
                return HttpResponseRedirect("/login/")
        if form.errors:
            errors = form.errors

        template_name = 'post.html'
        context = {"form": form, "errors": errors
                   }

        return render(request, template_name, context)

    else:
        template_name = 'request_post.html'
        context = {
                   }

        return render(request, template_name, context)