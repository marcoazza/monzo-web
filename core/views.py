import logging
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import requests


@login_required
def index(request):
    # print('User', request.user.social_auth.all())
    # print('User', request.user)
    social = request.user.social_auth.get(provider='monzo')
    print(social.extra_data)
    response = requests.get(
        'https://api.monzo.com/accounts',
        # params={'account_type': 'uk_retail'},
        headers={'Authorization': 'Bearer {}'.format(social.extra_data['access_token'])}
    )
    accounts = response.json().get('accounts', [])
    print(accounts)
    return render(request, 'core/welcome.html', {'accounts': accounts, })


@login_required
def details(request, account_id):
    # print('User', request.user.social_auth.all())
    # print('User', request.user)
    social = request.user.social_auth.get(provider='monzo')
    print('account_id: ', account_id)
    response = requests.get(
        'https://api.monzo.com/transactions?account_id={}'.format(account_id),
        headers={'Authorization': 'Bearer {}'.format(social.extra_data['access_token'])}
    )
    transactions = response.json()
    print(transactions)
    return render(request, 'core/transactions.html', {'transactions': transactions.get('transactions'), })
