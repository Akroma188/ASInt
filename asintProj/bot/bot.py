class bot:
	def __init__(self, building, b_id):
		self.building = building
		self.id = b_id
	def __str__(self):
		return "%d - %s" % (self.id, self.building) 