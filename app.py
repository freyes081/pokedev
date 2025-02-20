import random

import requests
import streamlit as st

st.set_page_config(
    page_title="Pokemon Explorer",
    page_icon="🔍",
    layout="centered",
    
)


#Funcion para obtener datos de un pokemon
def get_pokemon_data(pokemon_name):
    try:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    except:
        return None 
    
#Funcion para obtener un pokemon aleatorio
def get_random_pokemon():
    random_pokemon_id = random.randint(1,1010)
    return get_pokemon_data(str(random_pokemon_id))

#Titulo y descripcion
st.title("🔥 Pokemon Explorer")
st.markdown("Descubre información sobre tus pokemones favoritos o descubre un pokemon aleatorio")

#Crear dos columnas para la busqueda y el boton aleatorio
col1, col2 = st.columns([2, 1])

#Columna de busqueda

with col1:
    pokemon_name = st.text_input("Ingresa el nombre de un pokemon:", "")
    
#Columna de boton aleatorio

with col2:
    random_button = st.button("¡Quiero un pokemon aleatorio! 🎲") 
    

pokemon_data = None

# Manejar la busqueda o el boton aleatario 
if pokemon_name:
    pokemon_data = get_pokemon_data(pokemon_name)
elif random_button:
    pokemon_data = get_random_pokemon()

#Mostrar la informacion del pokemon
if pokemon_data:
    #Crear dos columnas para la imagen y la informacion
    img_col, info_col = st.columns([1, 1])
    with img_col:
        #Mostrar la imagen del pokemon
        st.image(pokemon_data["sprites"]["other"]["official-artwork"]["front_default"], 
                 caption=f"#{pokemon_data['id']} {pokemon_data['name'].title()}",
                 use_column_width=True) 
                 
        
          