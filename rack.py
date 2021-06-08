# rack som man kan putte noder i

from node import Node

class Rack:
	def __init__(self, maxNoderPerRack):
		self._noder = []
		self._maxNoderPerRack = maxNoderPerRack
		
	def hentNoder(self):
		return self._noder
		
	# lag ny node basert paa info i parameterne
	def lagNode(self, prosessorer, kjerner, hastighet, minne):
		self._noder.append(Node(prosessorer, kjerner, hastighet, minne))
	
	# sjekke om en rack er full
	def erFull(self):
		if len(self._noder) == self._maxNoderPerRack:
			return True
		else:
			return False