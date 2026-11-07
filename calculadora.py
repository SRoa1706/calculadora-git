# calculadora.py    
def presentacion():
    print("====================================")
    print("  CALCULADORA MODULAR EN PYTHON     ")
    print("====================================")

if __name__ == "__main__":
    presentacion()

def sumar(a, b):
   return a + b

def restar(a, b):
   return a - b

def multiplicar(a, b):
   return a * b

def dividir(a, b):
   if b == 0:
       return "Error: no es posible dividir entre cero"
   return a / b