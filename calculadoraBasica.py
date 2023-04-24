from fundamentosPython import nuevoTema
# Sin alias:
# import calc.operaciones

# Con alias:
import calc.operaciones as c

if __name__ =="__main__":
    nuevoTema("Módulos y paquetes")
    # Sin alias
    # print(calc.operaciones.resta(5,2))
    print(c.suma(5,2))
    print(c.resta(5,2))
    print(c.mult(5,2))
    print(c.div(5,2))