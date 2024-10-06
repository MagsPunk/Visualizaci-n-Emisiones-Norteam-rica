
import pandas as pd
import plotly.express as px

# Datos de emisiones expandidos para incluir México y Canadá
data = {
    'Estado/Provincia': [
        # Estados Unidos
        'Alabama (USA)', 'Alaska (USA)', 'Arizona (USA)', 'Arkansas (USA)', 'California (USA)', 
        'Colorado (USA)', 'Connecticut (USA)', 'Delaware (USA)', 'Florida (USA)', 'Georgia (USA)', 
        'Hawái (USA)', 'Idaho (USA)', 'Illinois (USA)', 'Indiana (USA)', 'Iowa (USA)', 
        'Kansas (USA)', 'Kentucky (USA)', 'Luisiana (USA)', 'Maine (USA)', 'Maryland (USA)', 
        'Massachusetts (USA)', 'Míchigan (USA)', 'Minnesota (USA)', 'Misisipi (USA)', 'Misuri (USA)', 
        'Montana (USA)', 'Nebraska (USA)', 'Nevada (USA)', 'Nuevo Hampshire (USA)', 'Nuevo México (USA)', 
        'Nueva York (USA)', 'Carolina del Norte (USA)', 'Dakota del Norte (USA)', 'Ohio (USA)', 
        'Oklahoma (USA)', 'Oregón (USA)', 'Pensilvania (USA)', 'Rhode Island (USA)', 
        'Carolina del Sur (USA)', 'Dakota del Sur (USA)', 'Tennessee (USA)', 'Texas (USA)', 
        'Utah (USA)', 'Vermont (USA)', 'Virginia (USA)', 'Washington (USA)', 
        'Virginia Occidental (USA)', 'Wisconsin (USA)', 'Wyoming (USA)',
        # México
        'Aguascalientes (MX)', 'Baja California (MX)', 'Baja California Sur (MX)', 'Campeche (MX)',
        'Chiapas (MX)', 'Chihuahua (MX)', 'Coahuila (MX)', 'Colima (MX)', 'Ciudad de México (MX)',
        'Durango (MX)', 'Guanajuato (MX)', 'Guerrero (MX)', 'Hidalgo (MX)', 'Jalisco (MX)',
        'Estado de México (MX)', 'Michoacán (MX)', 'Morelos (MX)', 'Nayarit (MX)', 'Nuevo León (MX)',
        'Oaxaca (MX)', 'Puebla (MX)', 'Querétaro (MX)', 'Quintana Roo (MX)', 'San Luis Potosí (MX)',
        'Sinaloa (MX)', 'Sonora (MX)', 'Tabasco (MX)', 'Tamaulipas (MX)', 'Tlaxcala (MX)',
        'Veracruz (MX)', 'Yucatán (MX)', 'Zacatecas (MX)',
        # Canadá
        'Alberta (CA)', 'Columbia Británica (CA)', 'Manitoba (CA)', 'Nuevo Brunswick (CA)',
        'Terranova y Labrador (CA)', 'Nueva Escocia (CA)', 'Ontario (CA)', 'Isla del Príncipe Eduardo (CA)',
        'Quebec (CA)', 'Saskatchewan (CA)', 'Territorios del Noroeste (CA)', 'Nunavut (CA)', 'Yukón (CA)'
    ]
}

# Generar datos de emisiones simulados para todos los estados/provincias
import numpy as np
np.random.seed(42)  # Para reproducibilidad

# Generar datos de CO2 y CH4
n_locations = len(data['Estado/Provincia'])
data['CO2 (ton)'] = np.random.randint(500000, 3000000, n_locations)
data['CH4 (ton)'] = np.random.randint(100000, 600000, n_locations)

