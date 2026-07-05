Python 3.14.6 (v3.14.6:c63aec69bd5, Jun 10 2026, 08:07:54) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
class CustomerManagement:
    def __init__(self):
...         self.customers = {}
... 
...     def add_customer(self):
...         cid = input("Customer ID: ")
... 
...         if cid in self.customers:
...             print("Customer already exists!")
...             return
... 
...         self.customers[cid] = {
...             "name": input("Customer Name: "),
...             "phone": input("Phone: "),
...             "email": input("Email: "),
...             "history": []
...         }
... 
...         print("Customer Added Successfully!")
... 
...     def search_customer(self):
...         cid = input("Enter Customer ID: ")
... 
...         if cid in self.customers:
...             print(self.customers[cid])
...         else:
...             print("Customer Not Found!")
... 
...     def purchase_history(self):
...         cid = input("Enter Customer ID: ")
... 
...         if cid in self.customers:
...             print("\nPurchase History")
...             history = self.customers[cid]["history"]
... 
...             if history:
...                 for item in history:
...                     print(item)
...             else:
...                 print("No Purchases Yet.")
...         else:
