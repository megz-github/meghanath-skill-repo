"""A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.

Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.

You will to use the arithmetic operators to complete this exercise."""

usb_stick_price = 6
budget = 50
num_usb_sticks = budget // usb_stick_price
pounds_left = budget % usb_stick_price
print("The girl can buy", num_usb_sticks, "USB sticks.")
print("She will have £", pounds_left, "left.")

