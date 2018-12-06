from django.shortcuts import render
from .models import People,Card
# Create your views here.
def index(request):
    # p1 = People.objects.create(name='大一',age=11,sex=True)
    # p2 = People.objects.create(name='大二',age=12,sex=True)
    # p3 = People.objects.create(name='大三',age=13,sex=True)
    # p4 = People.objects.create(name='大四',age=14,sex=True)
    #
    # c1 = Card(person=p3,code='33333',address='地址3')
    # c2 = Card(person=p4,code='44444',address='地址4')
    # c3 = Card(person=p2,code='22222',address='地址2')
    # c4 = Card(person=p1,code='11111',address='地址1')
    #
    # c1.save()
    # c2.save()
    # c3.save()
    # c4.save()

    return render(request,'first.html',{'content':'hello world'})

def select(request):

    c4 = Card.objects.get(address='地址1')
    print(c4.code)
    print(c4.person.name)

    c3 = Card.objects.get(person__name = '大三')
    print(c3.address)

    p1 = People.objects.get(card__address = '地址4')
    print(p1.name)
    return render(request,'first.html')