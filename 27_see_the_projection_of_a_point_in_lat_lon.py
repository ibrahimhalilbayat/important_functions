from numpy import array, dot
from pyproj import Transformer

def find_degree_of_projected_coordinate(radar_latlon, orta_latlon, mean_latlon):
    try:
        transformer = Transformer.from_crs("EPSG:4326", "EPSG:32635", always_xy=True)  
        radar_xy = array(transformer.transform(*radar_latlon))
        orta_xy = array(transformer.transform(*orta_latlon))
        mean_xy = array(transformer.transform(*mean_latlon))

        line_vec = radar_xy - orta_xy

        point_vec = mean_xy - orta_xy
        t = dot(point_vec, line_vec) / dot(line_vec, line_vec)
        proj_xy = orta_xy + t * line_vec

        transformer_back = Transformer.from_crs("EPSG:32635", "EPSG:4326", always_xy=True)
        proj_latlon = transformer_back.transform(*proj_xy)
        return proj_latlon
    
    except Exception as e:
        print(f'find_degree_of_projected_coordinate fonksiyonunda bir hata oluştu...')