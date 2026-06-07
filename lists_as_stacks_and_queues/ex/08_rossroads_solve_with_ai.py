from collections import deque
green_light = int(input())

windol = int(input())

passed_car = 0
cars = deque()

flag = True
while True:

    command = input()

    if command == "END":
        print("Everyone is safe.")
        print(f"{passed_car} total cars passed the crossroads.")
        break

    elif command == "green":
        curent_green = green_light


        while cars and curent_green > 0:
            car = cars.popleft()
            car_length = len(car)

            if car_length <= curent_green:
                curent_green -= car_length
                passed_car += 1
            else:
                remainig_time = car_length - curent_green

                if remainig_time <= windol:
                    passed_car += 1
                    curent_green = 0

                else:
                    hit_index = curent_green + windol
                    print("A crash happened!")
                    print(f"{car} was hit at {car[hit_index]}.")
                    flag = False
                    break



        if not flag:
            break
    else:
        cars.append(command)




