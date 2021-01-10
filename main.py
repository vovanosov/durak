android = False

try:
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()
    android = True
except ImportError:
    pass

import pygame
if not android:
    import pygame.mixer
import random
import time

def inter (x1, y1, x2, y2, db1, db2, db3):
	if x1 > x2 - db1 and x1 < x2 + db2 and y1 > y2 - db3 and y1 < y2 + db3:
		return 1
	else:
		return 0
		
def inter1 (x1, y1, x2, y2, db2, db1):
	if x1 > x2 and x1 < x2 + db2 and y1 > y2 and y1 < y2 + db1:
		return 1
	else:
		return 0
	
	
def resource_path(relative):
	if hasattr(sys, "_MEIPASS"):
		return os.path.join(sys._MEIPASS, relative)
	return os.path.join(relative)
	
pygame.init()
#window = pygame.display.set_mode((800,600),pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN)
screen = pygame.display.set_mode((800,600))
#screen = pygame.Surface((800,600))
pygame.display.set_caption("FOOL");

cardfile = []
card = []
gg = 0
o = 0
j = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
random.shuffle(j)

for h in range (1,39):
	card.append(h)
	
xcard = []
ycard = []
xvrag = []
yvrag = []
xvragru = []
yvragru = []
xcol = []
xrub = []
ycol = 240
xc1 = 590
xc = 10 #250
yc = 480

ras = 50

c = 0
	
a = []
aa = []


for hhh in range (0,34):
	xc1 += 2
	xcol.append(xc1)
	xrub.append(xc1)

mas = random.randint(1,4)
mast = pygame.image.load ("./images/mast" + str(mas) + ".png")

for g in range (1,36):
	#if j[g] == 37:
		#j[g] = j[36]
	cardfile.append("./images/card" + str(j[g]) + ".png")
	card[gg] = pygame.image.load (cardfile[gg])
	if j[g] == 1:
		a.append(1)
		aa.append(9)
	if j[g] == 2:
		a.append(1)
		aa.append(8)
	if j[g] == 3:
		a.append(1)
		aa.append(7)
	if j[g] == 4:
		a.append(1)
		aa.append(6)
	if j[g] == 5:
		a.append(1)
		aa.append(5)
	if j[g] == 6:
		a.append(1)
		aa.append(4)
	if j[g] == 7:
		a.append(1)
		aa.append(3)
	if j[g] == 8:
		a.append(1)
		aa.append(2)
	if j[g] == 9:
		a.append(1)
		aa.append(1)
		
	if j[g] == 10:
		a.append(2)
		aa.append(9)
	if j[g] == 11:
		a.append(2)
		aa.append(8)
	if j[g] == 12:
		a.append(2)
		aa.append(7)
	if j[g] == 13:
		a.append(2)
		aa.append(6)
	if j[g] == 14:
		a.append(2)
		aa.append(5)
	if j[g] == 15:
		a.append(2)
		aa.append(4)
	if j[g] == 16:
		a.append(2)
		aa.append(3)
	if j[g] == 17:
		a.append(2)
		aa.append(2)
	if j[g] == 18:
		a.append(2)
		aa.append(1)
		
	if j[g] == 19:
		a.append(3)
		aa.append(9)
	if j[g] == 20:
		a.append(3)
		aa.append(8)
	if j[g] == 21:
		a.append(3)
		aa.append(7)
	if j[g] == 22:
		a.append(3)
		aa.append(6)
	if j[g] == 23:
		a.append(3)
		aa.append(5)
	if j[g] == 24:
		a.append(3)
		aa.append(4)
	if j[g] == 25:
		a.append(3)
		aa.append(3)
	if j[g] == 26:
		a.append(3)
		aa.append(2)
	if j[g] == 27:
		a.append(3)
		aa.append(1)
		
	if j[g] == 28:
		a.append(4)
		aa.append(9)
	if j[g] == 29:
		a.append(4)
		aa.append(8)
	if j[g] == 30:
		a.append(4)
		aa.append(7)
	if j[g] == 31:
		a.append(4)
		aa.append(6)
	if j[g] == 32:
		a.append(4)
		aa.append(5)
	if j[g] == 33:
		a.append(4)
		aa.append(4)
	if j[g] == 34:
		a.append(4)
		aa.append(3)
	if j[g] == 35:
		a.append(4)
		aa.append(2)
	if j[g] == 36:
		a.append(4)
		aa.append(1)
	gg += 1
	

