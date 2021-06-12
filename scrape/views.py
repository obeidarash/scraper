from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ScrapeForm
from .models import Scrape
import requests
from bs4 import BeautifulSoup
# import goslate


@login_required(login_url='/admin')
def scrape(request):
    scrape_form = ScrapeForm(request.POST or None)
    if scrape_form.is_valid():
        url = scrape_form.cleaned_data.get('url')
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h1', attrs={'class': 'jojo', 'id': 'title-large-bold'}).text
        # gs = goslate.Goslate()
        # title = gs.translate(title, 'fa')
        rows = soup.find_all('div', attrs={'class': 'div-table-col-right'})
        color = rows[5].text
        size = rows[4].text
        Scrape.objects.create(user=request.user, url=url, title=title, color=color, size=size)
        scrape_form = ScrapeForm()
        redirect('scrape')
    context = {
        'title': 'Scraper - Test',
        'scrape_form': scrape_form
    }
    return render(request, 'home.html', context)
