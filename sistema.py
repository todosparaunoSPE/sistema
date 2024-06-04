# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 14:50:36 2024

@author: jperezr
"""

import streamlit as st

import numpy as np
import matplotlib.pyplot as plt

def main():
    st.title("Crea tu propio sistema de 2 ecuaciones con 2 incognitas")
    st.write("Esta aplicación solicita dos números. Que serán la solución que tu decidas para tu sistema (en el eje de las x toma de -10 a 10. En el eje de las (y) no importa que valor tomes)")
    st.write("Luego solicita 4 números más, que serán los coeficientes de las incognitas x e y")



    # Solicitar dos números al usuario
    num1 = st.number_input("Ingrese el primer número:", value=0.0)
    num2 = st.number_input("Ingrese el segundo número:", value=0.0)

    # Imprimir los números de diferentes maneras con más espacio
    st.write(f"Números ingresados:")
    st.markdown(f"({num1}) &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; ({num2})", unsafe_allow_html=True)

    # Solicitar cuatro números adicionales al usuario
    num3 = st.number_input("Ingrese el tercer número:", value=0.0)
    a = num3
    num4 = st.number_input("Ingrese el cuarto número:", value=0.0)
    a1 = num4
    num5 = st.number_input("Ingrese el quinto número:", value=0.0)
    a2 = num5
    num6 = st.number_input("Ingrese el sexto número:", value=0.0)
    a3 = num6
    
    

    # Imprimir los números adicionales
    st.write("Números adicionales ingresados:")
    ope1 = num3*num1+(num4 *num2)
    ope2 = num5*num1+(num6 *num2)
    st.write(f"({num3}) &emsp; * &emsp; ({num1}) &emsp; + &emsp; ({num4}) &emsp; * &emsp; ({num2}) &emsp; = &emsp; ({ope1})")
    st.write(f"({num5}) &emsp; * &emsp; ({num1}) &emsp; + &emsp; ({num6}) &emsp; * &emsp; ({num2}) &emsp; = &emsp; ({ope2})")
    
    st.write("")
    st.write("")
    
    st.write("el sistema de ecuaciones queda:")
    st.write("")
    
    st.write(f"({num3}) &emsp; * &emsp; (x) &emsp; + &emsp; ({num4}) &emsp; * &emsp; (y) &emsp; = &emsp; ({ope1})")
    st.write(f"({num5}) &emsp; * &emsp; (x) &emsp; + &emsp; ({num6}) &emsp; * &emsp; (y) &emsp; = &emsp; ({ope2})")
    
    st.write("")
    st.write("")
    
    st.write("La solución del sistema es:")
    
    st.write("")
    st.write("x=", num1)
    st.write("")
    st.write("y=", num2)
    st.write("")
    
    
    
    
    # Graficar las ecuaciones y el punto de intersección
    fig, ax = plt.subplots()
    
    x = np.linspace(-10, 10, 400)
    y1 = (ope1 - num3 * x) / num4
    y2 = (ope2 - num5 * x) / num6
    
    ax.plot(x, y1, label=f'{num3}x + {num4}y = {ope1}')
    ax.plot(x, y2, label=f'{num5}x + {num6}y = {ope2}')
    
    # Graficar el punto de intersección
    ax.plot(num1, num2, 'ro')  # Punto rojo
    ax.text(num1, num2, f' ({num1}, {num2})', fontsize=12, verticalalignment='bottom')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.axhline(0, color='black',linewidth=0.5)
    ax.axvline(0, color='black',linewidth=0.5)
    ax.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    ax.legend()
    
    st.pyplot(fig)
    
    st.write("")
    
    st.write("Espero hayas captado la idea, de la misma forma puedes crear tu sistema para 3,4, ecuaciones con el mismo número de incógnitas")

if __name__ == "__main__":
    main()

