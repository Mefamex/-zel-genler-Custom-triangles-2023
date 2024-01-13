
# -*- coding: utf-8 -*-
# Created on Thursday, January 12, 2024
# Author: mefamex

def minimize(given):
    gcd = min(given)
    for number in given:
        while number:
            gcd, number = number, gcd % number
    return [number // gcd for number in given]

def add_tri(triangles, tri):
    tri.sort()
    if tri[0] == 0 or tri[1] == 0:
        return None
    if tri not in triangles:
        triangles.append(tri)

def find_tri(x, y):
    a = int(abs(x**2 - y**2))
    b = int(2 * x * y)
    c = int(x**2 + y**2)
    return [a, b, c]

def run_finder(max_X, max_Y, show=True):
    triangles = []
    print(f"max values and side: {max_X}, {max_Y}, {max(find_tri(max_X, max_Y))}\nRunning...  ", end="")
    for X in range(1, max_X):
        for Y in range(1, max_Y):
            tri = find_tri(X, Y)
            tri = minimize(tri)
            add_tri(triangles, tri)
        print(f"\rX: {len(triangles)}  ", end="")
    triangles.sort()

    print(f"\r{len(triangles)} special triangles found")
    if show:
        print(*triangles, sep="\n")
        print("Done!")
    return triangles



if __name__ == "__main__":
    user_X = 10
    user_Y = 10

    run_finder(user_X, user_Y)

    # Or
    run_finder(5, 5, show=False)

    # Or 
    run_finder(3, 3)

    # Last one
    big = run_finder(100, 100, show=False)
    print("last big one:", big[-1])
