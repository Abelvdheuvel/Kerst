import streamlit as st 
import folium
import streamlit_folium

from haversine import haversine
from point_dict import points

CENTER = (52.0968641, 5.1209436)  # Noorderstraat 24, Netherlands

def distance_info():
    total_km = 0
    for point in points:
        distance = haversine(CENTER, point['coordinates'])
        total_km += distance
    
    avg_distance = total_km / len(points)

    return round(total_km), round(avg_distance)

def main():
    st.title('🌲 Kerst 2023 🌲')

    total_distance, avg_distance = distance_info()

    col1, col2 = st.columns(2)

    with col1:
        st.metric('Totale Afstand', str(total_distance) + 'km')

    with col2:
        st.metric('Gemiddelde Afstand', str(avg_distance) + 'km')
        

    m = folium.Map(location=[CENTER[0], CENTER[1]], zoom_start=8, tiles='https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', attr='CartoDB.Voyager')

    for point in points:
        folium.Marker(location=[point['coordinates'][0], point['coordinates'][1]], 
                    popup=point['name'], tooltip=point['name'], icon=folium.Icon(color='darkred', icon='map-pin')).add_to(m)
        
    st_data = streamlit_folium.st_folium(m, width=725)

    total_km = 0
    for point in points:
        distance = haversine(CENTER, point['coordinates'])
        total_km += distance
        name = point['name']
        st.write(f'{name}, {distance:.2f} km')



if __name__ == '__main__':
    main()
    
