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

last = (607, 355)
current = (553, 355)
target = (553, 455)

assert(getDirection(last, current, target) == "Left")

last = (553, 355)
current = (553, 455)
target = (503, 455)

assert(getDirection(last, current, target) == "Right")

last = (553, 455)
current = (503, 455)
target = (449, 440)

assert(getDirection(last, current, target) == "Right")

last = (503, 455)
current = (449, 440)
target = (449, 411)

assert (getDirection(last, current, target) == "Left")

last = (449, 440)
current = (449, 411)
target = (416, 232)

assert (getDirection(last, current, target) == "Left")

last = (449, 411)
current = (449, 440)
target = (347, 223)

assert (getDirection(last, current, target) == "Left")

last = (449, 440)
current = (347, 223)
target = (227, 469)

assert (getDirection(last, current, target) == "Left")
