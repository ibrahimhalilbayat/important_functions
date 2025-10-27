import math
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


def calculate_initial_compass_bearing(pointA, pointB):
    try:
        lat1 = math.radians(pointA[0])
        lat2 = math.radians(pointB[0])
        diffLong = math.radians(pointB[1] - pointA[1])
        x = math.sin(diffLong) * math.cos(lat2)
        y = math.cos(lat1)*math.sin(lat2) - (math.sin(lat1)*math.cos(lat2)*math.cos(diffLong))
        initial_bearing = math.atan2(x, y)
        return (math.degrees(initial_bearing) + 360) % 360
    except Exception as e:
        print(f'calculate_initial_compass_bearing fonksiyonunda bir hata oluştu. Girdiler: {pointA}, {pointB}. HATA: {e}')


Ankara = (39.9334, 32.8597)
Diyarbakır = (37.9250, 40.2110)

bearing_degrees = calculate_initial_compass_bearing(Ankara, Diyarbakır)

plt.figure(figsize=(10, 7))

m = Basemap(projection='merc',
            llcrnrlat=35, urcrnrlat=43,
            llcrnrlon=25, urcrnrlon=45,
            resolution='i')

m.drawcoastlines()
m.drawcountries()
m.fillcontinents(color='lightgray', lake_color='lightblue')
m.drawmapboundary(fill_color='lightblue')

lonA, latA = Ankara[1], Ankara[0]
lonB, latB = Diyarbakır[1], Diyarbakır[0]
xA, yA = m(lonA, latA)
xB, yB = m(lonB, latB)

m.plot(xA, yA, 'ro', markersize=5, label='Ankara')
m.plot(xB, yB, 'bo', markersize=5, label='Diyarbakır')
m.drawgreatcircle(lonA, latA, lonB, latB, color='green', linewidth=2)

plt.text(xA + 50000, yA + 50000, 'Ankara', fontsize=12)
plt.text(xB + 50000, yB + 50000, 'Diyarbakır', fontsize=12)

plt.legend(loc='lower left')
plt.title(f"Diyarbakır, Ankara'nın: {bearing_degrees:.2f}°sinde")
plt.tight_layout()
plt.show()
