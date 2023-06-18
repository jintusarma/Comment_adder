from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from dataset_upload.models import *
from django.urls import reverse
from django.db.models import Q

# Create your views here.

def home(request):
    # obj = AllDataset.objects.all()
    return  render(request,'home.html')


def list_sentence(request):
    tab = request.GET["tab"]
    if tab == "ab":
        obj = AssameseBodoDataset.objects.filter(score=None)
    if tab == "ae":
        obj = AssameseEnglishDataset.objects.filter(score=None)
    if tab == "be":
        obj = BodoEnglishDataset.objects.filter(score=None)
    return  render(request,'list.html',{'data':obj})


def edit_sentence(request,pk,dt):
    if dt == "ab":
        sentence = get_object_or_404(AssameseBodoDataset,pk=pk)
    elif dt == "be":
        sentence = get_object_or_404(BodoEnglishDataset,pk=pk)
    elif dt == "ae":
        sentence = get_object_or_404(AssameseEnglishDataset,pk=pk)


    if request.method == "POST":
        dt = request.POST.get('data_lang')
        score = request.POST.get('score')
        remark = request.POST.get('remark')
        typee = request.POST.get('typee')
        
        sentence.score = score
        sentence.remark = remark
        sentence.typee =typee
        # sentence.save()
        print(score)

        

        if dt == "ab":
            next_sentence = AssameseBodoDataset.objects.filter(id__gt=sentence.id).first()
            if next_sentence:
                return redirect('edit_sentence', pk=next_sentence.pk,dt="ab")
            else:
                url = reverse('list_sentence') +'?tab=ab'
                return redirect(url)
            
        elif dt == "be":
            next_sentence = BodoEnglishDataset.objects.filter(id__gt=sentence.id).first()
            if next_sentence:
                return redirect('edit_sentence', pk=next_sentence.pk,dt="be")
            else:
                url = reverse('list_sentence') +'?tab=be'
                return redirect(url)
            
        elif dt == "ae":
            next_sentence = AssameseEnglishDataset.objects.filter(id__gt=sentence.id).first()
            if next_sentence:
                return redirect('edit_sentence', pk=next_sentence.pk,dt="ae")
            else:
                url = reverse('list_sentence') +'?tab=ae'
                return redirect(url)

    
    return render(request,'edit/edit_sentence.html',{'data':sentence})















# unused

def modify(request):

    tab = request.GET["tab"]
    # print(tab)
    if request.method == "POST":
        # idk = request.POST['idk']
        domain = request.POST.get('domain')
        sen_l1 = request.POST.get('sen_l1')
        sen_l2 = request.POST.get('sen_l2')
        score = request.POST.get('score')
        remark = request.POST.get('remark')
        typee = request.POST.get('typee')

        if tab == "ab":
            # AssameseBodoDataset.objects.create()
            print(domain)
        #  .objects.create(domain=domain,sen_l1=sen_l1,seng_l2=sen_l2,score=score,remark=remark,typee=typee)
        # sel_obj = Dataset.objects.get(pk= sen_id)
        # sel_obj.remark = remark
        # sel_obj.save()
        # print(sel_obj)
        # print(score,remark,typee,sen_id)
    # obj = Dataset.objects.filter( Q(score=None) | Q(remark=None) | Q(typee=None))
    obj = AllDataset.objects.filter(is_updated=False)
    context = {'data':obj}
    return  render(request,'index.html',context)