rub = pygame.image.load ('./images/rub.png')
fon = pygame.image.load ('./images/fon.png')
bita = pygame.image.load ('./images/bita.png')
menu = pygame.image.load ('./images/menu.png')
next = pygame.image.load ('./images/next.png')
bita1 = pygame.image.load ('./images/bita1.png')
game = pygame.image.load ('./images/game.png')
voice = pygame.image.load ('./images/voice.png')
infa = pygame.image.load ('./images/infa.png')
exit = pygame.image.load ('./images/exit.png')
take = pygame.image.load ('./images/take.png')
take1 = pygame.image.load ('./images/take1.png')
lose = pygame.image.load ('./images/you fool.png')
winer = pygame.image.load ('./images/win.png')
nothing = pygame.image.load ('./images/nothing.png')
voicep = pygame.image.load ('./images/voicep.png')
info1 = pygame.image.load ('./images/info.png')
menuu = pygame.image.load ('./images/menuu.png')
Neww = pygame.image.load ('./images/New.png')
continues = pygame.image.load ('./images/continue.png')
exit1 = pygame.image.load ('./images/exit1.png')
on = pygame.image.load ('./images/on.png')
off = pygame.image.load ('./images/off.png')

done = False

xm = 54
ym = 572

ii = 1
iii = 1
kk = 1
p = 6
p1 = 6

rasp = 180
ind = 0
ind1 = 0
ind2 = 0
l = 0
esh = 7
li = 0

ind0 = 0

kof = 0

koor = 700

otb = 0

dif = 30

vz = 0

ra2 = 0

dif1 = 30

pod1 = 0
pod2 = 0

cas = 10
cas1 = 10

ch = 17

hod = 0
hod2 = 0

mest = 30
mest1 = 30

prop = 1

kn = 0

dob1 = 0

pod6 = 0

dip = 30
dip1 = 30

h3 = 0

h5 = 0
h6 = 0

rif = 30

hod10 = 0
hod15 = 0

odin = 0

doba = 0

win = 0
loser = 0

voic = False

colo = 0

musica = 1

new = 1

voz = 0

zak = 0

lose.set_colorkey((0,255,0))
winer.set_colorkey((0,255,0))

for hh in range (1,37):
	xc += 20
	if hh <= 18:
		xcard.append(xc)
		ycard.append(10000)
		
	else:
		xcard.append(xc-340)
		ycard.append(10000)
	xvrag.append(xc)
	yvrag.append(20)
	xvragru.append(xc)
	yvragru.append(yc-460)
	
	
for i in range (0,6):
	for i in range (0,35):
		if pod1 == 0:
			if ycard[i] == 10000:
				ycard[i] = 60
				xcard[i] = mest
				mest += 20
				
				pod1 = 1
				
	pod1 = 0
			
for i in range (0,6):
	for i in range (0,35):
		if pod2 == 0:
			if ycard[i] == 10000:
				ycard[i] = 480
				xcard[i] = mest1
				mest1 += 20
				prop += 1
				pod2 = 1
				
	pod2 = 0
	


