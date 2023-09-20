# This describes an object licensed under CC-BY-NC-SA 4.0
# This code is licensed under the CC-BY-NC-SA 4.0
# By Aria Salvatrice

import cadquery as cq

# Many values hardcoded instead (not expecting to make variants)
width = 53.5 * 2  # 2 breadboards
length = 163  # 1 breadboard
depth = 8  # 1 breadboard
compartmentWidth = 20
compartmentDepth = 6
engravingDepth = 1
pitch = 2.54
componentHole = 1.7
rulerX = 4
rulerY = 8.53

# Base block
holder = cq.Workplane("front").box(width, length, depth)

# Big ruler at the bottom
holeX = rulerX
holeY = rulerY
for row in range(40):
    for col in range(6):
        holder = (
            holder.faces(">Z")
            .workplane()
            .moveTo(holeX + row * pitch - width / 2, holeY + col * pitch - length / 2)
            .rect(componentHole, componentHole)
            .cutBlind(-compartmentDepth)
        )
    if (row + 1) % 5 == 0:  # Graduation
        holder = (
            holder.faces(">Z")
            .workplane()
            .moveTo(
                holeX + row * pitch - width / 2, holeY + col * pitch - length / 2 - 17
            )
            .rect(componentHole, componentHole * 2)
            .cutBlind(-engravingDepth)
        )


# Compartments
def addCompartment(holder, txt, ruler, x, y, boxSize):
    holder = (
        holder.faces(">Z")
        .vertices("<XY")
        .workplane(centerOption="CenterOfMass")
        .moveTo(x, y)
        # Compartment
        .rect(compartmentWidth, boxSize)
        .cutBlind(-compartmentDepth)
        # Label
        .center(x, y - boxSize / 2 - 4.7)
        # .text(txt=txt, fontsize=11, distance=-engravingDepth, font="Nova Flat")
        # forget it - couldn't get it to look good enough
        # Ruler start
        .center(-compartmentWidth / 2 - 2, 4.7 + componentHole / 2)
        .rect(componentHole, componentHole)
        .cutBlind(-compartmentDepth)
    )
    # Ruler middle (less deep)
    for i in range(ruler - 1):
        holder = (
            holder.center(0, pitch)
            .rect(componentHole, componentHole)
            .cutBlind(-engravingDepth)
        )
    # Ruler end
    holder = (
        holder.center(0, pitch)
        .rect(componentHole, componentHole)
        .cutBlind(-compartmentDepth)
    )
    return holder


holder = addCompartment(holder, "1", 1, 16, 36, 16)
holder = addCompartment(holder, "2", 2, 16, 62 - 3.4, 16)
holder = addCompartment(holder, "3", 3, 16, 88 - 3.4 * 2, 16)
holder = addCompartment(holder, "4", 4, 16, 114 - 3.4 * 3, 16)
holder = addCompartment(holder, "5", 5, 16, 140 - 3.4 * 4, 16)
holder = addCompartment(holder, "6", 6, 16, 166 - 3.4 * 5, 16)

holder = addCompartment(holder, "7", 7, 43 - 1.56, 42.5, 29)
holder = addCompartment(holder, "8", 8, 43 - 1.56, 81.5 - 5.6667, 29)
holder = addCompartment(holder, "9", 9, 43 - 1.56, 120.5 - 5.6667 * 2, 29)
holder = addCompartment(holder, "10", 10, 43 - 1.56, 159.5 - 5.6667 * 3, 29)

# A few free compartments
holder = (
    holder.faces(">Z")
    .vertices("<XY")
    .workplane(centerOption="CenterOfMass")
    .moveTo(69 - 1.7, 59.15)
    .rect(compartmentWidth, 62.3)
    .cutBlind(-compartmentDepth)
    .moveTo(69 - 1.7, 125.85)
    .rect(compartmentWidth, 62.3)
    .cutBlind(-compartmentDepth)
    .moveTo(93, 92.5)
    .rect(compartmentWidth, 129)
    .cutBlind(-compartmentDepth)
)

# Holes on the left
holder = (
    holder.faces("<X")
    .workplane(centerOption="CenterOfMass", offset=-2)
    .center(0, -1.5)
    .rect(4.3, 5)
    .cutBlind(2)
    .center(-66.9, 0)
    .rect(4.7, 5)
    .cutBlind(2)
    .center(66.9 * 2, 0)
    .rect(4.7, 5)
    .cutBlind(2)
)

# Notches on the right
holder = (
    holder.faces(">X")
    .workplane(centerOption="CenterOfMass")
    .center(0, -1.5)
    .rect(4, 5)
    .extrude(1.4)
    .center(-66.9, 0)
    .rect(4, 5)
    .extrude(1.4)
    .center(66.9 * 2, 0)
    .rect(4, 5)
    .extrude(1.4)
)
