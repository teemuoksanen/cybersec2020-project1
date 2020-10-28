from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.db import connection
from .models import Account, Transaction

@login_required
@csrf_exempt
def transferView(request):

  if request.method == 'GET':
    user_from_username = request.GET.get('user_from')
    user_to_username = request.GET.get('user_to')
    user_from = User.objects.get(username=user_from_username)
    user_to = User.objects.get(username=user_to_username)
    amount = int(request.GET.get('amount'))
    message = request.GET.get('message')
    acc1 = Account.objects.get(user=user_from)
    acc2 = Account.objects.get(user=user_to)

    if amount > 0 and amount <= acc1.balance:
      acc1.balance -= amount
      acc2.balance += amount
      with connection.cursor() as cursor:
        sql = 'INSERT INTO baybal_transaction (user_from, user_to, amount, message) VALUES ("%s", "%s", "%s", "%s")' % (user_from_username, user_to_username, amount, message)
        cursor.executescript(sql)
      acc1.save()
      acc2.save()

  return redirect('/')

@login_required
@csrf_exempt
def claimView(request):

  if request.method == 'GET':
    account = Account.objects.create(user=request.user, balance=100)
    account.save()
  return redirect('/')

@login_required
def homePageView(request):

  own_account = Account.objects.filter(user_id=request.user.id).first()

  if own_account == None:
    return render(request, 'pages/claim.html')

  users = Account.objects.exclude(user_id=request.user.id)
  received = Transaction.objects.filter(user_to=request.user.username)
  paid = Transaction.objects.filter(user_from=request.user.username)

  return render(request, 'pages/index.html', {'own_account': own_account, 'users': users, 'received': received, 'paid': paid})
