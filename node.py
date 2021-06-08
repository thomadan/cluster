
from prosessor import Prosessor
from minnebrikke import Minnebrikke

# klassen node som tar parametere informasjon om prosessor og minne
class Node:
	def __init__(self, prosessorer, kjerner, hastighet, minne):
		self._prosessorer = []
		# legge til prosessorer
		for i in range(0, prosessorer):
			self._prosessorer.append(Prosessor(kjerner, hastighet))
		self._minnebrikker = []
		self._minnebrikker.append(Minnebrikke(minne))
		self._maxMinne = 1024
		
	def hentProsessorer(self):
		return self._prosessorer
		
	def hentMinnebrikker(self):
		return self._minnebrikker
	