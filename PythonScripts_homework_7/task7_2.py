raw_transactions = ["SUCCESS:100", "FAILED:50", "SUCCESS:-10",
"SUCCESS:0", "SUCCESS:250", "ERROR:200"]

#clearing transactions that didn't success
transactions = [
    int(t.split(":")[1])
    for t in raw_transactions
    if "SUCCESS:" in t
    and int(t.split(":")[1]) > 0]    #added a second if to filter out invalid values

print(f"Очищенные транзации: {transactions}")