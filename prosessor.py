# prosessor-klasse: har state antall kjerner og hastighet

class Prosessor:
	def __init__(self, kjerner, hastighet):
		self._antallKjerner = kjerner
		self._hastighet = hastighet