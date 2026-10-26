z='x'
y='atan'
x='asin'
w='tan'
v='cos'
u='sin'
t='y'
s='='
r='acot'
q='acsc'
p='&'
k='asec'
j='cot'
i=False
f='sec'
e='csc'
a='e'
Z=''
W="'"
T='log'
S='('
Q='0'
M=')'
P='-1'
O='func'
N=int
L='/'
J='1'
I='^'
H='+'
F=str
E='-'
C=type
B='*'
class A:
	val=Z;children_nodes=[];abs_val=i
	def __init__(A,val,children,abs_val=i):A.val=val;A.children_nodes=children;A.abs_val=abs_val
	def __str__(G):
		Q=' ';N=G.children_nodes[0];P=G.children_nodes[1];D=F(N);K=F(P)
		if G.val==L:
			if C(N)is not F:D=S+D+M
			if C(P)is not F:K=S+K+M
		elif G.val==B:
			if C(N)is A:
				if N.val==H or N.val==E:D=S+D+M
			elif len(D.lstrip(E))==1:D=D.replace(J,Z)
			if C(P)is A:
				if P.val==H or P.val==E:K=S+K+M
				if C(N)is F:
					if X(N):return D+K
			elif C(P)is F:
				if C(N)is A:
					R=N.children_nodes[1]
					if C(R)is A:
						if R.val==I:return D+' * '+K
				if not P.lstrip(E).isdigit():return D+K
		elif G.val==I or G.val==E:
			if C(N)is A:D=S+D+M
			if C(P)is A:K=S+K+M
		elif G.val==O:return D+S+K+M
		elif G.val==T:
			if K==a:return'ln('+D+M
			else:return'log('+D+','+K+M
		if not G.abs_val:return D+(Q+G.val+Q if G.val!=I else G.val)+K
		else:return'| '+D+(Q+G.val+Q if G.val!=I else G.val)+K+' |'
def X(x):return x.lstrip(E).isdigit()or x==a or x==p
R=Z
Y=Z
def A0(equation_in):
	C=equation_in;global R;global Y;R=Z;C=S+C.replace('**',I).replace(')(',B).replace('1/sin',e).replace('1/cos',f).replace('1/tan',j).replace('1/asin',q).replace('1/acos',k).replace('1/atan',r).replace('pi',p)+M
	for A in C:
		if(A.lstrip(E).isdigit()and not Y.lstrip(E).isdigit()or Y.lstrip(E).isdigit()and not A.lstrip(E).isdigit()or A.isalpha()and not Y.isalpha())and X(Y)and A!=I and A!=H and A!=E and A!=B and A!=L and A!=M and A!=s and A!=',':R+=B
		R+=A;Y=A
	R=R.split(s)
	for D in range(len(R)):R[D]=S+R[D]+M
l=input("Enter an equation. (Don't use the regular x. Use the x/y found by pressing alpha + sto->/1 respectively)\n")
AF=t in l
A0(l)
b=0
D=0
A7=[u,v,w,e,f,j,x,'acos',y,q,k,r,T,'ln']
m=[]
c={}
def G():global D;return R[b][D:D+1]
def U(other_side=i):
	global D;global b
	if other_side:
		if s in l:D=0;b+=1
		else:return
	B=A1()
	while G()==H or G()==E:C=G();D+=1;F=A1();B=A(C,[B,F])
	return B
def A1():
	global D;C=A2()
	while G()==B or G()==L:E=G();D+=1;F=A2();C=A(E,[C,F])
	return C
def A2():
	global D;B=A3()
	if G()==I:C=G();D+=1;E=A3();B=A(C,[B,E])
	return B
def A3():
	global D;B=Z
	if X(G()):
		while X(G()):B+=G();D+=1
		return B
	if G()==z or G()==t:B+=G();D+=1;return B
	H=G()
	if H.isalpha():
		while G().isalpha():B+=G();D+=1
		D+=1
		if B not in m and B not in A7:m.append(B)
		if B==T:E=U();D+=1;I=U();return A(T,[E,I])
		elif B=='ln':E=U();return A(T,[E,a])
		else:return A(O,[B,U()])
	if G()==S or G()=='|':
		J=G()=='|';D+=1;F=U()
		if C(F)is A:F.abs_val=J
		D+=1;return F
