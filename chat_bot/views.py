from django.shortcuts import render
from urllib import request
import lxml.html as html
from datetime import datetime
from chat_bot.models import Message

# Create your views here.


def get_title(site):
    response = request.urlopen(site)
    tree = html.document_fromstring(response.read())
    title = tree.xpath('/html/head/title/text()')[0].strip()
    return ' >> заголовок сайта %s -- %s' % (site, title)


def get_h1(site):
    h1 = 'H1'
    return 'H1 сайта %s равен %s' % (site, h1)


def chat_page(request):
    return render(request, 'chat.html')


def chat_bot(request):
    query = request.POST['query']
    if query.startswith('Бот, дай мне заголовок сайта'):
        site = query.split()[-1:][0]
        if not site.startswith('http') and not site.startswith('https'):
            return render(request, 'chat.html', {'response': 'Адрес сайта должен начинаться с http:// или https://'})

        header = get_title(query.split()[-1:][0])
        new_message = datetime.now().strftime('Дата %d.%m.%y %H:%M:%S') + header
        Message.objects.create(text=new_message)
        messages = [mes.text for mes in Message.objects.all()]
        return render(request, 'chat.html', {'response': messages})

    if query.startswith('Бот, дай мне H1 с сайта'):
        h1 = get_h1(query.split()[-1:][0])
        return render(request, 'chat.html', {'response': h1})





