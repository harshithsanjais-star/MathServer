from django.shortcuts import render
def fuel(request):
    d = int(request.POST.get('distance', 0))
    f = int(request.POST.get('fuelconsumed', 0))
    fe = d / f if request.method == 'POST' else 0
    print("DISTANCE=",d)
    print("FUELCONSUMED=",f)
    print("FUELEFFICENCY=",fe)
    return render(request, 'mathapp/math.html', {'d': d, 'f': f, 'fe': fe})