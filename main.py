
# -*- coding: utf-8 -*-
# Created on Thursday, January 12, 2024
# Author: mefamex

class SpeTriFinder:
    def __init__(self, user_X, user_Y, show=True):
        """
        Initializes the SpeTriFinder class.

        Parameters:
            user_X (int): The user-provided value for X.
            user_Y (int): The user-provided value for Y.
            show (bool, optional): Whether to show the triangles. Defaults to True.
        """
        self.spec_tri, self.show = [], show
        self.run_finder(user_X, user_Y, show=show)
 
    def minimize(self, given: list):
        """
        Calculates the greatest common divisor and minimizes the given numbers.

        Parameters:
            given (list): List of numbers to minimize.

        Returns:
            list: Minimized list of numbers.
        """
        gcd = min(given)
        for number in given:
            while number:
                gcd, number = number, gcd % number
        return [number // gcd for number in given]

    def add_tri(self, tri: list):
        """
        Adds a triangle after sorting and checking for duplicates.

        Parameters:
            tri (list): Triangle to be added.

        Returns:
            None: If triangle is invalid (contains zero).
        """
        tri.sort()
        if tri[0] == 0 or tri[1] == 0: return None
        if tri not in self.spec_tri:
            self.spec_tri.append(tri)

    def find_tri(self, x, y):
        """
        Finds the sides of a triangle with given x and y values.

        Parameters:
            x (int): First parameter.
            y (int): Second parameter.

        Returns:
            list: List representing the sides of the triangle.
        """
        a = int(abs(x**2 - y**2))
        b = int(2 * x * y)
        c = int(x**2 + y**2)
        return [a, b, c]

    def run_finder(self, max_X, max_Y, show=None):
        """
        Finds and optionally shows special triangles based on user-provided X and Y values.

        Parameters:
            max_X (int): The maximum value for X in the loop.
            max_Y (int): The maximum value for Y in the loop.
            show (bool, optional): Whether to show the triangles. Defaults to the value provided in __init__.
        """
        if show is None:
            show = self.show
        self.spec_tri = []
        print(f"max values and side: {max_X}, {max_Y}, {max(self.find_tri(max_X, max_Y))}\nRunning...  ", end="")
        for X in range(1, max_X):
            for Y in range(1, max_Y):
                tri = self.find_tri(X, Y)
                tri = self.minimize(tri)
                self.add_tri(tri)
            print(f"\rX: {X}  ", end="")
        self.spec_tri.sort()
        print(f"\r{len(self.spec_tri)} special triangles found")
        if show:
            print(*self.spec_tri, sep="\n")
            print("Done!  ","-"*15)

if __name__ == "__main__":
    # Example usage:
    user_X = 10
    user_Y = 10

    finder = SpeTriFinder(user_X, user_Y)

    # Or
    finder.run_finder(5, 5, show=False)

    # Or 
    SpeTriFinder(3, 3)

    # Last one
    big = SpeTriFinder(100, 100, False)
    print(big.spec_tri[-1])
