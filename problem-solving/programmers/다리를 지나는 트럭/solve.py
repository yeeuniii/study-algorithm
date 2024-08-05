from collections import deque


class Bridge:
    def __init__(self, max_weight, length):
        self.MAX_WEIGHT = max_weight
        self.LENGTH = length
        self.bridge = deque([0 for _ in range(length)])
        self.total_truck_weight = 0

    def move_forward_all_trucks(self):
        if truck := self.bridge.popleft():
            self.total_truck_weight -= truck

    def can_accept_truck(self, truck):
        return self.total_truck_weight + truck <= self.MAX_WEIGHT

    def add_truck(self, truck):
        self.bridge.append(truck)
        if truck:
            self.total_truck_weight += truck


def solution(bridge_length, weight, truck_weights):
    time = 0
    trucks = deque(truck_weights)
    bridge = Bridge(weight, bridge_length)

    while trucks:
        bridge.move_forward_all_trucks()
        if bridge.can_accept_truck(trucks[0]):
            truck = trucks.popleft()
            bridge.add_truck(truck)
        else:
            bridge.add_truck(0)
        time += 1
    time += bridge_length
    return time


def main():
    print(solution(2,	10,	[7,4,5,6]))
    print(solution(100,100,[10]))
    print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))


if __name__ == "__main__":
    main()
