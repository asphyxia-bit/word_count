#from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'home.html')

def count(request):
    user_tesxt = request.GET['text']
    total_len = len(user_tesxt)

    word_dict = {}
    for word in user_tesxt:
        if word not in word_dict:
            word_dict[word] = 1
        else:
         word_dict[word] += 1
    sorted_result = sorted(word_dict.items(),key=lambda x:x[1],reverse=True)
    return render(request,'count.html',
                  {'count': total_len,'text':user_tesxt
                   ,'frequent' :sorted_result[0]})