stock = int(input())
price = int(input())
req_stock = int(input())
amount = int(input())
total_amount = price * req_stock
if stock >= req_stock and total_amount <= amount:
    print("Remaining amount",amount - total_amount)
else:
    print("Insufficent")
