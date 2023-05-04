# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

# Part 1: Leek price
leek_price = 2
print("Leek is " + str(leek_price) + " euro per kilo.")

# Part 2: Leek order
leek_order = "leek 4"
leek_order_amount = leek_order[leek_order.find(" "):]
leek_order_amount = int(leek_order_amount)

sum_total = leek_order_amount * leek_price
print(sum_total)

# Part 3: Broccoli order
broccoli_price = 2.34
broccoli_order = "broccoli 1.6"
broccoli_order_amount = float(broccoli_order[broccoli_order.find(" "):])
broccoli_sum_total = round(broccoli_price * broccoli_order_amount, 2)

print(str(broccoli_order_amount) + "kg broccoli costs " + str(broccoli_sum_total) + "e")


