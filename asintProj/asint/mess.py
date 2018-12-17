class mess:
	def __init__(self, building, user, message, identifier):
		self.building = building
		self.user = user
		self.message = message
		self.id = identifier
	def __str__(self):
		return "%d - %s - %s - %s" % (self.building, self.user, self.message, self.id) 