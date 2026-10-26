z='acsc'
y=range
q=None
p='='
o='l'
n='a'
m='y'
l='x'
k='asec'
j='cot'
i='&'
f='sec'
e='csc'
d=False
a=''
Y='e'
V='log'
S='('
R='func'
Q='0'
P=')'
O='-1'
N=int
L='/'
K='1'
I='^'
H='+'
F=str
E='-'
D=type
B='*'
class A:
	val=a;children_nodes=[];abs_val=d
	def __init__(A,val,children,abs_val=d):A.val=val;A.children_nodes=children;A.abs_val=abs_val
	def __str__(G):
		O=' ';M=G.children_nodes[0];N=G.children_nodes[1];C=F(M);J=F(N)
		if G.val==L:
			if D(M)is not F:C=S+C+P
			if D(N)is not F:J=S+J+P
		elif G.val==B:
			if D(M)is A:
				if M.val==H or M.val==E:C=S+C+P
			elif len(C.lstrip(E))==1:C=C.replace(K,a)
			if D(N)is A:
				if N.val==H or N.val==E:J=S+J+P
				if D(M)is F:
					if X(M):return C+J
			elif D(N)is F:
				if D(M)is A:
					Q=M.children_nodes[1]
					if D(Q)is A:
						if Q.val==I:return C+' * '+J
				if not N.lstrip(E).isdigit():return C+J
		elif G.val==I or G.val==E:
			if D(M)is A:C=S+C+P
			if D(N)is A:J=S+J+P
		elif G.val==R:return C+S+J+P
		elif G.val==V:
			if J==Y:return'ln('+C+P
			else:return'log('+C+','+J+P
		if not G.abs_val:return C+(O+G.val+O if G.val!=I else G.val)+J
		else:return'| '+C+(O+G.val+O if G.val!=I else G.val)+J+' |'
def X(x):return x.lstrip(E).isdigit()or x==Y or x==i
r=S+input("Enter an equation. (Don't use the regular x. Use the x/y found by pressing alpha + sto->/1 respectively)\n").replace('**',I).replace(')(',B).replace('1/sin',e).replace('1/cos',f).replace('1/tan',j).replace('1/asin',z).replace('1/acos',k).replace('1/atan','acot').replace('pi',i)+P
T=a
b=a
for J in r:
	if(J.lstrip(E).isdigit()and not b.lstrip(E).isdigit()or b.lstrip(E).isdigit()and not J.lstrip(E).isdigit()or(J==l or J==m or J=='s'or J=='c'or J=='t'or J==n or J==o))and X(b)and J!=I and J!=H and J!=E and J!=B and J!=L and J!=P and J!=p:T+=B
	T+=J;b=J
T=T.split(p)
for s in y(len(T)):T[s]=S+T[s]+P
g=0
C=0
def G():global C;return T[g][C:C+1]
def W(other_side=d):
	global C;global g
	if other_side:
		if p in r:C=0;g+=1
		else:return
	B=t()
	while G()==H or G()==E:D=G();C+=1;F=t();B=A(D,[B,F])
	return B
def t():
	global C;D=u()
	while G()==B or G()==L:E=G();C+=1;F=u();D=A(E,[D,F])
	return D
def u():
	global C;B=v()
	if G()==I:D=G();C+=1;E=v();B=A(D,[B,E])
	return B
def v():
	global C;B=a
	if X(G()):
		while X(G()):B+=G();C+=1
		return B
	if G()==l or G()==m:B+=G();C+=1;return B
	I=[n,'s','c','t'];E=G()
	if E in I:
		for L in y(4 if E==n else 2 if E==o else 3):B+=G();C+=1
		C+=1;return A(R,[B,W()])
	if E==o:
		C+=1
		if G()=='n':C+=2;F=W();return A(V,[F,Y])
		if G()=='o':C+=3;F=W();C+=1;J=W();return A(V,[F,J])
	if G()==S or G()=='|':
		K=G()=='|';C+=1;H=W()
		if D(H)is A:H.abs_val=K
		C+=1;return H
