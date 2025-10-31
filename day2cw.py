SHOP = "BOOKSTORE RECEIPT\n-----------------\n"
l1 = "\tBook Title: {} - Price {}\n".format("Python Basics", 450)
l2 = "\tBook Title: {} - Price {}\n".format("DataScience Intro", 600)
sum = 450 + 600
Total = "\tTotal price: {}\n".format(sum)
thanks = "\tThank you for shopping with us!"
receipt = SHOP + l1 + l2 + Total + thanks
print(receipt.upper())