while done == False:
	for u in pygame.event.get():
		if u.type == pygame.QUIT:
			done = True
		if u.type == pygame.KEYUP and u.key == pygame.K_ESCAPE:
			done = True
		# Android back key.
		elif u.type == pygame.KEYDOWN and u.key == pygame.K_AC_BACK:
			done = True
		"""
		if u.type == pygame.KEYUP and u.key == pygame.K_TAB:

			for i in range (0,35):
				if pod1 == 0:
					if ycard[i] == 10000:
						ycard[i] = 60
						xcard[i] = mest
						mest += 20
						prop += 1
						pod1 = 1
						
			pod1 = 0
			
				
		if u.type == pygame.KEYUP and u.key == pygame.K_RETURN:
			
			for i in range (0,35):
				if pod2 == 0:
					if ycard[i] == 10000:
						ycard[i] = 480
						xcard[i] = mest1
						mest1 += 20
						prop += 1
						pod2 = 1
			pod2 = 0
		"""
		
		if voz == 1:
			if musica == 0:
				pygame.mixer.init()
				pygame.mixer.music.load("./images/vozmu.mp3")
				pygame.mixer.music.play()
				
			voz = 0
		
		if u.type == pygame.MOUSEBUTTONDOWN:
			x,y = u.pos
			if inter (x,y,88,17,1,88,15):
				voic = False
				while voic == False:
					for pp in pygame.event.get():
						if pp.type == pygame.MOUSEBUTTONUP:
							x,y = pp.pos
							if inter (x,y,286,240,10,222,50):
								if not android:  # don't play music on android
									musica = 0
								voic = True
							if inter (x,y,286,283,10,222,50):
								musica = 1
								voic = True
						if pp.type == pygame.MOUSEMOTION and not android:
							x,y = pp.pos
							if inter (x,y,286,240,10,222,50):
								screen.blit(on, (285,191))
							if inter (x,y,286,283,10,222,50):
								screen.blit(off, (285,280))
#						window.blit(screen, (0,0))
						screen.blit(voicep, (0,0))
						pygame.display.update()
						
						
			if inter (x,y,176,17,1,88,15):
				info = False
				while info == False:
					for ppp in pygame.event.get():
						if ppp.type == pygame.MOUSEBUTTONUP:
							x,y = ppp.pos
						if inter (x,y,522,504,1,228,63):
							info = True
#						window.blit(screen, (0,0))
						screen.blit(info1, (0,0))
						pygame.display.update()
						
			if inter (x,y,0,17,1,88,15):
				gamee = False
				while gamee == False:
					for pppp in pygame.event.get():
						if pppp.type == pygame.MOUSEMOTION:
							x,y = pppp.pos
							if inter (x,y,182,111,1,228,63):
								screen.blit(Neww, (184,114))
							if inter (x,y,182,250,1,412,63):
								screen.blit(continues, (182,250))
							if inter (x,y,183,387,1,228,63):
								screen.blit(exit1, (184,386))
						if pppp.type == pygame.MOUSEBUTTONUP:
							x,y = pppp.pos
							if inter (x,y,182,111,1,228,63):
								gamee = True
								done = True
								new = 0
							if inter (x,y,182,250,1,228,63):
								gamee = True
							if inter (x,y,183,387,1,228,63):
								gamee = True
								done = True
								new = 1
