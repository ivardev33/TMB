#CALCULADORA DE TASA METABOLICA BASAL

#PARA HOMBRES
"""
def calcular_tmb_hombre(peso_kg,altura_cm,edad_anos):

    tmb= 88.362 + (13.397*peso_kg)+(4.799* altura_cm)-(5.677 *edad_anos)
    return tmb

tmb_hombre= calcular_tmb_hombre(68,174,33)

print("Calorias para un hombre")

print (tmb_hombre, "Calorias por dia")

"""

def calcular_tmb ():

    genero=input(('Eres un hombre o una mujer :?'))

    

  #Para hombres  

    
    if genero == "hombre" :

        kg=   int((input("itroduce tu peso : ")))

        altura= int((input("Introduce tu altura en cm : ")))

        edad= int((input("introduce tu edad :")))

        resultado= (10*kg)+(6.25*altura)-(5*edad)+5

        print("Tus calorias por dia como H  serian: " ,resultado)
  #Para mujeres       

    if genero == "mujer":



        kg=   int((input("itroduce tu peso : ")))

        altura= int((input("Introduce tu altura en cm : ")))

        edad= int((input("introduce tu edad :")))

        resultado= (10*kg)+(6.25*altura)-(5*edad)-161

        print("Tus calorias por dia como M serian: " ,resultado)
        
    else:

       print( "Sigue las intrucciones")
        

    
calcular_tmb()    