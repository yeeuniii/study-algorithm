import sys
import math


def get_euclid_circle_area(r):
    return r * r * math.pi


def get_taxi_circle_area(r):
    return r * r * 2


if __name__ == "__main__":
    r = int(sys.stdin.readline().strip())
    print(f"{get_euclid_circle_area(r):.6f}")
    print(f"{get_taxi_circle_area(r):.6f}")
