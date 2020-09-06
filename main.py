# from PointGen import *
from Rune import RuneGen
from math import sqrt, floor
x = 5
y = 5
w = 40

ruMirror = RuneGen(x,y,w)
ruHex = RuneGen(x,y,w)
ruRhombus = RuneGen(x,y,w)

point_list_mirror = [
	lambda t: (t.x,t.y),
	lambda t: (t.x + t.w, t.y),
	lambda t: (t.x, t.y + t.w),
	lambda t: (t.x + t.w, t.y + t.w),
	lambda t: (t.x, t.y + 2 * t.w),
	lambda t: (t.x + t.w, t.y + 2 * t.w)
]

point_list_hex = [
	lambda t: (t.x + t.w//2, t.y),
	lambda t: (t.x + (3*t.w//2), t.y),
	lambda t: (t.x, t.y + floor(sqrt(3)*t.w/2)),
	lambda t: (t.x + t.w, t.y + floor(sqrt(3)*t.w/2)),
	lambda t: (t.x + 2*t.w, t.y + (sqrt(3)*t.w/2)),
	lambda t: (t.x + t.w//2, t.y + floor(sqrt(3)*t.w)),
	lambda t: (t.x + (3*t.w//2), t.y + floor(sqrt(3)*t.w))
]

point_list_rhombus = [
	lambda t: (t.x + t.w//2, t.y),
	lambda t: (t.x, t.y + floor(sqrt(3)*t.w/2)),
	lambda t: (t.x + t.w, t.y + floor(sqrt(3)*t.w/2)),
	lambda t: (t.x + t.w//2, t.y + floor(sqrt(3)*t.w))
]

line_list_mirror = [
	(1,2),
	(1,3),
	(1,4),
	(2,3),
	(2,4),
	(3,4),
	(3,5),
	(3,6),
	(4,5),
	(4,6),
	(5,6)
]

line_list_rhombus = [(1,2),(1,3),(2,3),(2,4),(3,4)]

line_list_hex = [
	(1,2),
	(1,3),
	(1,4),
	(2,4),
	(2,5),
	(3,4),
	(3,6),
	(4,5),
	(4,6),
	(4,7),
	(5,7),
	(6,7)]

# Mirror Rune Setup
ruMirror.add_point_list(point_list_mirror)
ruMirror.set_name("mirror_rune")
ruMirror.line_gen(line_list_mirror)

# Hex Rune Setup
ruHex.add_point_list(point_list_hex)
ruHex.set_name("hex_rune")
ruHex.line_gen(line_list_hex)

# Rhombus Rune Setup
ruRhombus.add_point_list(point_list_rhombus)
ruRhombus.set_name("rhombus_rune")
ruRhombus.line_gen(line_list_rhombus)


# Draw the points
ruHex.draw_points()
ruMirror.draw_points()
ruRhombus.draw_points()

#make a test line
ruMirror.draw_lines()
ruRhombus.draw_lines()
ruHex.draw_lines()
