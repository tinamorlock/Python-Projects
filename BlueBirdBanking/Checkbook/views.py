from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction

# this function renders the Home page when requested

def home(request):
    form = TransactionForm(data=request.POST or None)     # retrieve form
    # checks if POST
    if request.method == 'POST':
        pk = request.POST['account']        # retrieve acct
        return balance(request, pk)     # call balance function to render the balance sheet
    content = {'form': form}        # pass content to template in a dictionary
    # adds content of form to the page
    return render(request, 'checkbook/index.html', content)


# this function renders the Create New Account page when requested

def create_account(request):
    form = AccountForm(data=request.POST or None)   # retrieve acct form
    # checks if request method is POST
    if request.method == 'POST':
        if form.is_valid():     # saves if valid
            form.save()         # saves new account
            return redirect('index')    # returns back to home
    content = {'form': form}            # saves content to the template as a dictionary
    # adds content of form to page
    return render(request, 'checkbook/CreateNewAccount.html', content)


# this function renders the Balance page when requested

def balance(request, pk):
    account = get_object_or_404(Account, pk=pk)     # retrieve using primary key
    transactions = Transaction.Transactions.filter(account=pk)      # retrieve all of the accounts transactions
    current_total = account.initial_deposit     # creates account total variable, starting with initial deposit
    table_contents = {}     # creates a dictionary where the transactions will go
    for t in transactions:      # loops through transactions
        if t.type == 'Deposit':
            current_total += t.amount       # adds deposit to total
            table_contents.update({t: current_total})       # adds transaction and total
        else:
            current_total -= t.amount   # withdrawal subtracts from acct
            table_contents.update({t: current_total})     # transaction and total go in dictionary
    # pass account, account total balance, and transaction info to template
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)


# this function renders the Transaction page when requested

def transaction(request):
    form = TransactionForm(data=request.POST or None)   # retrieves transaction form
    # checks if POST
    if request.method == 'POST':
        if form.is_valid():     # saves form if valid
            pk = request.POST['account']        # retrieve which account the transaction was for
            form.save()
            return balance(request, pk)         # renders balance of the accounts Balance Sheet
    # pass content to the template in a dictionary
    content = {'form': form}
    # adds content of form to page
    return render(request, 'checkbook/AddTransaction.html', content)
