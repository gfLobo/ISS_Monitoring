import pandas as pd
import folium
from folium.features import DivIcon
from geopy.geocoders import Nominatim
from tzwhere import tzwhere
from datetime import datetime
import pytz
import base64
from io import BytesIO
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import time



zoom_rate = 5
main_theme = 'stamenterrain'
while True:



    # Requests
    data = pd.read_json('http://api.open-notify.org/iss-now.json')
    info = pd.read_json('http://api.open-notify.org/astros.json')

    loc = [
        data['iss_position']['latitude'],
        data['iss_position']['longitude']
    ]




    # Current Address
    """Current Address doesn't work on ocean,
        so I use coordinates for that case"""
    try:
        geoLoc = Nominatim(user_agent="GetLoc")
        locname = geoLoc.reverse(f"{loc[0]}, {loc[1]}")
        tzwherer = tzwhere.tzwhere()
        tzwherer.tzNameAt(loc[0], loc[1])
        u = datetime.utcnow()
        u.replace(tzinfo=pytz.utc)

        address = locname.address

    except:
        address = f'Lat: {loc[0]}, Lon: {loc[1]}'

    # The Map
    m = folium.Map(
        location=loc,
        zoom_start=zoom_rate, tiles=f'{main_theme}')

    # Viewing modes

    folium.TileLayer('stamenterrain', name='Earth Relief').add_to(m)
    folium.TileLayer('openstreetmap', name='Street Map').add_to(m)
    folium.TileLayer('stamenwatercolor', name='Vintage').add_to(m)
    folium.TileLayer('cartodbpositron', name='White Earth').add_to(m)
    folium.TileLayer('cartodbdark_matter', name='Dark Earth').add_to(m)
    folium.LayerControl().add_to(m)

    # ISS on the map
    folium.CircleMarker(location=(loc[0] - 0.5, loc[1] + 0.8),
                        radius=40,
                        color='purple',
                        fill=True,
                        fill_color='#3186cc',
                        fill_opacity=1,
                        parse_html=False).add_to(m)

    folium.map.Marker(
        location=loc,
        icon=DivIcon(

            html=f'<img src="images/iss.png" width="50"></img>',
        )
    ).add_to(m)

    # Header
    folium.map.Marker(
        location=loc,
        icon=DivIcon(
            icon_size=(500, 90),
            icon_anchor=(225, 300),
            html=f'''<h1 ><mark style="background-color:black; color:white;">International Space Station</mark></h1>
            <br/>
            <h4  ><mark style="background-color:black; color:white;">📍 {address}</mark></h4>''',
        )
    ).add_to(m)

    folium.map.Marker(
        location=loc,
        icon=DivIcon(
            icon_anchor=(300, 295),
            html=f'<img src="images/iss_badge.png" width="80"></img>',
        )
    ).add_to(m)

    # Astronauts Info
    folium.map.Marker(
        location=loc,
        icon=DivIcon(
            icon_size=(500, 500),
            icon_anchor=(400, -200),
            html=f'<h2 >👩‍🚀 <mark style="background-color:black; color:white;">{len(info["people"])} Astronauts on board:</mark></h2><br/><br/> <h6 ><mark style="background-color:black; color:white;">{[i["name"] for i in info["people"]]}</mark></h6>',
        )
    ).add_to(m)

    # Globe Figure
    flatMap = plt.figure()
    globe = Basemap(projection='mill')


    globe.drawparallels(np.arange(-90, 90, 30), labels=[1, 0, 0, 0])
    globe.drawmeridians(np.arange(globe.lonmin, globe.lonmax + 30, 60), labels=[0, 0, 0, 1])
    # fill continents 'coral' (with zorder=0), color wet areas 'aqua'
    globe.drawmapboundary(fill_color='#003399')
    globe.fillcontinents(color='#00cc00', lake_color='#003399')
    ''' shade the night areas, with alpha transparency so the
        map shows through. Use current time in UTC.'''

    date = datetime.utcnow()
    globe.nightshade(date)

    plt.title('Globe terminator line %s (UTC)' % date.strftime("%d %b %Y"), fontdict={'fontsize': 13})
    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)

    '''ISS location on the globe'''
    globe.scatter(loc[1], loc[0], latlon=True, c='r', s=100)

    '''Handling the globe as a temporary PNG file and writing to an HTML file'''
    tmpfile = BytesIO()
    flatMap.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')

    html = '<img src=\'data:image/png;base64,{}\' width="100%" height="100%">\n'.format(encoded)

    with open('globe.html', 'w') as f:
        f.write(html)

    '''GloboSphere plot'''
    globoSphereMap = plt.figure(figsize=(9, 6))

    # set perspective angle
    lat_viewing_angle = loc[0]
    lon_viewing_angle = loc[1]

    # define color maps for water and land
    ocean_map = (plt.get_cmap('ocean'))(210)
    cmap = plt.get_cmap('gist_earth')

    # call the basemap and use orthographic projection at viewing angle
    globoSphereBasemap = Basemap(projection='ortho',
                                 lat_0=lat_viewing_angle, lon_0=lon_viewing_angle)

    # coastlines, map boundary, fill continents/water, fill ocean, draw countries
    globoSphereBasemap.drawcoastlines()
    globoSphereBasemap.drawmapboundary(fill_color=ocean_map)
    globoSphereBasemap.fillcontinents(color=cmap(200), lake_color=ocean_map)
    globoSphereBasemap.drawcountries()

    # latitude/longitude line vectors
    lat_line_range = [-90, 90]
    lat_lines = 8
    lat_line_count = (lat_line_range[1] - lat_line_range[0]) / lat_lines

    merid_range = [-180, 180]
    merid_lines = 8
    merid_count = (merid_range[1] - merid_range[0]) / merid_lines

    globoSphereBasemap.drawparallels(np.arange(lat_line_range[0], lat_line_range[1], lat_line_count))
    globoSphereBasemap.drawmeridians(np.arange(merid_range[0], merid_range[1], merid_count))

    x, y = globoSphereBasemap(lon_viewing_angle, lat_viewing_angle)
    globoSphereBasemap.scatter(x, y, marker='o', color='#DDDDDD', s=3000, zorder=10, alpha=0.7,
                               edgecolor='#000000')
    globoSphereBasemap.scatter(x, y, marker='o', color='#000000', s=100, zorder=10, alpha=0.7,
                               edgecolor='#000000')

    plt.annotate('ISS here!', xy=(x, y), xycoords='data',
                 xytext=(-110, -10), textcoords='offset points',
                 color='k', fontsize=20, bbox=dict(facecolor='w', alpha=0.5),
                 arrowprops=dict(arrowstyle="fancy", color='k'),
                 zorder=20)

    tmpfile2 = BytesIO()
    globoSphereMap.savefig(tmpfile2, format='png')
    encoded2 = base64.b64encode(tmpfile2.getvalue()).decode('utf-8')

    html2 = '<img src=\'data:image/png;base64,{}\' width="100%" height="100%">\n'.format(encoded2)

    with open('globe.html') as fobj:
        text = fobj.read()

    with open('globe.html', 'a') as fobj:
        if text.endswith('\n'):
            fobj.write('\n')
        fobj.write(html2)

    folium.map.Marker(
        location=loc,
        icon=DivIcon(
            icon_anchor=(-150, -50),
            html=f'<iframe src="globe.html" height=300 width=500></iframe>',
        )
    ).add_to(m)

    '''Saving the map file'''
    m.save('mp.html')

    '''The auto-refresh functionality'''
    with open("mp.html", "r") as in_file:
        buf = in_file.readlines()

    with open("mp.html", "w") as out_file:
        for line in buf:
            if line == '    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />\n':
                line = line + '''        <script type="text/javascript" src="https://livejs.com/live.js"></script>\n'''
            out_file.write(line)

    """Sleep a little. A performance strategy and also to keep the view pleasant."""
    time.sleep(30)