def M(node_o):
	h='atan';g='asin';d='tan';c='cos';b='sin';U='2';C=node_o
	if D(C)is A:
		if C.val==H or C.val==E:return A(C.val,[M(C.children_nodes[0]),M(C.children_nodes[1])])
		elif C.val==B:S=C.children_nodes[0];Z=M(S);T=C.children_nodes[1];a=M(T);return A(H,[A(B,[Z,T]),A(B,[S,a])])
		elif C.val==L:S=C.children_nodes[0];Z=M(S);T=A(I,[C.children_nodes[1],O]);a=M(T);return A(H,[A(B,[Z,T]),A(B,[S,a])])
		elif C.val==I:
			if D(C.children_nodes[1])is F:
				if X(C.children_nodes[1]):
					P=C.children_nodes[1]
					if D(P)is A:
						if P.val==L:W=P.children_nodes;W[0]=F(N(W[0])-N(W[1]));P=A(L,*W)
					else:P=F(N(P)-1)
					return A(B,[A(B,[C.children_nodes[1],A(I,[C.children_nodes[0],P])]),M(C.children_nodes[0])])
				else:return A(B,[A(B,[A(V,[C.children_nodes[0],Y]),A(I,[C.children_nodes[0],C.children_nodes[1]])]),M(C.children_nodes[1])])
			else:return A(B,[A(B,[A(V,[C.children_nodes[0],Y]),A(I,[C.children_nodes[0],C.children_nodes[1]])]),M(C.children_nodes[1])])
		elif C.val==R:
			J=C.children_nodes[0];G=C.children_nodes[1]
			if J==b:C=A(R,[c,G])
			elif J==c:C=A(B,[O,A(R,[b,G])])
			elif J==d:C=A(I,[A(R,[f,G]),U])
			elif J==e:C=A(B,[O,A(B,[A(R,[e,G]),A(R,[j,G])])])
			elif J==f:C=A(B,[A(R,[f,G]),A(R,[d,G])])
			elif J==j:C=A(B,[O,A(I,[A(R,[e,G]),U])])
			elif J==g or J=='acos':return A(B,[K if J==g else O,A(L,[M(G),A(I,[A(E,[K,A(I,[G,2])]),A(L,[K,U])])])])
			elif J==k or J==z:return A(B,[K if J==k else O,A(L,[M(G),A(B,[A(H,[Q,G],True),A(I,[A(E,[A(I,[G,U]),K]),A(L,[K,U])])])])])
			elif J==h or J=='acot':return A(B,[K if J==h else O,A(L,[M(G),A(H,[K,A(I,[G,2])])])])
			return A(B,[C,M(G)])
		elif C.val==V:return A(L,[M(C.children_nodes[0]),A(B,[A(V,[C.children_nodes[1],Y]),C.children_nodes[0]])])
	elif C==l or C==m:return C+"'"
	elif X(C):return Q
def c(node_o,negative=d):
	F=negative;C=node_o
	if D(C)is A:
		if C.val==H or C.val==E:G=[];G.extend(c(C.children_nodes[0],F));G.extend(c(C.children_nodes[1],C.val==E and not F or C.val==H and F));return G
		elif not F:return[C]
		else:return[A(B,[O,C])]
	elif not F:return[C]
	else:return[A(B,[O,C])]
def U(node_o):
	B=node_o
	if D(B)is A:C=U(B.children_nodes[0]);E=U(B.children_nodes[1]);return C or E
	elif D(B)is F:return B=="y'"
def h(node_o):
	B=node_o
	if D(B)is A:C=h(B.children_nodes[0]);E=h(B.children_nodes[1]);B.children_nodes[0]=C;B.children_nodes[1]=E;return B
	elif D(B)is F:
		if B=="y'":return K
		else:return B
