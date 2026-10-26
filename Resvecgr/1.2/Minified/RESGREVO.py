A0='BACKSPACE'
z=round
l='DOWN'
k='UP'
g='LEFT'
f='RIGHT'
e='SOUTH'
d='NORTH'
c='WEST'
b='EAST'
a=int
X='ENTER'
W='.'
R=str
O=True
N=abs
J=len
import ti_system as q,ti_draw as A,math as H
m=[(255,0,0),(255,126,0),(220,220,0),(0,255,0),(0,0,255),(133,0,255)]
r={'A':[82,40,850,16424],'B':[82,39,850,1618,16420,17444],'C':[98,39,1634],'D':[82,39,1618,16678],'E':[98,40,866,1634],'F':[98,40,866],'G':[98,39,9026,1618,17189],'H':[40,850,16424],'I':[98,8232,1634],'J':[98,8232,1602],'K':[40,850,16420,17444],'L':[39,1634],'M':[40,16424,4386,8738,12578],'N':[40,16424,4386,8738,13090],'O':[82,40,1618,16424],'P':[82,40,850,16421],'Q':[82,40,1602,16422,9250,13602,17954],'R':[82,40,850,16420,17444],'S':[98,37,850,1618,17189],'T':[98,8232],'U':[39,5698,16423],'V':[38,5410,9762,13602,16422],'W':[40,16424,5410,9250,13602],'X':[35,16419,1315,17699,4642,12834,5154,13346,8994],'Y':[34,16418,8742,4386,12578],'Z':[98,1634,1314,5154,8994,12834,16674],'1':[546,4386,8232,1634],'2':[82,1634,1314,5154,8994,12834,16674],'3':[82,850,1618,16675,17443],'4':[37,850,16424],'5':[98,37,850,1618,17443],'6':[98,39,866,1618,17189],'7':[98,16424],'8':[98,39,866,1618,16424],'9':[98,37,850,16424],'0':[82,40,1618,16424,4642,8994,13346],'+':[8486,866],'-':[866],'$':[354,292,850,1362,17188,8232],'/':[1570,5155,8994,12579,16418],W:[9506]}
s=255,0,255
def A1(components):
	I=' OF ';G=' DEGREES ';E=' UNITS ';A=components;F=z((A[0]**2+A[1]**2)**.5,3);D=R(F)[:J(R(F).split(W))+4]
	if A[0]!=0 and A[1]!=0:K=H.atan(N(A[1]/A[0]));B=z(H.degrees(K),3);L=R(B)[:J(R(B).split(W))+4];M=R(90-B)[:J(R(90-B).split(W))+4];C=[b if A[0]>0 else c,d if A[1]>0 else e];return[D+E+L+G+C[1]+I+C[0],D+E+M+G+C[0]+I+C[1]]
	else:O=d if A[1]>0 else b if A[0]>0 else e if A[1]<0 else c;return[D+E+O]
def t(angle,magnitude):B=magnitude;A=angle;return[B*H.cos(A),B*H.sin(A)]
def I(startpt,components,scalar):
	E=scalar;D=components;B=startpt;B=[a(B[0]*E+159),a(-B[1]*E+95)];C=[a(B[0]+D[0]*E),a(B[1]-D[1]*E)];A.draw_line(B[0],B[1],C[0],C[1]);F=H.atan2(D[1],D[0]);I=[t(F+H.pi/4,7.5),t(F-H.pi/4,7.5)]
	for G in I:A.draw_line(C[0],C[1],C[0]-G[0],C[1]+G[1])
def n(text,x,y):
	C=x;E=y
	for D in text:
		if D=='|':E+=8;C=x;continue
		if D in r:
			for B in r[D]:A.fill_rect(C+(B>>12&15)-1,E+(B>>8&15)-1,B>>4&15,B&15)
		C+=6
def Y():
	A=q.wait_key()
	if A==92:return 1
	elif A==93:return 2
	elif A==94:return 3
	elif A==82:return 4
	elif A==83:return 5
	elif A==84:return 6
	elif A==72:return 7
	elif A==73:return 8
	elif A==74:return 9
	elif A==102:return 0
	elif A==103:return W
	elif A==26:return f
	elif A==24:return g
	elif A==25:return k
	elif A==34:return l
	elif A==105:return X
	elif A==23:return A0
	elif A==45:return'CLEAR'
def F(text,starting_line,col):B=starting_line;C=text.count('|')+1;A.set_color(255,255,255);A.fill_rect(2,180+B*8,315,C*8+1);A.set_color(*col);n(text,3,181+B*8)
def u(writing_line,col):
	A=''
	while O:
		B=Y()
		if type(B)is a or B==W:A+=R(B)
		elif B==A0:A=A[:J(A)-1]
		elif B==X:return A
		F(A,writing_line,col)
def o(starting_line,col):
	D=col;C=starting_line;F('Y  N',C,D);B=O
	while O:
		if B:A.set_color(*D)
		else:A.set_color(255,255,255)
		A.fill_rect(2,188+C*8,6,2)
		if not B:A.set_color(*D)
		else:A.set_color(255,255,255)
		A.fill_rect(20,188+C*8,6,2);E=Y()
		if E==f or E==g:B=not B
		elif E==X:return B
