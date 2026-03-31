def get_balance(transactions):
    total_deposits = 0
    total_withdrawals = 0
    balance = 0
    status = ""
    
    for transaction in transactions:
        if transaction is None:
            return False
        elif transaction['type'] == 'deposit':
            total_deposits = total_deposits + transaction['amount']
        else:#transaction['type'] == 'withdrawals': preguntar porque el elif no sirve y el else si
            
            total_withdrawals = total_withdrawals + transaction['amount']
            
            
    balance = total_deposits - total_withdrawals   
        
    if balance < 0:
        status = "negative"
    elif balance >= 0:
        status = "positive"
    
    return {
        "total_deposits": total_deposits,
        "total_withdrawals": total_withdrawals,
        "balance": balance,
        "status": status,
    }


transactions = [
    {"type": "deposit", "amount": 1500},
    {"type": "withdrawal", "amount": 200},
    {"type": "deposit", "amount": 800},
    {"type": "withdrawal", "amount": 1900},
    {"type": "deposit", "amount": 600},
    {"type": "withdrawal", "amount": 300},
]
print(get_balance(transactions))