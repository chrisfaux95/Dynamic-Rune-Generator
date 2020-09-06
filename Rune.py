from PIL import Image, ImageDraw
from string import ascii_letters, digits

WHITE = (255,255,255)
BLACK = (0,0,0)
ALPHA = digits + ascii_letters

class RuneGen(object):

	"""docstring for RuneGen"""

	def __init__(self, inx,iny,inw):
		self.x = inx
		self.y = iny
		self.w = inw
		self.points = []
		self.points.append((lambda t: (t.x,t.y)))
		self.lines = []
		self.name = ""


	def set_name(self,s):
		self.name = s

	# add a point to the list of points
	def add_point(self,p):
		self.points.append(p)


	# append a list of points to the existing point list
	def add_point_list(self,pl):
		self.points.extend(pl)


	# Add a line to the list of lines
	def add_line(self,p1,p2):
		self.lines.append((p1,p2))


	def add_line_list(self, line_list):
		self.lines.extend(line_list)


	# LINE MAKER?
	def line_create(self,coord):
		p1 = self.points[coord[0]]
		p2 = self.points[coord[1]]
		self.lines.append((p1,p2))


	def line_gen(self,line_point_list):
		for l in line_point_list:
			self.line_create(l)


	# calculates the current values of the point
	def calculate_point(self,p):
		return p(self)

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
		im.save("images/points_{}.png".format(self.name))


	def draw_lines(self):
		im = Image.new("RGB", self.rune_size(), WHITE)
		dr = ImageDraw.Draw(im)
		for li in self.calculate_line_list():
			dr.line(li,BLACK)
		im.save("images/lines_{}.png".format(self.name))




