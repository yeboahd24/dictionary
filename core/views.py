from django.conf import settings
from django.shortcuts import render
from .forms import WordForm
import requests


def get_definition(request):
    if request.method == "POST":
        form = WordForm(request.POST)
        if form.is_valid():
            api_key = settings.DICTIONARY_KEY
            endpoint = "https://www.dictionaryapi.com/api/v3/references/thesaurus/json/"
            word = form.cleaned_data["input"]
            url = f"{endpoint}{word}?key={api_key}"
            response = requests.get(url)
            data = response.json()
            # data = JsonResponse(response, safe=False)
            synonyms = data[0]["meta"]["syns"][0]
            meaning = data[0]["shortdef"][0]
            return render(
                request,
                "dictionary.html",
                {"synonyms": synonyms, "meaning": meaning, "word": word},
            )
    else:
        form = WordForm()
    return render(request, "dictionary.html", {"form": form})
