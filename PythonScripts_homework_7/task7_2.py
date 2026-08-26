raw_transactions = ["SUCCESS:100", "FAILED:50", "SUCCESS:-10",
"SUCCESS:0", "SUCCESS:250", "ERROR:200"]

#clearing transactions that didn't success
transactions = [
    int(t.split(":")[1])
    for t in raw_transactions
    if "SUCCESS:" in t]

#selecting only valid transactions (hope this is not banned)
for i in range(len(transactions) - 1, -1, -1):
    if transactions[i] <= 0:
        transactions.pop(i)

print(f"Очищенные транзации: {transactions}")