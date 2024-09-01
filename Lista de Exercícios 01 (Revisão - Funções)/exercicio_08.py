"""
Faça uma função hipotenusa(cateto1, cateto2) que retorna o comprimento da hipotenusa de um triângulo
 retângulo dados os comprimentos dos dois lados como parâmetros.
"""

import math




def hipotenusa(cateto1, cateto2):
    return (cateto1 **2) + (cateto2**2)


print(math.sqrt(hipotenusa(5, 7)))