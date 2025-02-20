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
    img_col, info_col = st.columns([3, 1])
    with img_col:
        #Mostrar la imagen del pokemon
        st.image(pokemon_data["sprites"]["other"]["official-artwork"]["front_default"], 
                 caption=f"#{pokemon_data['id']} {pokemon_data['name'].title()}",
                 use_container_width=True) 
    with info_col:
        #Informacion basica
        st.subheader("Información Básica")
        st.write(f"**Altura:** {pokemon_data['height']/10} m")
        st.write(f"**Peso:** {pokemon_data['weight']/10} kg")
        
        #Tipos
        st.subheader("Tipos")
        tipos = [tipo["type"]["name"] for tipo in pokemon_data["types"]]
        for tipo in tipos:
            st.write(f"- {tipo.title()}")             
        
    #Estadisticas
    st.subheader("Estadísticas")
    stats_col = st.columns(3)
    stats = pokemon_data["stats"]
    for idx, stat in enumerate(stats):
        col_idx = idx % 3
        with stats_col[col_idx]:
            st.metric(
                label=stat["stat"]["name"].replace("-", " ").title(),
                value=stat["base_stat"],
            )
    
    #Habilidades
    st.subheader("Habilidades")
    abilities = [ability["ability"]["name"].replace("-", "").title()
                 for ability in pokemon_data["abilities"]]
    for ability in abilities:
        st.write(f"⭐ {ability.title()}")      
elif pokemon_name:
    st.error("Pokemon no encontrado,  Verifique e intente nuevamente.")
else:
    st.info("Ingresa un nombre de pokemon o presiona el botón para obtener un pokemon aleatorio.")            