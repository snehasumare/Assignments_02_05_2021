bill_amount = int(input("Enter Bill amount:"))
gst_percent = float(input("Enter gst percent:"))
total_bill = bill_amount + (bill_amount*gst_percent/100)
print(total_bill)