def P():A.set_color(255,255,255);A.fill_rect(2,180,315,50)
def S():A.set_color(255,255,255);A.fill_rect(77,13,165,165);A.set_color(0,0,0);A.fill_rect(158,15,3,161);A.fill_rect(79,94,161,3)
while O:
	v=0;K=[];Q=[0,0];T=[0,0];A.set_color(255,255,255);A.fill_rect(-1,-1,321,241)
	while O:
		C=m[v];S();F('WHAT IS THE LENGTH OF THE VECTOR?',0,C);U=float(u(1,C));P();F('DOES THE ANGLE LIE ON AN AXIS?',0,C);A2=o(1,C)
		if A2:
			P();F('CHOOSE THE AXIS',0,C);B=1
			while O:
				S();A.set_color(*C)
				if B==1:A.fill_rect(158,15,3,79)
				elif B==2:A.fill_rect(161,94,79,3)
				elif B==3:A.fill_rect(158,97,3,79)
				elif B==4:A.fill_rect(79,94,79,3)
				F(d if B==1 else b if B==2 else e if B==3 else c,1,C);D=Y()
				if D==k:B=1
				elif D==f:B=2
				elif D==l:B=3
				elif D==g:B=4
				elif D==X:break
			if B==1:E=[0,U]
			elif B==2:E=[U,0]
			elif B==3:E=[0,-U]
			elif B==4:E=[-U,0]
		else:
			P();F('WHAT IS THE ANGLE OF THE VECTOR?',0,C);L=float(u(1,C));F('CHOOSE A DIRECTION',0,C);G=1
			while O:
				S();A.set_color(*C)
				if G==1:I([.5,.1],[0,.4],80);I([-.5,.1],[0,.4],80)
				elif G==2:I([.1,.5],[.4,0],80);I([.1,-.5],[.4,0],80)
				elif G==3:I([.5,-.1],[0,-.4],80);I([-.5,-.1],[0,-.4],80)
				elif G==4:I([-.1,.5],[-.4,0],80);I([-.1,-.5],[-.4,0],80)
				F(d if G==1 else b if G==2 else e if G==3 else c,1,C);D=Y()
				if D==k:G=1
				elif D==f:G=2
				elif D==l:G=3
				elif D==g:G=4
				elif D==X:break
			P();F('CHOOSE THE INITIAL AXIS',0,C);Z=[1,3]if G%2==0 else[2,4];B=Z[0]
			while O:
				S();A.set_color(*C)
				if B==1:A.fill_rect(158,15,3,79)
				elif B==2:A.fill_rect(161,94,79,3)
				elif B==3:A.fill_rect(158,97,3,79)
				elif B==4:A.fill_rect(79,94,79,3)
				F(d if B==1 else b if B==2 else e if B==3 else c,1,C);D=Y()
				if D==k and 1 in Z:B=1
				elif D==f and 2 in Z:B=2
				elif D==l and 3 in Z:B=3
				elif D==g and 4 in Z:B=4
				elif D==X:break
			if B==1 or B==3:L=9e1-L
			V=[B,G]
			if 1 in V and 4 in V:L=180-L
			elif 3 in V and 4 in V:L+=180
			elif 3 in V and 2 in V:L=360-L
			E=[U*H.cos(H.radians(L)),U*H.sin(H.radians(L))]
		S();P();A.set_color(*C);I([0,0],E,80/(N(E[0])if N(E[0])>N(E[1])else N(E[1])));F('DOES THIS LOOK CORRECT?',0,C)
		if o(1,C):
			K.append(E);Q[0]+=E[0];Q[1]+=E[1]
			if N(Q[0])>T[0]:T[0]=N(Q[0])
			if N(Q[1])>T[1]:T[1]=N(Q[1])
			v+=1
		P()
		if J(K)>1:
			F('IS THIS THE FINAL VECTOR?',0,C)
			if o(1,C):break
		P()
	S();h=[80/T[0],80/T[1]];w=h[0]if h[0]<h[1]else h[1];A.set_color(0,0,0);A.fill_rect(158,15,3,161);A.fill_rect(79,94,161,3);A.set_pen('medium','solid');i=[0,0];x=0
	for E in K:A.set_color(*m[x]);I(i,E,w);i=[i[0]+E[0],i[1]+E[1]];x+=1
	A.set_color(*s);I([0,0],Q,w);A.set_pen('thin','solid');K.append(Q);y=O;M=J(K)-1
	while y:
		j=A1(K[M]);A.set_color(255,255,255);A.fill_rect(2,180,315,25)
		if M<J(K)-1:C=m[M]
		else:C=s
		A.set_color(*C)
		if J(j)==1:n(j[0],3,181)
		else:n(j[0]+'|OR|'+j[1],3,181)
		p=q.wait_key()
		if p==105:y=False
		elif p==24:
			M-=1
			if M<0:M=J(K)-1
		elif p==26:
			M+=1
			if M>J(K)-1:M=0
	P()