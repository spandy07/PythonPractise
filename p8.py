# A timestamp is three numbers: a number of hours, minutes and seconds. Given two timestamps, calculate how many seconds is between them.
# The moment of the first timestamp occurred before the moment of the second timestamp.
hrs_1 = int(input("Hour1: "))
min_1 = int(input("Minute1: "))
sec_1 = int(input("Second1: "))
hrs_2 = int(input("Hour2: "))
min_2 = int(input("Minute2: "))
sec_2 = int(input("Second2: "))
diff = (hrs_2 * 3600 + min_2 *60 + sec_2) - (hrs_1 * 3600 + min_1 *60 + sec_1)
print(diff)