def K(node_o):
	V='2';D=node_o
	if C(D)is A:
		if D.val==H or D.val==E:return A(D.val,[K(D.children_nodes[0]),K(D.children_nodes[1])])
		elif D.val==B:S=D.children_nodes[0];Z=K(S);U=D.children_nodes[1];b=K(U);return A(H,[A(B,[Z,U]),A(B,[S,b])])
		elif D.val==L:S=D.children_nodes[0];Z=K(S);U=A(I,[D.children_nodes[1],P]);b=K(U);return A(H,[A(B,[Z,U]),A(B,[S,b])])
		elif D.val==I:
			if C(D.children_nodes[1])is F:
				if X(D.children_nodes[1]):
					R=D.children_nodes[1]
					if C(R)is A:
						if R.val==L:Y=R.children_nodes;Y[0]=F(N(Y[0])-N(Y[1]));R=A(L,*Y)
					else:R=F(N(R)-1)
					return A(B,[A(B,[D.children_nodes[1],A(I,[D.children_nodes[0],R])]),K(D.children_nodes[0])])
				else:return A(B,[A(B,[A(T,[D.children_nodes[0],a]),A(I,[D.children_nodes[0],D.children_nodes[1]])]),K(D.children_nodes[1])])
			else:return A(B,[A(B,[A(T,[D.children_nodes[0],a]),A(I,[D.children_nodes[0],D.children_nodes[1]])]),K(D.children_nodes[1])])
		elif D.val==O:
			M=D.children_nodes[0];G=D.children_nodes[1]
			if M==u:D=A(O,[v,G])
			elif M==v:D=A(B,[P,A(O,[u,G])])
			elif M==w:D=A(I,[A(O,[f,G]),V])
			elif M==e:D=A(B,[P,A(B,[A(O,[e,G]),A(O,[j,G])])])
			elif M==f:D=A(B,[A(O,[f,G]),A(O,[w,G])])
			elif M==j:D=A(B,[P,A(I,[A(O,[e,G]),V])])
			elif M==x or M=='acos':return A(B,[J if M==x else P,A(L,[K(G),A(I,[A(E,[J,A(I,[G,2])]),A(L,[J,V])])])])
			elif M==k or M==q:return A(B,[J if M==k else P,A(L,[K(G),A(B,[A(H,[Q,G],True),A(I,[A(E,[A(I,[G,V]),J]),A(L,[J,V])])])])])
			elif M==y or M==r:return A(B,[J if M==y else P,A(L,[K(G),A(H,[J,A(I,[G,2])])])])
			else:D=A(O,[M+W,G])
			return A(B,[D,K(G)])
		elif D.val==T:return A(L,[K(D.children_nodes[0]),A(B,[A(T,[D.children_nodes[1],a]),D.children_nodes[0]])])
	elif D==z or D==t:return D+W
	elif X(D):return Q
def g(node_o,negative=i):
	F=negative;D=node_o
	if C(D)is A:
		if D.val==H or D.val==E:G=[];G.extend(g(D.children_nodes[0],F));G.extend(g(D.children_nodes[1],D.val==E and not F or D.val==H and F));return G
		elif not F:return[D]
		else:return[A(B,[P,D])]
	elif not F:return[D]
	else:return[A(B,[P,D])]
def V(node_o):
	B=node_o
	if C(B)is A:D=V(B.children_nodes[0]);E=V(B.children_nodes[1]);return D or E
	elif C(B)is F:return B=="y'"
def n(node_o):
	B=node_o
	if C(B)is A:D=n(B.children_nodes[0]);E=n(B.children_nodes[1]);B.children_nodes[0]=D;B.children_nodes[1]=E;return B
	elif C(B)is F:
		if B=="y'":return J
		else:return B
def o(node_o,val):
	D=val;B=node_o
	if C(B)is A:E=o(B.children_nodes[0],D);F=o(B.children_nodes[1],D);B.children_nodes[0]=E;B.children_nodes[1]=F;return B
	elif B==z:return D
	else:return B
def A4(func,node_o):
	D=func;B=node_o
	if W not in D:E=c[D][0]
	else:E=c[D.rstrip(W)][1]
	if C(B)is A:
		if B.val==O and B.children_nodes[0].rstrip(W)in c:B=A4(B.children_nodes[0],B.children_nodes[1])
	return o(E,B)
