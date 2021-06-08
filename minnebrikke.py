# minnebrikke-klasse: har state stoerrelse, og har metode for aa returnere stoerrelse

class Minnebrikke:
	def __init__(self, stoerrelse):
		self._stoerrelse = stoerrelse
		
	def hentStoerrelse(self):
		return self._stoerrelse