from django.shortcuts import render
from geoproyecto.models import Municipality, Project, Rate, RateItem
from django.shortcuts import get_object_or_404
from django.db.models import Avg
from django.http import JsonResponse


def municipalities(request):
    municipalities = Municipality.objects.all()
    return render(request, 'geoproyecto/municipalities.html', {'munis':municipalities})
    
def muni(request, muni_id):
    muni = get_object_or_404(Municipality, pk=muni_id)
    projects = Project.objects.filter(municipality = muni_id, active = True)
    return render(request, 'geoproyecto/muni.html', {'muni':muni, 'projects':projects})

def proj(request, proj_id):
    proj = get_object_or_404(Project, pk=proj_id)
    rates = RateItem.objects.all()
    rateList = {}
    for rateItem in rates:
        rateList[rateItem.name] = Rate.objects.filter(project = proj_id, rate_item = rateItem.id).aggregate(value_avg=Avg('value'))['value_avg']
    return render(request, 'geoproyecto/proyecto.html', {'muni':proj.municipality, 'project':proj, 'rates':rateList})
    
def vote(request):
    item = request.POST['item']
    rateItems = RateItem.objects.all()
    riKeyName = ""
    riId = 0
    for ri in rateItems:
        riKeyName = ri.name.replace(" ","")
        if (riKeyName == item):
            riId = ri.id
            break
    if (riKeyName == item):
        projectObj = Project.objects.filter(id = request.POST['proj']).first()
        rate = Rate(rate_item = RateItem.objects.filter(id=riId).first(),
                    value = request.POST['value'],
                    project = projectObj,
                    ip = request.META.get('REMOTE_ADDR'),
                )
        rate.save()
        newValue = Rate.objects.filter(project = projectObj.id, rate_item = riId).aggregate(value_avg=Avg('value'))['value_avg']
        return JsonResponse({'value':newValue}, safe=False)
    else:
        return False