#						window.blit(screen, (0,0))
						screen.blit(menuu, (0,0))
						pygame.display.update()
			
		if u.type == pygame.MOUSEBUTTONUP:
			x,y = u.pos
			if inter (x,y,610,200,1,105,20):
				if hod == 1:
					if odin == 0:
						for pol in range (0,35):
							if ycard[pol] == 480:
								xcard[pol] = dip
								dip += 20
							if ycard[pol] == 60:
								xcard[pol] = dip1
								dip1 += 20
						dip = 30
						dip1 = 30
						for boll2 in range (0, 35):
							if ycard[boll2] == 177 or ycard[boll2] == 261:
								if odin == 0:
									if hod == 1:
										ycard[boll2] = 480
										h3 = 0
										
										ind0 = 0
										h5 = 0
										odin = 0
							if musica == 0:
								pygame.mixer.init()
								pygame.mixer.music.load("./images/Beri1.mp3")
								pygame.mixer.music.play()
										
						for pol in range (0,35):
							if ycard[pol] == 480:
								xcard[pol] = dip
								dip += 20
							if ycard[pol] == 60:
								xcard[pol] = dip1
								dip1 += 20
						dip = 30
						dip1 = 30
						dif = 30
						otb = 0
						hod = 1
						ind = 2
						h3 = 0
						ind0 = 0
						h5 = 0
						h6 = 0
						rif = 30
				
				
									
		
						
		if u.type == pygame.MOUSEBUTTONUP:
			x,y = u.pos
			if inter (x,y,610,350,1,105,20):
				if musica == 0:
					pygame.mixer.init()
					pygame.mixer.music.load("./images/Bita1.mp3")
					pygame.mixer.music.play()
			if inter (x,y,610,350,1,105,20) and hod == 0 or inter (x,y,610,200,1,105,20) and hod == 1:
				for pod in range (0,35):
					cas = xcard[pod] + 5
					if inter1 (cas,500,xcard[pod],ycard[pod], 20, 81):
						pod6 += 1
						
					
				if pod6 < 6:
					for pod4 in range (pod6,6):
						p += 1
						for i in range (0,35):
							if pod2 == 0:
								if ycard[i] == 10000:
									ycard[i] = 480
									xcard[i] = mest1
									mest1 += 20
									prop += 1
									pod2 = 1
						pod2 = 0
					pod6 = 0
						
				
				for pod5 in range (0,35):
					cas1 = xcard[pod5] + 5
					
					
					if inter1 (cas1,80,xcard[pod5],ycard[pod5], 20, 81):
						pod3 += 1
				
				if pod3 < 6:
					for pod4 in range (pod3,6):
						p1 += 1
						for i in range (0,35):
							if pod1 == 0:
								if ycard[i] == 10000:
									ycard[i] = 60
									xcard[i] = mest
									mest += 20
									prop += 1
									pod1 = 1
						
						pod1 = 0
					
				for pol in range (0,35):
					if ycard[pol] == 480:
						xcard[pol] = dip
						dip += 20
					if ycard[pol] == 60:
						xcard[pol] = dip1
						dip1 += 20
				dip = 30
				dip1 = 30
				
				
				
				
		if doba == 1:
			for pod in range (0,35):
				cas = xcard[pod] + 5
				if inter1 (cas,500,xcard[pod],ycard[pod], 20, 81):
					pod6 += 1
					
				
			if pod6 < 6:
				for pod4 in range (pod6,6):
					p += 1
					for i in range (0,35):
						if pod2 == 0:
							if ycard[i] == 10000:
								ycard[i] = 480
								xcard[i] = mest1
								mest1 += 20
								prop += 1
								pod2 = 1
					pod2 = 0
				pod6 = 0
					
			
			for pod5 in range (0,35):
				cas1 = xcard[pod5] + 5
				
				
				if inter1 (cas1,80,xcard[pod5],ycard[pod5], 20, 81):
					pod3 += 1
			
			if pod3 < 6:
				for pod4 in range (pod3,6):
					p1 += 1
					for i in range (0,35):
						if pod1 == 0:
							if ycard[i] == 10000:
								ycard[i] = 60
								xcard[i] = mest
								mest += 20
								prop += 1
								pod1 = 1
					
					pod1 = 0
				
			for pol in range (0,35):
				if ycard[pol] == 480:
					xcard[pol] = dip
					dip += 20
				if ycard[pol] == 60:
					xcard[pol] = dip1
					dip1 += 20
			dip = 30
			dip1 = 30
			
			doba = 0
				
			#print (p1-6)
						
	if prop == 31:
		done = True
		
		l = False
		
	
	pod6 = 0
	cas = 15
	cas1 = 35
	pod1 = 0
	pod3 = 0
	loser = 0
	win = 0
	screen.fill ((0,140,0))
	#screen.blit(fon, (0,0))
	screen.blit(bita, (610,350))
	screen.blit(take, (610,200))
	screen.blit(menu, (0,0))
	screen.blit(mast, (740,270))
	if u.type == pygame.MOUSEBUTTONDOWN:
		x,y = u.pos
		if inter (x,y,610,350,1,105,20):
			screen.blit(bita1, (610,350))
		if inter (x,y,610,200,1,105,20):
			screen.blit(take1, (610,200))
		
			
	if u.type == pygame.MOUSEMOTION and not android:
		x,y = u.pos
		if inter (x,y,0,17,1,88,15):
			screen.blit(game, (0,17))
		if inter (x,y,88,17,1,88,15):
			screen.blit(voice, (88,17))
		if inter (x,y,176,17,1,88,15):
			screen.blit(infa, (176,17))
		if inter (x,y,772,3,1,23,11):
			screen.blit(exit, (772,3))
			
			
			
	for iii in range (0,35):
		screen.blit(card[iii], (xcard[iii],ycard[iii]))
		if ii >= 35:
			ii = 1
		if ycard[iii] == 480:
			ii += 1
			
		if ycard[iii] == 60:
			screen.blit(rub, (xcard[iii],ycard[iii]))
		#print (ii)
		
		if u.type == pygame.MOUSEBUTTONUP:
			kof = 1
			x,y = u.pos
			if hod == 0:
				if ind == 1:
					if inter1 (x,y,xcard[iii],ycard[iii], 20, 81):
						#print ("hello")
						for uu in range (0,35):
							ind2 += 1
							if ind2 == 35:
								ind2 = 0
							if ycard[ind2] == 178 or ycard[ind2] == 260:
								if aa[iii] == aa[ind2]:
									ind = 0
							
			if hod == 0:
				if ind == 0:
					if inter1 (x,y,xcard[iii],ycard[iii], 20, 81): #or inter (x,y,xvrag[ii],yvrag[ii], 1, 20):
						#p += 1
						#print (iii)
						if y > 400:
							#print (y)
							ind = 1
							vz = 0
							kof = 0
							#otb += 1
							xcard[iii] = dif 
							ycard[iii] -= 220
							#print ("\n", a[esh], "\n")
							
							li = 0
							l = 0
							
							for bol in range (0,35):
								l += 1
								if l == 35:
									l = 0
						
								if a[l] == a[iii] and aa[l] > aa[iii]:
								
									if ycard[l] == 60:
									
										if li == 0:
											vz = 1
											otb += 1
											ycard[l] += 118
											xcard[l] = dif
											xvragru[l] = 10000
											dif += 55
											li = 1
											ind1 = l + 18
											l = 0
											bol = 0
											
											
								if aa[l] > aa[iii] and a[l] == mas and a[iii] == mas:
									
									if ycard[l] == 60:
										if li == 0:
											vz = 1
											otb += 1
											ycard[l] += 118
											xcard[l] = dif
											xvragru[l] = 10000
											dif += 55
											li = 1
											ind1 = l + 18
											l = 0
											bol = 0
											
							if li < 1:
								l = 0
								for bol in range (0,35):
									l += 1
									if l == 35:
										l = 0
										
									if a[l] == mas and a[iii] != mas:
										
										if ycard[l] == 60:
											if li == 0:
												vz = 1
												otb += 1
												ycard[l] += 118
												xcard[l] = dif
												xvragru[l] = 10000
												dif += 55
												li = 1
												ind1 = l + 18
												l = 0
												bol = 0
											
			if hod == 1:
				if ind0 == 1:
					
					for h0 in range (0,35):
						if ycard[h0] == 60:
							for h10 in range (0,35):
								if aa[h0] == aa[h10]:
									if hod10 == 0:
										if ycard[h10] == 177 or ycard[h10] == 261:
											zak += 1
											
											rif += 55
											ycard[h0] = 177
											xcard[h0] = rif
											hod10 = 1
											ind0 = 0
					if ind0 != 0 or hod10 != 1 or zak == 4:
						for jj in range (0,35):
							if ycard[jj] == 177 or ycard[jj] == 261:
								ycard[jj] = 5000
								zak = 0
						hod = 0
						ind = 0
						doba = 1
						if musica == 0:
							pygame.mixer.init()
							pygame.mixer.music.load("./images/Bita1.mp3")
							pygame.mixer.music.play()

				if ind0 == 0:
				
					hod10 = 0
					
						
					for h2 in range (0,36):
						if h3 == 0:
							
							if ycard[h5] == 60:
								ycard[h5] = 177
								h3 = 1
							
								
						
						h5 += 1
						if h5 == 35:
							h5 = 0
						
								
					for h4 in range (0,36):
						h6 += 1
						if h6 == 35:
							h6 = 0
						if u.type == pygame.MOUSEBUTTONUP:
							x,y = u.pos
							if inter1 (x,y,xcard[h6],ycard[h6], 20, 81) and ycard[h6] == 480:
								for h7 in range (0,35):
									if ycard[h7] == 177 and xcard[h7] == rif:
										if a[h6] == a[h7] and aa[h6] > aa[h7]:
											ycard[h6] = 261
											xcard[h6] = rif
											
											ind0 = 1
										if aa[h6] > aa[h7] and a[h6] == mas and a[h7] == mas:
											ycard[h6] = 261
											xcard[h6] = rif
											
											ind0 = 1
										if a[h6] == mas and a[h7] != mas:
											ycard[h6] = 261
											xcard[h6] = rif
											
											ind0 = 1
											
						
								
									
									
		for zab in range (0,34):
			if ycard[zab] == 260:
				kof = 0
				for zab1 in range (0,35):
					if ycard[zab1] == 178 and xcard[zab1] == xcard[zab]:
						kof = 1
				
						
		#for per in range (0,35):
		#	if dif1 == 0:
		#		if ycard[per] == 480 and xcard[per+1] - xcard[per] != 20:
		#			print ("hello")
		#			xcard[per+1] -= 20
		#			dif1 = 1
									

						
						

		if u.type == pygame.MOUSEBUTTONUP:
			if inter (x,y,610,350,1,105,20):
				
				for boll in range (0, 35):
					if ycard[boll] == 178:
						xcard[boll] = -5000
						ycard[boll] = 5000
						dif = 30
						otb = 0
						hod = 1
						ind = 2
						h3 = 0
						ind = 0
						otb = 0
						ind0 = 0
						h5 = 0
						h6 = 0
						rif = 30
					if ycard[boll] == 260:
						xcard[boll] = -5000
						ycard[boll] = 5000
						dif = 30
						otb = 0
						hod = 1
						ind = 2
						ind0 = 0
						otb = 0
						
		
		
		if done == True and new == 0:
			cardfile = []
			card = []
			gg = 0
			o = 0
			j = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
			random.shuffle(j)

			for h in range (1,39):
				card.append(h)
				
			xcard = []
			ycard = []
			xvrag = []
			yvrag = []
			xvragru = []
			yvragru = []
			xcol = []
			xrub = []
			ycol = 240
			xc1 = 590
			xc = 10 #250
			yc = 480

			ras = 50

			c = 0
				
			a = []
			aa = []
				
			for hhh in range (0,34):
				xc1 += 2
				xcol.append(xc1)
				xrub.append(xc1)

			mas = random.randint(1,4)
			mast = pygame.image.load ("./images/mast" + str(mas) + ".png")

			for g in range (1,36):
				#if j[g] == 37:
					#j[g] = j[36]
				cardfile.append("./images/card" + str(j[g]) + ".png")
				card[gg] = pygame.image.load (cardfile[gg])
				if j[g] == 1:
					a.append(1)
					aa.append(9)
				if j[g] == 2:
					a.append(1)
					aa.append(8)
				if j[g] == 3:
					a.append(1)
					aa.append(7)
				if j[g] == 4:
					a.append(1)
					aa.append(6)
				if j[g] == 5:
					a.append(1)
					aa.append(5)
				if j[g] == 6:
					a.append(1)
					aa.append(4)
				if j[g] == 7:
					a.append(1)
					aa.append(3)
				if j[g] == 8:
					a.append(1)
					aa.append(2)
				if j[g] == 9:
					a.append(1)
					aa.append(1)
					
				if j[g] == 10:
					a.append(2)
					aa.append(9)
				if j[g] == 11:
					a.append(2)
					aa.append(8)
				if j[g] == 12:
					a.append(2)
					aa.append(7)
				if j[g] == 13:
					a.append(2)
					aa.append(6)
				if j[g] == 14:
					a.append(2)
					aa.append(5)
				if j[g] == 15:
					a.append(2)
					aa.append(4)
				if j[g] == 16:
					a.append(2)
					aa.append(3)
				if j[g] == 17:
					a.append(2)
					aa.append(2)
				if j[g] == 18:
					a.append(2)
					aa.append(1)
					
				if j[g] == 19:
					a.append(3)
					aa.append(9)
				if j[g] == 20:
					a.append(3)
					aa.append(8)
				if j[g] == 21:
					a.append(3)
					aa.append(7)
				if j[g] == 22:
					a.append(3)
					aa.append(6)
				if j[g] == 23:
					a.append(3)
					aa.append(5)
				if j[g] == 24:
					a.append(3)
					aa.append(4)
				if j[g] == 25:
					a.append(3)
					aa.append(3)
				if j[g] == 26:
					a.append(3)
					aa.append(2)
				if j[g] == 27:
					a.append(3)
					aa.append(1)
					
				if j[g] == 28:
					a.append(4)
					aa.append(9)
				if j[g] == 29:
					a.append(4)
					aa.append(8)
				if j[g] == 30:
					a.append(4)
					aa.append(7)
				if j[g] == 31:
					a.append(4)
					aa.append(6)
				if j[g] == 32:
					a.append(4)
					aa.append(5)
				if j[g] == 33:
					a.append(4)
					aa.append(4)
				if j[g] == 34:
					a.append(4)
					aa.append(3)
				if j[g] == 35:
					a.append(4)
					aa.append(2)
				if j[g] == 36:
					a.append(4)
					aa.append(1)
				gg += 1
				

			rub = pygame.image.load ('./images/rub.png')
			fon = pygame.image.load ('./images/fon.png')
			bita = pygame.image.load ('./images/bita.png')
			menu = pygame.image.load ('./images/menu.png')
			next = pygame.image.load ('./images/next.png')
			bita1 = pygame.image.load ('./images/bita1.png')
			game = pygame.image.load ('./images/game.png')
			voice = pygame.image.load ('./images/voice.png')
			infa = pygame.image.load ('./images/infa.png')
			exit = pygame.image.load ('./images/exit.png')
			take = pygame.image.load ('./images/take.png')
			take1 = pygame.image.load ('./images/take1.png')
			lose = pygame.image.load ('./images/you fool.png')
			winer = pygame.image.load ('./images/win.png')
			nothing = pygame.image.load ('./images/nothing.png')

			done = False

			xm = 54
			ym = 572

			ii = 1
			iii = 1
			kk = 1
			p = 6
			p1 = 6

			rasp = 180
			ind = 0
			ind1 = 0
			ind2 = 0
			l = 0
			esh = 7
			li = 0

			ind0 = 0

			kof = 0

			koor = 700

			otb = 0

			dif = 30

			vz = 0

			ra2 = 0

			dif1 = 30

			pod1 = 0
			pod2 = 0

			cas = 10
			cas1 = 10

			ch = 17

			hod = 0
			hod2 = 0

			mest = 30
			mest1 = 30

			prop = 1

			kn = 0

			dob1 = 0

			pod6 = 0

			dip = 30
			dip1 = 30

			h3 = 0

			h5 = 0
			h6 = 0

			rif = 30

			hod10 = 0
			hod15 = 0

			odin = 0

			doba = 0

			win = 0
			loser = 0
			i = 0
			hh = 0
			colo = 0
			iii = 0
			ii = 0
			
			voz = 0
			
			done = False
			
			

			lose.set_colorkey((0,255,0))
			winer.set_colorkey((0,255,0))

			for hh in range (1,37):
				xc += 20
				if hh <= 18:
					xcard.append(xc)
					ycard.append(10000)
					
				else:
					xcard.append(xc-340)
					ycard.append(10000)
				xvrag.append(xc)
				yvrag.append(20)
				xvragru.append(xc)
				yvragru.append(yc-460)
				
				
			for i in range (0,6):
				for i in range (0,35):
					if pod1 == 0:
						if ycard[i] == 10000:
							ycard[i] = 60
							xcard[i] = mest
							mest += 20
							
							pod1 = 1
							
				pod1 = 0
						
			for i in range (0,6):
				for i in range (0,35):
					if pod2 == 0:
						if ycard[i] == 10000:
							ycard[i] = 480
							xcard[i] = mest1
							mest1 += 20
							prop += 1
							pod2 = 1
							
				pod2 = 0
				
		for ww in range (0,35):
			if ycard[ww] == 240:
				colo = 1
		
		if colo == 0:
			for w in range (0,35):
				if ycard[w] == 60 or ycard[w] == 177 or  ycard[w] == 178:
					win = 1
				if ycard[w] == 480 or ycard[w] == 260 or ycard[w] == 261:
					loser = 1
		colo = 0
		
					
		if loser == 0 and win == 0:
			screen.blit (nothing, (0,0))
#			window.blit(screen, (0,0))
			pygame.display.update()
			if musica == 0:
				pygame.mixer.init()
				pygame.mixer.music.load("./images/Nothing.mp3")
				pygame.mixer.music.play()
			time.sleep(3)
			done = True
			new = 0
				
		if win == 0 and loser > 0:
			time.sleep(1)
			
			screen.blit (lose, (0,0))
#			window.blit(screen, (0,0))
			pygame.display.update()
			if musica == 0:
				pygame.mixer.init()
				pygame.mixer.music.load("./images/losecard.mp3")
				pygame.mixer.music.play()
			time.sleep(3)
			
			done = True
			new = 0
			
		
				
		if loser == 0 and win > 0:
			
			screen.blit (winer, (0,0))
#			window.blit(screen, (0,0))
			pygame.display.update()
			if musica == 0:
				pygame.mixer.init()
				pygame.mixer.music.load("./images/Winn.mp3")
				pygame.mixer.music.play()
			time.sleep(3)
			done = True
			new = 0
			
		loser = 0
		win = 0
									

							
					
					
		if u.type == pygame.MOUSEBUTTONUP:
			if inter (x,y,772,3,1,24,20):
				done = True
				new = 1

		if kof != 1 or vz == 0:
			ind = 0
			
			#screen.blit(next, (610,400))
			
			for ber in range (0, 35):
				if ycard[ber] == 178 or ycard[ber] == 260:
					ycard[ber] = 60
					xcard[ber] = koor
					koor -= 20
					dif = 30
					doba = 1
					voz = 1
					
					
				
	for k in range (prop+4, 34):
		
		#screen.blit(card[k], (xcol[k-p], 240))
		screen.blit(rub, (xrub[k],240))
	
	
	
	
	
#	window.blit(screen, (0,0))
#	pygame.display.update()
	pygame.display.flip()

pygame.quit()
