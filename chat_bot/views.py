from django.shortcuts import render

# Create your views here.


def get_title(site):
        return 'заголовок сайта %s' % site

def homepage(request):
    return render(request, 'homepage.html')


def chat(request):
    return render(request, 'chat.html')


def chat_bot(request):
    query = request.GET['query']
    if query.startswith('Бот, дай мне заголовок сайта'):
        header = get_title(query.split()[-1:][0])
        return render(request, 'chat.html', {'response': header})