# Coordenadas completas
coordinates = {
    # Estados Unidos (mantenemos los existentes)
    'Alabama (USA)': [32.806671, -86.791130],
    'Alaska (USA)': [61.370716, -152.404419],
    'Arizona (USA)': [33.729759, -111.431221],
    'Arkansas (USA)': [34.969704, -92.373123],
    'California (USA)': [36.116203, -119.681564],
    'Colorado (USA)': [39.059811, -105.311104],
    'Connecticut (USA)': [41.597782, -72.755371],
    'Delaware (USA)': [39.318523, -75.507141],
    'Florida (USA)': [27.766279, -81.686783],
    'Georgia (USA)': [33.040619, -83.643074],
    'Hawái (USA)': [21.094318, -157.498337],
    'Idaho (USA)': [44.240459, -114.478828],
    'Illinois (USA)': [40.349457, -88.986137],
    'Indiana (USA)': [39.849426, -86.258278],
    'Iowa (USA)': [42.011539, -93.210526],
    'Kansas (USA)': [38.526600, -96.726486],
    'Kentucky (USA)': [37.668140, -84.670067],
    'Luisiana (USA)': [31.169546, -91.867805],
    'Maine (USA)': [44.693947, -69.381927],
    'Maryland (USA)': [39.063946, -76.802101],
    'Massachusetts (USA)': [42.230171, -71.530106],
    'Míchigan (USA)': [43.326618, -84.536095],
    'Minnesota (USA)': [45.694454, -93.900192],
    'Misisipi (USA)': [32.741646, -89.678696],
    'Misuri (USA)': [38.456085, -92.288368],
    'Montana (USA)': [46.921925, -110.454353],
    'Nebraska (USA)': [41.125370, -98.268082],
    'Nevada (USA)': [38.313515, -117.055374],
    'Nuevo Hampshire (USA)': [43.452492, -71.563896],
    'Nuevo México (USA)': [34.840515, -106.248482],
    'Nueva York (USA)': [42.165726, -74.948051],
    'Carolina del Norte (USA)': [35.630066, -79.806419],
    'Dakota del Norte (USA)': [47.528912, -99.784012],
    'Ohio (USA)': [40.388783, -82.764915],
    'Oklahoma (USA)': [35.565342, -96.928917],
    'Oregón (USA)': [44.572021, -122.070938],
    'Pensilvania (USA)': [40.590752, -77.209755],
    'Rhode Island (USA)': [41.680893, -71.511780],
    'Carolina del Sur (USA)': [33.856892, -80.945007],
    'Dakota del Sur (USA)': [44.299782, -99.438828],
    'Tennessee (USA)': [35.747845, -86.692345],
    'Texas (USA)': [31.054487, -97.563461],
    'Utah (USA)': [40.150032, -111.862434],
    'Vermont (USA)': [44.045876, -72.710686],
    'Virginia (USA)': [37.769337, -78.169968],
    'Washington (USA)': [47.400902, -121.490494],
    'Virginia Occidental (USA)': [38.491226, -80.954453],
    'Wisconsin (USA)': [44.268543, -89.616508],
    'Wyoming (USA)': [42.755966, -107.302490],
    # México
    'Aguascalientes (MX)': [21.8818, -102.2916],
    'Baja California (MX)': [30.8406, -115.2838],
    'Baja California Sur (MX)': [25.5818, -111.7100],
    'Campeche (MX)': [18.9333, -90.5333],
    'Chiapas (MX)': [16.7569, -93.1292],
    'Chihuahua (MX)': [28.6353, -106.0889],
    'Coahuila (MX)': [27.0587, -101.7068],
    'Colima (MX)': [19.1223, -104.0072],
    'Ciudad de México (MX)': [19.4326, -99.1332],
    'Durango (MX)': [24.0277, -104.6532],
    'Guanajuato (MX)': [21.0190, -101.2574],
    'Guerrero (MX)': [17.4392, -99.5451],
    'Hidalgo (MX)': [20.1168, -98.7376],
    'Jalisco (MX)': [20.6595, -103.3494],
    'Estado de México (MX)': [19.4969, -99.7233],
    'Michoacán (MX)': [19.5665, -101.7068],
    'Morelos (MX)': [18.6813, -99.1013],
    'Nayarit (MX)': [21.7514, -104.8455],
    'Nuevo León (MX)': [25.5922, -99.9962],
    'Oaxaca (MX)': [17.0732, -96.7266],
    'Puebla (MX)': [19.0414, -98.2063],
    'Querétaro (MX)': [20.5888, -100.3899],
    'Quintana Roo (MX)': [19.1817, -88.4791],
    'San Luis Potosí (MX)': [22.1565, -100.9855],
    'Sinaloa (MX)': [25.1721, -107.4795],
    'Sonora (MX)': [29.2972, -110.3309],
    'Tabasco (MX)': [17.8409, -92.6189],
    'Tamaulipas (MX)': [24.2669, -98.8363],
    'Tlaxcala (MX)': [19.3139, -98.2404],
    'Veracruz (MX)': [19.1738, -96.1342],
    'Yucatán (MX)': [20.7099, -89.0943],
    'Zacatecas (MX)': [22.7709, -102.5832],
    # Canadá
    'Alberta (CA)': [53.9333, -116.5765],
    'Columbia Británica (CA)': [53.7267, -127.6476],
    'Manitoba (CA)': [53.7609, -98.8139],
    'Nuevo Brunswick (CA)': [46.5653, -66.4619],
    'Terranova y Labrador (CA)': [53.1355, -57.6604],
    'Nueva Escocia (CA)': [45.1969, -63.1553],
    'Ontario (CA)': [51.2538, -85.3232],
    'Isla del Príncipe Eduardo (CA)': [46.5107, -63.4168],
    'Quebec (CA)': [52.9399, -73.5491],
    'Saskatchewan (CA)': [52.9399, -106.4509],
    'Territorios del Noroeste (CA)': [64.8255, -124.8457],
    'Nunavut (CA)': [70.2998, -83.1076],
    'Yukón (CA)': [64.2823, -135.0000]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Añadir coordenadas al DataFrame
df['lat'] = df['Estado/Provincia'].map(lambda x: coordinates[x][0])
df['lon'] = df['Estado/Provincia'].map(lambda x: coordinates[x][1])

# Crear la visualización del globo
fig = px.scatter_geo(df, 
                     lat='lat',
                     lon='lon',
                     size='CO2 (ton)',
                     color='CH4 (ton)',
                     hover_name='Estado/Provincia',
                     hover_data=['CO2 (ton)', 'CH4 (ton)'],
                     projection='orthographic',
                     color_continuous_scale='Viridis',
                     title='Emisiones de CO2 y CH4 en Norteamérica')

# Actualizar el diseño
fig.update_layout(
    geo=dict(
        showland=True,
        showocean=True,
        showcountries=True,
        countrywidth=0.5,
        landcolor='rgb(243, 243, 243)',
        oceancolor='rgb(204, 229, 255)',
        projection_rotation=dict(lon=-100, lat=40, roll=0),
        bgcolor='rgba(0,0,0,0)'
    ),
    height=800,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

# Actualizar los marcadores
fig.update_traces(
    marker=dict(
        line=dict(width=1, color='DarkSlateGrey'),
        sizeref=2000,
        sizemin=4
    )
)

# Mostrar el gráfico
fig.show()

# Guardar como HTML interactivo
fig.write_html("globo_emisiones_norteamerica_3d.html")