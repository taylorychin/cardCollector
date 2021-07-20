from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Deck, Extra, Accessory
from .forms import ExtraForm

# Create your views here.
# Add the Cat class & list and view function below the imports


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, "about.html")


def decks_index(request):
    decks = Deck.objects.all()
    return render(request, 'decks/index.html', {
        'decks': decks,
    })


def decks_detail(request, deck_id):
    deck = Deck.objects.get(id=deck_id)
    accessories_deck_doesnt_have = Accessory.objects.exclude(
        id__in=deck.accessories.all().values_list('id'))
    extra_form = ExtraForm()
    return render(request, 'decks/detail.html', {
        "deck": deck,
        'extra_form': extra_form,
        'accessories': accessories_deck_doesnt_have
    })


class DeckCreate(CreateView):
    model = Deck
    fields = ['name', 'brand', 'description', 'printing_company']
    success_url = '/decks/'


class DeckUpdate(UpdateView):
    model = Deck
    fields = ['brand', 'description', 'printing_company', ]


class DeckDelete(DeleteView):
    model = Deck
    success_url = '/decks/'


class ExtraUpdate(CreateView):
    model = Extra
    fields = ['name']


class ExtraDelete(DeleteView):
    model = Extra
    success_url = "decks/<int:deck_id>/"


def add_extra(request, deck_id):
    form = ExtraForm(request.POST)
    if form.is_valid():
        new_extra = form.save(commit=False)
        new_extra.deck_id = deck_id
        new_extra.save()
    return redirect('detail', deck_id=deck_id)


def assoc_acc(request, deck_id, accessory_id):
    Deck.objects.get(id=deck_id).accessories.add(accessory_id)
    return redirect('detail', deck_id=deck_id)


def unassoc_acc(request, deck_id, accessory_id):
    Deck.objects.get(id=deck_id).accessories.remove(accessory_id)
    return redirect('detail', deck_id=deck_id)


class AccList(ListView):
    model = Accessory


class AccDetail(DetailView):
    model = Accessory


class AccCreate(CreateView):
    model = Accessory
    fields = '__all__'


class AccUpdate(UpdateView):
    model = Accessory
    fields = ['name', 'color']


class AccDelete(DeleteView):
    model = Accessory
    success_url = '/accessories/'
