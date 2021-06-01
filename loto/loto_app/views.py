from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
# Create your views here.
from loto.loto_app.forms import AbetForm, BbetForm, CbetForm, DbetForm, EbetForm, FbetForm, GbetForm, PlayerForm, \
    EventForm
from loto.loto_app.models import Bet, Mybet


class IndexView(TemplateView):
    template_name = "index.html"

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'home'
        return context


@login_required
def mybetsview(request):
    bets = [x.bet.id for x in Mybet.objects.filter(user=request.user)]
    for bet in Bet.objects.all():
        if bet.id not in bets:
            mybet = Mybet()
            mybet.bet = bet
            mybet.user = request.user
            mybet.save()


    mybets_list = Mybet.objects.filter(user=request.user).order_by('bet_id')
    page = request.GET.get('page', 1)
    paginator = Paginator(mybets_list, 10)
    try:
        mybets = paginator.page(page)
    except PageNotAnInteger:
        mybets = paginator.page(1)
    except EmptyPage:
        mybets = paginator.page(paginator.num_pages)
    context = {
        'mybets': mybets,
        'current_page' : 'my bets',
    }
    return render(request, 'app/my_bets.html', context)

@login_required
def edit_bet(request, pk):
    mybet = Mybet.objects.get(pk=pk)
    if mybet.bet.type == 'type_a':
        if request.method == 'GET':
            form = AbetForm(instance=mybet)
        else:
            form = AbetForm(request.POST, instance=mybet)
    if mybet.bet.type == 'type_b':
        if request.method == 'GET':
            form = BbetForm(instance=mybet)
        else:
            form = BbetForm(request.POST, instance=mybet)
    if mybet.bet.type == 'type_c':
        if request.method == 'GET':
            form = CbetForm(instance=mybet)
        else:
            form = CbetForm(request.POST, instance=mybet)
    if mybet.bet.type == 'type_d':
        if request.method == 'GET':
            form = DbetForm(instance=mybet)
        else:
            form = DbetForm(request.POST, instance=mybet)
    if mybet.bet.type == 'type_e':
        if request.method == 'GET':
            form = EbetForm(instance=mybet)
        else:
            form = EbetForm(request.POST, instance=mybet)
    if mybet.bet.type == 'type_f':
        f_teams = mybet.bet.fteams
        if request.method == 'GET':
            form = FbetForm(instance=mybet)
        else:
            form = FbetForm(request.POST, instance=mybet)
    if mybet.bet.type == 'type_g':
        if request.method == 'GET':
            form = GbetForm(instance=mybet)
        else:
            form = GbetForm(request.POST, instance=mybet)

    if request.method == 'GET':
        if mybet.bet.type == 'type_f':
            context = {
                'form': form,
                'mybet': mybet,
                'fteams': f_teams,
            }
        else:
            context = {
                'form': form,
                'mybet': mybet,
            }
        return render(request, 'app/edit.html', context)
    else:
        if mybet.bet.type == 'type_f':
            if form.is_valid():
                f_team = request.POST.getlist('type_f_bet_3')[0]
                form.save()
                mybet.type_f_bet_3 = f_team
                mybet.save()
                return redirect('my bets')

            context = {
                'form': form,
                'mybet': mybet,
                'fteams': f_teams,
            }
        else:
            if form.is_valid():
                form.save()
                return redirect('my bets')
            context = {
                'form': form,
                'mybet': mybet,
            }

        return render(request, 'app/edit.html', context)


@login_required
def player_choice(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = form.cleaned_data['player']
            pk = player.pk
            return redirect('player bets', pk)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PlayerForm()
        context = {
            'form': form,
        }
    return render(request, 'app/player.html', context)

@login_required
def player_bets(request, pk):
    mybets_list = Mybet.objects.filter(user=pk).order_by('bet_id')
    player = User.objects.get(id=pk).username
    page = request.GET.get('page', 1)
    paginator = Paginator(mybets_list, 10)
    try:
        mybets = paginator.page(page)
    except PageNotAnInteger:
        mybets = paginator.page(1)
    except EmptyPage:
        mybets = paginator.page(paginator.num_pages)
    context = {
        'mybets': mybets,
        'current_page': 'player bets',
        'player': player,
    }
    return render(request, 'app/player_bets.html', context)

@login_required
def event_choice(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.cleaned_data['event']
            pk = event.pk
            return redirect('event bets', pk)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = EventForm()
        context = {
            'form': form,
        }
    return render(request, 'app/event.html', context)


@login_required
def event_bets(request, pk):
    mybets_list = Mybet.objects.filter(bet=pk)
    event = Bet.objects.get(id=pk)
    page = request.GET.get('page', 1)
    paginator = Paginator(mybets_list, 10)

    try:
        mybets = paginator.page(page)
    except PageNotAnInteger:
        mybets = paginator.page(1)
    except EmptyPage:
        mybets = paginator.page(paginator.num_pages)
    context = {
        'mybets': mybets,
        'current_page': 'event bets',
        'event': event,
    }
    return render(request, 'app/event_bets.html', context)


@login_required
def ranking_view(request):
    user_list = User.objects.all()
    ranking_list = {}
    for u in user_list:
        mybets_list = Mybet.objects.filter(user=u)
        sum_points = 0
        for mybet in mybets_list:
            sum_points += mybet.points
        ranking_list[u] = sum_points
    ranking_list_users = [k for k,v in sorted(ranking_list.items(), key=lambda x: -x[1])]
    page = request.GET.get('page', 1)
    paginator = Paginator(ranking_list_users, 10)

    try:
        ranking_users = paginator.page(page)
    except PageNotAnInteger:
        ranking_users = paginator.page(1)
    except EmptyPage:
        ranking_users = paginator.page(paginator.num_pages)
    context = {
        'ranking_list': ranking_list,
        'ranking_users' : ranking_users,
        'current_page': 'ranking',
        'page_number': page,
    }
    return render(request, 'app/ranking.html', context)