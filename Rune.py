from PIL import Image, ImageDraw
from math import floor, sqrt

WHITE = (255,255,255)
BLACK = (0,0,0)

class RuneGen(object):

	""" A Class for generating runic designs and spritesheets of them
	based upon geometric relationships """

	def __init__(self, inx, iny, inw):
		self.x = inx
		self.y = iny
		self.w = inw
		self.points = []
		self.points.append('x, y')
		self.lines = []
		self.name = ""


	def set_name(self,s):
		self.name = s

	# function to add a point to the list of points
	def add_point(self,p):
		self.points.append(p)


	# function to append a list of points to the existing point list
	def add_point_list(self,pl):
		self.points.extend(pl)


	# Function to add a line relationship to the list of lines
	def add_line(self,p1,p2):
		self.lines.append((p1,p2))

	# function to add a list of line relationships to the list of lines
	def add_line_list(self, line_list):
		self.lines.extend(line_list)


	# LINE MAKER?
	def line_create(self,coord):
		p1 = self.points[coord[0]]
		p2 = self.points[coord[1]]
		self.lines.append((p1,p2))


	def line_gen(self, line_point_list):
		for l in line_point_list:
			self.line_create(l)


	# calculates the current values of the point
	def calculate_point(self, point):
		point_calc = lambda x, y, w: eval(point)
		return point_calc(self.x, self.y, self.w)

	# calculates the entire list
	def calculate_point_list(self):
		return [self.calculate_point(p) for p in self.points]


	def calculate_line(self,l):
		return self.calculate_point(l[0]),self.calculate_point(l[1])


	def calculate_line_list(self):
		return [self.calculate_line(l) for l in self.lines]


	def rune_dimensions(self):
		c = self.calculate_point_list()
		max_x = max(c, key = lambda i: i[0])[0]
		min_x = min(c, key = lambda i: i[0])[0]
		# print("x: ", max_x,min_x)
		max_y = max(c, key = lambda i: i[1])[1]
		min_y = min(c, key = lambda i: i[1])[1]
		# print("y: ", max_y,min_y)
		x = max_x - min_x
		y = max_y - min_y
		return (x, y)


	def rune_size(self):
		(x_wid, y_wid) = self.rune_dimensions()
		x_wid += self.x * 2
		y_wid += self.y * 2
		return (x_wid, y_wid)


	def draw_points(self):
		im = Image.new("RGB", self.rune_size(), WHITE)
		dr = ImageDraw.Draw(im)
		dr.point(self.calculate_point_list(),BLACK)
		im.save(F"images/points_{self.name}.png")


	def draw_lines(self):
		im = Image.new("RGB", self.rune_size(), WHITE)
		dr = ImageDraw.Draw(im)
		for li in self.calculate_line_list():
			dr.line(li,BLACK)
		im.save(F"images/lines_{self.name}.png")




