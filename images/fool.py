import pygame
import random
import time

def inter (x1, y1, x2, y2, db1, db2):
	if x1 > x2 - db1 and x1 < x2 + db2 and y1 > y2 - db1 and y1 < y2 + db2:
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
window = pygame.display.set_mode((800,600))#,pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN)
screen = pygame.Surface((800,600))
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
xc1 = 600
xc = 10
yc = 480

c = 0
	
a = []
aa = []
	
for hhh in range (0,31):
	xc1 += 2
	xcol.append(xc1)
	xrub.append(xc1)

mas = random.randint(1,4)
mast = pygame.image.load ("mast" + str(mas) + ".png")

for g in range (1,36):
	#if j[g] == 37:
		#j[g] = j[36]
	cardfile.append("card" + str(j[g]) + ".png")
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
	

rub = pygame.image.load ('rub.png')
fon = pygame.image.load ('fon.png')
bita = pygame.image.load ('bita.png')


done = False

xm = 54
ym = 572

ii = 1
kk = 1
p = 6

rasp = 180
ind = 0
ind1 = 0
ind2 = 0
l = 0
esh = 7
li = 0

koor = 700

dif = 30

for hh in range (1,37):
	xc += 20
	if hh <= 18:
		xcard.append(xc)
		ycard.append(yc)
	else:
		xcard.append(xc-360)
		ycard.append(20)
	xvrag.append(xc)
	yvrag.append(20)
	xvragru.append(xc)
	yvragru.append(yc-460)
	

while done == False:
	for u in pygame.event.get():
		if u.type == pygame.QUIT:
			done = True
		if u.type == pygame.KEYUP and u.key == pygame.K_ESCAPE:
			done = True
		if u.type == pygame.KEYUP and u.key == pygame.K_RETURN:
			p += 1
	
		l = False
		
	screen.fill ((0,140,0))
	screen.blit(fon, (0,0))
	screen.blit(bita, (610,400))
	screen.blit(mast, (740,270))
	for i in range (c,c+p):
		screen.blit(card[i], (xcard[ii],ycard[ii]))
		screen.blit(card[i+18], (xcard[ii+18],ycard[ii+18]))
		#if ycard[ii+18] == 20 or ycard[ii] == 20 and ycard[ii+18] != 178:
		#	screen.blit(rub, (xcard[ii+18],ycard[ii+18]))
		#if ycard[ii] == 20:
		#	screen.blit(rub, (xcard[ii],ycard[ii]))
			
		
		#yvrag[ind] = rasp
		#yvragru[ind] = 10000
		
		esh += 1
		ii += 1
		if ii == p + 1:
			ii = 1
			esh = 0
		if u.type == pygame.MOUSEBUTTONUP:
				x,y = u.pos
				if ind == 1:
					if inter1 (x,y,xcard[ii],ycard[ii], 20, 81):
						#print ("hello")
						for uu in range (0,35):
							ind2 += 1
							if ind2 == 35:
								ind2 = 0
							if ycard[ind2] == 178 or ycard[ind2] == 260:
								if aa[esh] == aa[uu]:
									ind = 0
				if ind == 0:
					if inter1 (x,y,xcard[ii],ycard[ii], 20, 81): #or inter (x,y,xvrag[ii],yvrag[ii], 1, 20):
						#p += 1
						ind = 1
						
						if y > 400:
							xcard[ii] = dif
							ycard[ii] -= 220
							#print ("\n", a[esh], "\n")
							
							li = 0
							
							for bol in range (18,24+p-6):
								l += 1
								
								if a[bol] == a[esh] and aa[bol] > aa[esh]:
									
									if ycard[l+18] == 178 or ycard[l+18] == -10000:
										pass
									else:
										if li == 0:
											ycard[l+18] = 178
											xcard[l+18] = dif
											xvragru[l] = 10000
											dif += 55
											li = 1
											ind1 = l + 18
											
								if aa[bol] > aa[esh] and a[bol] == mas and a[esh] == mas:
									
									if ycard[l+18] == 178 or ycard[l+18] == -10000:
										pass
									else:
										if li == 0:
											ycard[l+18] = 178
											xcard[l+18] = dif
											xvragru[l] = 10000
											dif += 55
											li = 1
											ind1 = l + 18
											
								if a[bol] == mas and a[esh] != mas:
									
									if ycard[l+18] == 178 or ycard[l+18] == -10000:
										pass
									else:
										if li == 0:
											ycard[l+18] = 178
											xcard[l+18] = dif
											xvragru[l] = 10000
											dif += 55
											li = 1
											ind1 = l + 18
									
		if u.type == pygame.MOUSEBUTTONUP:
			if inter (x,y,610,400,1,105):
				ind = 0
				for boll in range (c, c+p+1):
					if ycard[boll+18] == 178:
						xcard[boll+18] = -10000
						ycard[boll+18] = -10000
						dif = 30
					if ycard[boll] == 260:
						xcard[boll] = -10000
						ycard[boll] = -10000
						dif = 30
						
		if li != 1:
			ind = 0
			for ber in range (0, 34):
				if ycard[ber] == 178 or ycard[ber] == 260:
					ycard[ber] = 20
					xcard[ber] = koor
					koor -= 20
					dif = 30
							
					#if inter (xcard[ii],ycard[ii],xvrag[ind-1],yvrag[ind-1], 96, 96):
				
				
	for k in range (c+p+p, 34):
		screen.blit(card[k], (xcol[k-p],ycol))
		screen.blit(rub, (xrub[k-p],ycol))
	
	window.blit(screen, (0,0))
	pygame.display.update()
pygame.quit()