def A8(left,right):
	I=Q;J=Q;K=g(left)
	for G in K:
		if V(G)and C(G)is A:
			D=G.children_nodes[0];F=G.children_nodes[1]
			if G.val==B:
				if C(D)is A and V(D):
					if D.val==H:K.extend([A(B,[D.children_nodes[0],F]),A(B,[D.children_nodes[1],F])]);continue
					if D.val==E:K.extend([A(B,[D.children_nodes[0],F]),A(B,[P,A(B,[D.children_nodes[1],F])])]);continue
				elif C(F)is A and V(F):
					if F.val==H:K.extend([A(B,[F.children_nodes[0],D]),A(B,[F.children_nodes[1],D])]);continue
					elif F.val==E:K.extend([A(B,[F.children_nodes[0],D]),A(B,[P,A(B,[F.children_nodes[1],D])])]);continue
			I=A(H,[I,G])
		else:J=A(E,[J,G])
	M=g(right)
	for G in M:
		if V(G)and C(G)is A:
			D=G.children_nodes[0];F=G.children_nodes[1]
			if G.val==B:
				if C(D)is A and V(D):
					if D.val==H:M.extend([A(B,[D.children_nodes[0],F]),A(B,[D.children_nodes[1],F])]);continue
					if D.val==E:M.extend([A(B,[D.children_nodes[0],F]),A(B,[P,A(B,[D.children_nodes[1],F])])]);continue
				elif C(F)is A and V(F):
					if F.val==H:M.extend([A(B,[F.children_nodes[0],D]),A(B,[F.children_nodes[1],D])]);continue
					elif F.val==E:M.extend([A(B,[F.children_nodes[0],D]),A(B,[P,A(B,[F.children_nodes[1],D])])]);continue
			I=A(E,[I,G])
		else:J=A(H,[J,G])
	I=n(I);return A(L,[J,I])
def A5(node_o):
	D=node_o
	if C(D)is not F and C(D)is not A:I=D[0];D=D[1]
	else:I=[]
	if C(D)is A:
		if D.val==B:
			G=A5(D.children_nodes[0]);H=A5(D.children_nodes[1]);J=[]
			if C(G)is not F and C(G)is not A:I.extend(G[0]);J.append(G[1])
			else:J.append(G)
			if C(H)is not F and C(H)is not A:I.extend(H[0]);J.append(H[1])
			else:J.append(H)
			if C(G)is F:
				if G.lstrip(E).isdigit():I.append(G)
			if C(H)is F:
				if H.lstrip(E).isdigit():I.append(H)
			return I,A(B,*J)
		else:return D
	else:return D
def d(node_o):
	K=node_o
	if C(K)is A:
		D=d(K.children_nodes[0]);G=d(K.children_nodes[1])
		if K.val==B:
			if D==Q or G==Q:return Q
			elif G==J:return D
			elif D==J:return G
			elif C(D)is F and C(G)is F:
				if D.lstrip(E).isdigit()and G.lstrip(E).isdigit():return F(N(D)*N(G))
			elif C(D)is A and C(G)is F:
				if G.lstrip(E).isdigit():
					if D.val==B:
						M=D.children_nodes[1]
						if C(M)is F:
							if M.lstrip(E).isdigit():G=F(N(M)*N(G));D=D.children_nodes[0]
					elif D.val==L:
						M=D.children_nodes[0]
						if C(M)is F:
							if M.lstrip(E).isdigit():return A(H,[A(L,[F(N(M)*N(G)),D.children_nodes[1]]),0])
			elif C(D)is F and C(G)is A:
				if D.lstrip(E).isdigit():
					if G.val==B or G.val==L:
						O=K;R=G;M=G.children_nodes[0];S=G.children_nodes[1]
						if C(M)is F:
							if M.lstrip(E).isdigit():
								if O.val==B and R.val==B:D=F(N(M)*N(D));G=S
		elif K.val==L:
			if G==J or D==Q:return D
		elif K.val==H or K.val==E:
			if G==Q:return D
			elif D==Q:
				if K.val==H:return G
				else:return A(B,[P,G])
			elif C(D)is F and C(G)is F:
				if D.lstrip(E).isdigit()and G.lstrip(E).isdigit():return F(N(D)+N(G)if K.val==H else N(D)-N(G))
		elif K.val==I:
			if G==J:return D
			elif G==Q:return J
		elif K.val==T:
			if D==G:return J
			if D==J:return Q
		K.children_nodes=[D,G]
	elif K=="x'":return J
	return K
def A9(left,right):
	B=right;A=left;A=d(A)
	if B==None:return A
	else:B=d(B);AA();A=h(A);B=h(B);return"y' = "+F(d(A8(A,B)))
def h(node_o):
	B=node_o
	if C(B)is A:
		if B.val==O:
			D=B.children_nodes[0].rstrip(W)
			if D.rstrip(W)in c:return A4(D,B.children_nodes[1])
		E=h(B.children_nodes[0]);F=h(B.children_nodes[1]);B.children_nodes[0]=E;B.children_nodes[1]=F;return B
	else:return B
def AA():
	global R;global D;global b
	for A in m:D=0;b=0;A0(input('Input the function:\n'+A+'(x) = '));B=U();C=K(B);c[A]=[B,C]
AB=U()
AC=K(AB)
A6=U(True)
AD=K(A6)if A6!=None else None
AE=F(A9(AC,AD)).replace(p,'pi')
print(AE)