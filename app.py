import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
scatter_button= st.button('Construir diagrama de dispersion') #crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    
if scatter_button:  # Al hacer clic en el botón de gráfico de dispersión
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    
    # Mostrar el gráfico de dispersión
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Casillas de verificación para seleccionar gráficos
build_histogram = st.checkbox('Construir un histograma')
build_scatter_plot = st.checkbox('Construir un diagrama de dispersión')

if build_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un histograma
    fig_histogram = px.histogram(car_data, x="odometer", title="Histograma de Odómetro")
    
    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_histogram, use_container_width=True)

if build_scatter_plot:
    st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un diagrama de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Diagrama de Dispersión de Odómetro vs Precio")
    
    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)