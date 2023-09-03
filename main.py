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

    

    

    
    if genero == "hombre" or genero == "mujer":

        kg=   int((input("itroduce tu peso : ")))

        altura= int((input("Introduce tu altura en cm : ")))

        edad= int((input("introduce tu edad :")))

        resultado= 66.47 +(13.75*kg)+(5.003*altura)-(6.755*edad)

        print("Tus calorias por dia serian: " ,resultado)
    
calcular_tmb()    