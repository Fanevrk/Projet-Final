import matplotlib.pyplot as plt 
import math
from Variables import *

class Astre:
	'''
	Classe contenant toutes les planètes ainsi que leurs variables initiales
	'''
	def __init__(self,nom,x,vy,Aire_A=0,y=0,vx=0,t=0):
		self.nom=nom
		self.x,self.y=x,y
		self.vx,self.vy=vx,vy
		self.r=x
		self.ax,self.ay=0,0
		self.t=t
		self.Aire_A=Aire_A
		self.XInitial=x

	def Accélération(self):
		'''
		Méthode de calcul de l'accélération
		'''
		if self.x<=10 and self.x>=-10 and self.y>=-10 and self.y<=10:
			ax=0
			ay=0
		else:
			ax=-G*MS*(self.x/(self.x**2+self.y**2)**(3/2))
			ay=-G*MS*(self.y/(self.x**2+self.y**2)**(3/2))
		return ax,ay

	def Vitesse(self,dt,ax,ay):
		"""
		Méthode de calcul de la vitesse
		"""
		global t
		if self.x<=10 and self.x>=-10 and self.y>=-10 and self.y<=10:
			vx=0
			vy=0
		else:
			t=self.t+dt
			
			vx=ax*dt+self.vx
			vy=ay*dt+self.vy
		return vx,vy,t

	def Position(self,vx,vy,dt):
		"""
		Méthode de calcul de la position
		"""
		ri=(self.x**2+self.y**2)**(1/2)
		x=vx*dt+self.x
		y=vy*dt+self.y
		rf=(x**2+y**2)**(1/2)
		dx,dy=x-self.x,y-self.y
		return x,y,ri,rf,dx,dy

	def Variables(self,x,y,vx,vy,ax,ay,t):
		"""
		Méthode pour définir les variables initiales de la prochaine itération
		"""
		self.x=x
		self.y=y
		self.vx=vx
		self.vy=vy
		self.ax=ax
		self.ay=ay
		self.t=t

	def Liste(self):
		LX=[self.x]
		LY=[self.y]
		LAire=[]
		LT=[0]
		return LX,LY,LAire,LT


def Loi_2(ri,rf,dx,dy,n,Planetes):
	'''
	Fonction pour le calcul de la 2nde Loi de Kepler
	'''
	Dist=math.sqrt((dx)**2+(dy)**2)
	DemiP=(ri+rf+Dist)/2
	Argument=DemiP*(DemiP-ri)*(DemiP-rf)*(DemiP-Dist)
	Aire=0
	'''Vérification si l'aire est calculable (intérieur de la racine positive)'''
	if abs(Argument)>0:
		if Aire-Planetes[n].Aire_A<Planetes[n].Aire_A*0.05:
			Aire=math.sqrt(Argument)
			Aire=Aire
		else:
			Aire=0
	else:
		Aire=False
	return Aire

def Analyse_Loi_2(LAire):
	L1=LAire[0:100000]
	L2=LAire[500000:600000]

	Somme_1=sum(L1)
	Somme_2=sum(L2)
	return Somme_1,Somme_2

def Max_Min(LX,LY):
	'''
	Fonction pour définir les extrémités de l'ellipse
	'''
	Coord=list(zip(LX,LY))

	Xmax=max(Coord)
	X1,Y1=zip(Xmax)
	Xmin=min(Coord)
	X2,Y2=zip(Xmin)
	Ymax=max(Coord, key=lambda item:item[1])
	X3,Y3=zip(Ymax)
	Ymin=min(Coord, key=lambda item:item[1])
	X4,Y4=zip(Ymin)

	return X1,X2,X3,X4,Y1,Y2,Y3,Y4

def Loi_3(Position_Initiale,LX,n):
	'''
	Fonction permettant de déterminer la période
	'''
	LX=LX[100:]
	''' Exclure les premières itérations car elles rentrent dans la condition'''
	PIndex=[i for i, x in enumerate(LX) if x<Position_Initiale[n]+(Position_Initiale[n]*0.1) and x>=Position_Initiale[n]]
	if not PIndex:
		print("Impossible")
		index=0
	else:
		index=int(PIndex[0])
	return index

def Graphique_individuel(n,nom,LX,LY,X1,X2,X3,X4,Y1,Y2,Y3,Y4,Planetes):
	'''Fonction créant le graphique de chaque astre'''
	plt.figure(n)
	plt.grid()
	plt.gca().set_aspect('equal', adjustable='box')
	plt.xlabel('Position en X')
	plt.ylabel('Position en Y')
	plt.title(Planetes[n].nom)
	plt.plot(LX,LY)
	plt.scatter(X1,Y1)
	plt.scatter(X2,Y2)
	plt.scatter(X3,Y3)
	plt.scatter(X4,Y4)

def Graphique_Collectif(LX,LY,n):
	'''Fonction créant un graphique regroupant tous les astres'''
	if n<6:
		plt.figure('Ensemble')
		plt.title('Ensemble')
		plt.plot(LX,LY)
	else:
		pass
def Graphique_Individuellement_Collectifs(LX,LY,n):
	if n<3:
		plt.figure('Terres')
		plt.title('Terres')
		plt.plot(LX,LY)
	elif n<6:
		plt.figure('Jupiters')
		plt.title('Jupiters')
		plt.plot(LX,LY)
	else:
		pass
	