print("Enter a distance(in numbers).")
distance = input()
print("Enter units.")
units = input()
print("Enter target units.")
tgt_units = input()

mi = 1.0000
km = 1.60934 * mi
ft = 5280.0000 * mi
m = 1609.34 * mi

if tgt_units == mi:
    mi = 1.0000
elif tgt_units == km:
    km = 1.60934 * mi
elif tgt_units == ft:
    ft = 5280.0000 * mi
elif tgt_units == m:
    m = 1609.34 * mi


total_units = float(distance) * float(tgt_units)

if tgt_units == mi:
    print(distance + units + 'is' + total_units + tgt_units)
elif tgt_units == km:
    print(distance + units + 'is' + total_units + tgt_units)
elif tgt_units == ft:
    print(distance + units + 'is' + total_units + tgt_units)
elif tgt_units == m:
    print(distance + units + 'is' + total_units + tgt_units)
