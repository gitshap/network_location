from django.shortcuts import redirect, render

from equipment.models import Building, Computer, Floor, Switch
import os


def home(request):
    template_name = 'home.html'
    main_building = Floor.objects.filter(building=1)
    annex_building = Floor.objects.filter(building=3)
    shs_building = Floor.objects.filter(building=2)

    context = {
        'main_building': main_building,
        'annex_building': annex_building,
        'shs_building': shs_building,

    }
    return render(request, template_name, context=context)


def floor(request):
    template_name = 'floors.html'
    comp = Computer.objects.all()
    context = {
        'computer': comp
    }
    return render(request, template_name, context=context)


def floor_level(request, id):
    get_floor = Floor.objects.get(id=id)
    switches = Switch.objects.filter(floor=get_floor.id)


    template_name = 'floor_level.html'

    context = {
        'switches': switches,
    }
    return render(request, template_name, context=context)

def ping(request, id):
    comp = Computer.objects.get(id=id)
    response = os.system("ping -n 1 " + comp.pc_name)
    if response == 0:
        print(f'{comp.pc_name} is up')
        comp.is_reachable = True
        comp.save()
    else:
        print(f'{comp.pc_name} is down')
        comp.is_reachable = False
        comp.save()
    
    return redirect(request.META.get('HTTP_REFERER'))
