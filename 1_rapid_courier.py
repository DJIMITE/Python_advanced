from collections import deque

packets = list(map(int, input().split()))
couriers = deque(map(int, input().split()))
wight_packet = 0

while packets and couriers:
    packet = packets[-1]
    courier = couriers.popleft()


    if courier >= packet:
        wight_packet += packet
        packets.pop()
        current_wight = courier - (packet *2)
        if current_wight > 0:
            couriers.append(current_wight)

    elif courier < packet:
        current_wight = packet - courier
        packets[-1] = current_wight
        wight_packet += courier
print(f"Total weight: {wight_packet} kg")

if not packets and not couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")

if packets and not couriers:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(map(str, packets))}")

if couriers and not packets:
    print(f"Couriers are still on duty: {', '.join(map(str, couriers))} but there are no more packages to deliver.")


