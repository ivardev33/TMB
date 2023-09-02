#CALCULADORA DE TASA METABOLICA BASAL

#PARA HOMBRES

def calcular_tmb_hombre(peso_kg,altura_cm,edad_anos):

    tmb= 88.362 + (13.397*peso_kg)+(4.799* altura_cm)-(5.677 *edad_anos)
    return tmb

tmb_hombre= calcular_tmb_hombre(68,174,33)

print("Calorias para un hombre")

print (tmb_hombre, "Calorias por dia")



