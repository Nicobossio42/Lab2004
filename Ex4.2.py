def demo(valor1, valor2, valor3=None):
   return valor1, valor2, valor3
    apply(demo, (1, 2), {'valor3': 3})
#La función apply() devuelve el resultado de una función o objeto clase llamado con argumentos soportados.