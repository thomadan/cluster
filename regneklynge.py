from rack import Rack

class Regneklynge:
	def __init__(self):
		self._racks = []
		fil = open('regneklynge.txt')		# apne fil med informasjon om regneklyngen
		linje = fil.readline()				# lese foerste linje, som er antall noder per rack
		self._maxNoderPerRack = int(linje)
		
		# lage noder basert paa informasjon fra filen, linje for linje, saa lenge det finnes linjer
		while linje:
			linje = fil.readline()
			if linje != '':
				linjebiter = linje.split(' ')		
				for i in range(0, int(linjebiter[0])):
					self.leggTilNode(int(linjebiter[2]), 1, 3000, int(linjebiter[1]))
	
	def leggTilNode(self, prosessorer, kjerner, hastighet, minne):
		# hvis det ikke finnes racks, eller alle racks er fulle ..
		if len(self._racks) == 0 or self._racks[len(self._racks) - 1].erFull():
			# .. lage ny rack
			self._racks.append(Rack(self._maxNoderPerRack))
		# lag ny node i ledige rack, som er den siste som ble lagt til regneklyngen
		self._racks[len(self._racks) - 1].lagNode(prosessorer, kjerner, hastighet, minne)
		
	def hentAntallRacks(self):	
		return len(self._racks)
		
	def antProsessorer(self):
		prosessorAntall = 0
		# telle gjennom alle racks ..
		for rack in self._racks:
			# .. og alle noder ..
			for node in rack.hentNoder():
				# .. og finne antall prosessorer i hver node
				prosessorAntall += len(node.hentProsessorer())
		return prosessorAntall
		
	def noderMedNokMinne(self, paakrevdMinne):
		nokMinneAntall = 0
		# se gjennom alle racks ..
		for rack in self._racks:
			# .. og alle noder .. 
			for node in rack.hentNoder():
				# .. og alle minnebrikker ..
				for minnebrikke in node.hentMinnebrikker():
					# .. for om det er nok minne i en minnebrikke
					if minnebrikke.hentStoerrelse() >= paakrevdMinne:
						nokMinneAntall += 1
		return nokMinneAntall
						