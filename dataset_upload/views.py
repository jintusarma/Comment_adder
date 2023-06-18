from django.shortcuts import render
from .models import *
from main.models import *

# Create your views here.
def upload(request):
    if request.method == "POST":
        domain = request.POST["domain"]
        assamese = request.FILES['assamese']
        bodo = request.FILES['bodo']
        english = request.FILES['english']

        lines_file1 = assamese.read().decode('utf-8').splitlines()
        lines_file2 = bodo.read().decode('utf-8').splitlines()
        lines_file3 = english.read().decode('utf-8').splitlines()

        same_lines_count = len(set([len(lines_file1), len(lines_file2), len(lines_file3)])) == 1

        if same_lines_count is True:
            
            assamese_sentence = []
            for line in assamese:
                    text= line.decode('utf-8').strip()
                    AssameseDataset.objects.create(domain=domain,sentence_L1=text)
                    assamese_sentence.append(text)
            
            bodo_sentence = []
            for line in bodo:
                    text= line.decode('utf-8').strip()
                    BodoDataset.objects.create(domain=domain,sentence_L2=text)
                    bodo_sentence.append(text)
            
            english_sentence = []
            for line in english:
                    text= line.decode('utf-8').strip()
                    EnglishDataset.objects.create(domain=domain,sentence_L3=text)
                    english_sentence.append(text)

            num_lines = max(len(assamese_sentence), len(bodo_sentence), len(english_sentence))
            for i in range(num_lines):
                AllDataset.objects.create(
                    domain = domain,
                    sentence_L1=assamese_sentence[i] if i < len(assamese_sentence) else None,
                    sentence_L2=bodo_sentence[i] if i < len(bodo_sentence) else None,
                    sentence_L3=english_sentence[i] if i < len(english_sentence) else None,
                )
            

            for i in range(num_lines):
                AssameseBodoDataset.objects.create(
                    domain = domain,
                    sentence_L1=assamese_sentence[i] if i < len(assamese_sentence) else None,
                    sentence_L2=bodo_sentence[i] if i < len(bodo_sentence) else None,
                )
                AssameseEnglishDataset.objects.create(
                    domain = domain,
                    sentence_L1=assamese_sentence[i] if i < len(assamese_sentence) else None,
                    sentence_L3=english_sentence[i] if i < len(english_sentence) else None,
                )
                BodoEnglishDataset.objects.create(
                    domain = domain,
                    sentence_L2=bodo_sentence[i] if i < len(bodo_sentence) else None,
                    sentence_L3=english_sentence[i] if i < len(english_sentence) else None,
                )


        # print(domain,assamese)
    return render(request,"upload.html")