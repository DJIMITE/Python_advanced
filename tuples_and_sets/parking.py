n = int(input())

parking = set()

for i in range(n):
    directory, car_number = input().split(", ")

    if directory == "IN":
        parking.add(car_number)
    elif directory == "OUT":
        parking.remove(car_number)
if len(parking) == 0:
    print("Parking Lot is Empty")
else:
    for car_number in parking:
        print(car_number)
