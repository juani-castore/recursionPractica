# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 22:12:48 2022

@author: juani
"""

from typing import List


#------------------------ ejercicio 1 ----------------------
def pot2(n: int) -> int:
    """
    requiere: un entero n >= 0
    devuelve: 2**n
    """
    if n == 0:
        return 1
    return pot2(n-1) * 2

#print(pot2(2830))

def pot_a(a: int, n: int) -> int:
    """
    Parameters
    ----------
    a : int
    n : int >= 0
    Returns
    -------
    int = a**n
    """
    if n == 0:
        return 1
    return pot_a(a, n - 1) * a

# print(pot_a(0,0))

def producto(n: int,m: int)-> int:
    if m == 0:
        return 0
    return producto(n, m - 1) + n

# print(producto(0, 0))

def es_par(n: int) -> bool:
    if n == 0:
        return True
    elif n == -1:
        return False
    return es_par(n - 2)

# print(es_par(0))

#------------------------ ejercicio 2 ----------------------

def productoria(xs: List[int]) -> int:
    if len(xs) == 1:
        return xs[0]
    return productoria(xs[1:]) + xs[0]

# xs_prueba: List[int] = [1,2,3,4,5,6,7,8,9]
# print(productoria(xs_prueba))

i = 0
def cantidad_ocurrencias(x: int, xs: List[int]) -> int:
    if len(xs) == 0:
        return 0
    elif xs[0] == x:
        return cantidad_ocurrencias(x, xs[1:]) + 1
    else: 
        return cantidad_ocurrencias(x, xs[1:]) 
    
#xs_prueba: List[int] = [1,2,3,4,1,6,7,1,9]
#print(cantidad_ocurrencias(1, xs_prueba))
    
def max_pos(xs: List[int]) -> int:
    
    if len(xs) == 1:
        return 0
    else:
        pos_max = max_pos(xs[1:]) + 1
        valor_max = xs[pos_max]
        
        if xs[0] >= valor_max:
            return 0
        else:
            return pos_max
    
# xs_prueba: List[int] = [1,2,8,9,4,8,6,9,1,7]
# print(max_pos(xs_prueba))

def contar_coincidencias(xs: List[int]) -> int:
    if len(xs) == 0:
        return 0
    else:
        nro_actual = xs.pop()
        if nro_actual == len(xs):
            return contar_coincidencias(xs) + 1
        else:
            return contar_coincidencias(xs)
    
    
        
#xs_prueba: List[int] = [1,1,2,2,4,4]
#print(contar_coincidencias(xs_prueba))


def sumar_posiciones_pares(xs: List[int]) -> int:
    if len(xs) <= 0:
        return 0
    else:
        return sumar_posiciones_pares(xs[2:]) + xs[0] 

#xs_prueba: List[int] = [1,124,1,315,1,124]
#print(sumar_posiciones_pares(xs_prueba))


#------------------------ ejercicio 3 ----------------------

def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
    
#print(fibonacci(6))
    


































