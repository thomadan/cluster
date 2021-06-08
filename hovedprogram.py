# program som lager en regneklynge basert paa info i filen regneklynge.txt

from regneklynge import Regneklynge

# lage ny regneklynge
regneklyngen = Regneklynge()

# skrive ut informasjon om regneklyngen
print('Noder med minst 32 GB:', regneklyngen.noderMedNokMinne(32))
print('Noder med minst 64 GB:', regneklyngen.noderMedNokMinne(64))
print('Noder med minst 128 GB:', regneklyngen.noderMedNokMinne(128))
print()
print('Antall prosessorer:', regneklyngen.antProsessorer())
print('Antall rack:', regneklyngen.hentAntallRacks())