def A0(left,right):
	I=Q;J=Q;K=c(left)
	for G in K:
		if U(G):
			C=G.children_nodes[0];F=G.children_nodes[1]
			if G.val==B:
				if D(C)is A and U(C):
					if C.val==H:K.extend([A(B,[C.children_nodes[0],F]),A(B,[C.children_nodes[1],F])]);continue
					if C.val==E:K.extend([A(B,[C.children_nodes[0],F]),A(B,[O,A(B,[C.children_nodes[1],F])])]);continue
				elif D(F)is A and U(F):
					if F.val==H:K.extend([A(B,[F.children_nodes[0],C]),A(B,[F.children_nodes[1],C])]);continue
					elif F.val==E:K.extend([A(B,[F.children_nodes[0],C]),A(B,[O,A(B,[F.children_nodes[1],C])])]);continue
			I=A(H,[I,G])
		else:J=A(E,[J,G])
	M=c(right)
	for G in M:
		if U(G):
			C=G.children_nodes[0];F=G.children_nodes[1]
			if G.val==B:
				if D(C)is A and U(C):
					if C.val==H:M.extend([A(B,[C.children_nodes[0],F]),A(B,[C.children_nodes[1],F])]);continue
					if C.val==E:M.extend([A(B,[C.children_nodes[0],F]),A(B,[O,A(B,[C.children_nodes[1],F])])]);continue
				elif D(F)is A and U(F):
					if F.val==H:M.extend([A(B,[F.children_nodes[0],C]),A(B,[F.children_nodes[1],C])]);continue
					elif F.val==E:M.extend([A(B,[F.children_nodes[0],C]),A(B,[O,A(B,[F.children_nodes[1],C])])]);continue
			I=A(E,[I,G])
		else:J=A(H,[J,G])
	I=h(I);return A(L,[J,I])
def w(node_o):
	C=node_o
	if D(C)is not F and D(C)is not A:I=C[0];C=C[1]
	else:I=[]
	if D(C)is A:
		if C.val==B:
			G=w(C.children_nodes[0]);H=w(C.children_nodes[1]);J=[]
			if D(G)is not F and D(G)is not A:I.extend(G[0]);J.append(G[1])
			else:J.append(G)
			if D(H)is not F and D(H)is not A:I.extend(H[0]);J.append(H[1])
			else:J.append(H)
			if D(G)is F:
				if G.lstrip(E).isdigit():I.append(G)
			if D(H)is F:
				if H.lstrip(E).isdigit():I.append(H)
			return I,A(B,*J)
		else:return C
	else:return C
def Z(node_o):
	J=node_o
	if D(J)is A:
		C=Z(J.children_nodes[0]);G=Z(J.children_nodes[1])
		if J.val==B:
			if C==Q or G==Q:return Q
			elif G==K:return C
			elif C==K:return G
			elif D(C)is F and D(G)is F:
				if C.lstrip(E).isdigit()and G.lstrip(E).isdigit():return F(N(C)*N(G))
			elif D(C)is A and D(G)is F:
				if G.lstrip(E).isdigit():
					if C.val==B:
						M=C.children_nodes[1]
						if D(M)is F:
							if M.lstrip(E).isdigit():G=F(N(M)*N(G));C=C.children_nodes[0]
					elif C.val==L:
						M=C.children_nodes[0]
						if D(M)is F:
							if M.lstrip(E).isdigit():return A(H,[A(L,[F(N(M)*N(G)),C.children_nodes[1]]),0])
			elif D(C)is F and D(G)is A:
				if C.lstrip(E).isdigit():
					if G.val==B or G.val==L:
						P=J;R=G;M=G.children_nodes[0];S=G.children_nodes[1]
						if D(M)is F:
							if M.lstrip(E).isdigit():
								if P.val==B and R.val==B:C=F(N(M)*N(C));G=S
		elif J.val==L:
			if G==K or C==Q:return C
		elif J.val==H or J.val==E:
			if G==Q:return C
			elif C==Q:
				if J.val==H:return G
				else:return A(B,[O,G])
			elif D(C)is F and D(G)is F:
				if C.lstrip(E).isdigit()and G.lstrip(E).isdigit():return F(N(C)+N(G)if J.val==H else N(C)-N(G))
		elif J.val==I:
			if G==K:return C
			elif G==Q:return K
		elif J.val==V:
			if C==G:return K
			if C==K:return Q
		J.children_nodes=[C,G]
	elif J=="x'":return K
	return J
def A1(left,right):
	B=right;A=left;A=Z(A)
	if B==q:return A
	else:B=Z(B);return"y' = "+F(Z(A0(A,B)))
A2=W()
A3=M(A2)
x=W(True)
A4=M(x)if x!=q else q
A5=F(A1(A3,A4)).replace(i,'pi')
print(A5)