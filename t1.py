import math


def getDirection(last, current, target):
    tgtx, tgty = target
    lstx, lsty = last
    curx, cury = current

    tgtx = tgtx - lstx
    tgty = tgty - lsty
    curx = curx - lstx
    cury = cury - lsty
    lstx = 0
    lsty = 0
    invert_direction = False
    if curx < 0:
        invert_direction = True
    normaly = (tgty/tgtx)*curx
    if cury < normaly:
        if invert_direction:
            return "Right"
        return "Left"
    if invert_direction:
        return "Left"
    return "Right"

last = (0, 0)
current = (6, 0)
target = (7, 1)

assert(getDirection(last, current, target) == "Left")

last = (0, 4)
current = (6, 4)
target = (9, 2)

assert(getDirection(last, current, target) == "Right")

last = (9, 0)
current = (6, 0)
target = (4, 1)

assert(getDirection(last, current, target) == "Right")

last = (9, 9)
current = (6, 8)
target = (4, 1)

assert (getDirection(last, current, target) == "Left")
