
h = "-"
v = "|"


def drawLine (length, direction):
    if direction == h:
        while length > 0:
            length -= 1
            print("-", end="")
    if direction == v:
        while length > 0:
            length -= 1
            print("|")

drawLine (10, h)
drawLine (5, v)
