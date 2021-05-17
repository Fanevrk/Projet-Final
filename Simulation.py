from Fonctions import *
from Variables import *

'''Liste des planètes à simuler'''
Planetes=[Astre('Terre',147*math.pow(10,9),29780,6.903*math.pow(10,18)),
		  Astre('20% Terre',147*math.pow(10,9),8492,1.968*math.pow(10,18)),
		  Astre('90% Terre',147*math.pow(10,9),40000,9.74*math.pow(10,18)),
		  Astre('Jupiter',740*math.pow(10,9),13058.5,2.03*math.pow(10,20)),
		  Astre('90% Jupiter',740*math.pow(10,9),17935.6,1.66*math.pow(10,19)),
  		  Astre('20% Jupiter',740*math.pow(10,9),4000,1.02*math.pow(10,19)),
		  Astre('100% VLib',147*math.pow(10,9),45000,0),
		  Astre('0% Terre', 147*math.pow(10,9),0)]

Fichier=open('Résultats.txt', 'w')

'''Boucle se répétant pour tous les astres'''
for Astre in [Astre for Astre in Planetes]:
	'''Répéter la section indentée pour tous les objets de la classe Astre dans la liste Planète'''
	Fichier.write('L\'astre {} commence aux coordonnées {},{} et possède une vitesse de {} \n'.format(Planetes[n].nom,Planetes[n].x,Planetes[n].y,Planetes[n].vy))
	dt=P[n]/NIt

	LX,LY,LAire,LT=Planetes[n].Liste()
	'''Boucle des mouvements par dt'''
	for i in range (NIt):

		ax,ay=Planetes[n].Accélération()

		vx,vy,t=Planetes[n].Vitesse(dt,ax,ay)

		x,y,ri,rf,dx,dy=Planetes[n].Position(vx,vy,dt)


		Planetes[n].Variables(x,y,vx,vy,ax,ay,t)

		Aire=Loi_2(ri,rf,dx,dy,n,Planetes)
	
		LX.append(x)
		LY.append(y)
		LAire.append(Aire)
		LT.append(t)

	X1,X2,X3,X4,Y1,Y2,Y3,Y4=Max_Min(LX,LY)

	Somme_1,Somme_2=Analyse_Loi_2(LAire)
	Fichier.write('Somme 1 = {}, Somme 2 ={}\n'.format(Somme_1,Somme_2))

	index=Loi_3(Position_Initiale,LX,n)
	Fichier.write('L\'astre aura effectué un tour après {} secondes.\n'.format(LT[index]))

	Fichier.write('Les coordonnées maximales et minimales de cet astre sont :')
	Fichier.write('Xmax={},{}\n'.format(X1,Y1))
	Fichier.write('Xmin={},{}\n'.format(X2,Y2))
	Fichier.write('Ymax={},{}\n'.format(X3,Y3))
	Fichier.write('Ymin={},{}\n'.format(X4,Y4))

	Graphique_individuel(n,Planetes,LX,LY,X1,X2,X3,X4,Y1,Y2,Y3,Y4,Planetes)
	Graphique_Collectif(LX,LY,n)
	Graphique_Individuellement_Collectifs(LX,LY,n)

	Fichier.write('\nNOUVELLE ITÉRATION \n')
	n+=1
print("Finished")
plt.show()
Fichier.close()