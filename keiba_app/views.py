from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm

from keiba_app.models import Race

def create_race():
    #新たなレースデータを作成する。
    race = Race()

    if request.method == "GET": #GET操作だった場合はkeiba_app/race_form.htmlのページを返す。
        form = RaceForm(instance=race)

        return render(request, 'keiba_app/race_form.html', {'form': form})
    
    if request.method == "POST": #GET操作だった場合はデータ更新の処理を行う。
        form = PostRace(request.RACE, instance=race)

        if form.is_valid():
            race = form.save(commit=False)
            race.save
        
        return redirect('keiba_app:read_race')
    
def read_race(request):
    #レース一覧を表示する。

    races = Race.objects.all().order_by('id')
    return render(request, 'keiba_app/race_list.html', {'races': races})