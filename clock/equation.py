from random import randrange, choice
from math import floor, ceil

OPERATORS = ["+","-","*"]

class TreeNode:

    def __init__(self, left, right, operator):
        self.left = left
        self.right = right
        self.operator = operator

    def __str__(self) -> str:
        return str(self.left) + " " + self.operator + " " + str(self.right)


def generate_equation(numNodes, maxNumber=10):
    if numNodes == 1:
        return randrange(maxNumber-10, maxNumber)

    numLeft = floor(numNodes / 2)
    leftSubTree = generate_equation(numLeft, maxNumber)
    numRight = ceil(numNodes / 2)
    rightSubTree = generate_equation(numRight, maxNumber)

    op = choice(OPERATORS)

    return TreeNode(leftSubTree, rightSubTree, op)

if __name__ == "__main__":
    print(str(generate_equation(3)))