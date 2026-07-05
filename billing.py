Python 3.14.6 (v3.14.6:c63aec69bd5, Jun 10 2026, 08:07:54) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
>>> class BillingSystem:
...     def generate_bill(self, product_name, price, quantity):
...         subtotal = price * quantity
... 
...         discount = 0
... 
...         if subtotal >= 5000:
...             discount = subtotal * 0.10
... 
...         gst = (subtotal - discount) * 0.18
...         total = subtotal - discount + gst
... 
...         print("\n========== INVOICE ==========")
...         print("Product :", product_name)
...         print("Price   :", price)
...         print("Quantity:", quantity)
...         print("-----------------------------")
...         print("Subtotal :", subtotal)
...         print("Discount :", discount)
...         print("GST (18%):", round(gst, 2))
...         print("-----------------------------")
...         print("Grand Total :", round(total, 2))
...         print("=============================")
... 
