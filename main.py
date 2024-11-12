class Asiento:
    def __init__(self,color,precio,registro):
        self.color=color
        self.precio=precio
        self.registro=registro
    
    def cambiarColor(self,Color):
        colores= ["rojo","verde","amarillo","negro","blanco"]
        if Color in colores:
            self.color=Color
        else:
            pass

class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro
        
    def cambiarRegistro(self,nRegistro):
        self.registro=nRegistro
    
    def asignarTipo(self,nTipo):
        if nTipo == "gasolina":
            self.tipo = nTipo
        elif nTipo == "electrico":
            self.tipo = nTipo
        else:
            pass
        
class Auto:
    cantidadCreados = "0"
    def __init__(self,modelo,precio,asiento,marca,motor,registro):
        self.modelo= modelo
        self.precio= precio
        self.asientos= asiento
        self.marca= marca
        self.motor= motor
        self.registro= registro

    def cantidadAsientos(self):
        cantidad = 0
        for asiento in self.asientos:
            if asiento != None:
                cantidad+=1
                
        return cantidad
    
    def verificarIntegridad(self):
        
        for asiento in self.asientos:
            if asiento !=None:
                if asiento.registro != self.registro:
                    return ("Las piezas no son originales")
            
        if self.motor.registro != self.registro:
            return ("Las piezas no son originales")
        return ("Auto original")
            
            

