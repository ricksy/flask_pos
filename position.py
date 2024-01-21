# get user coordinates
#use flask and folium to create a page with a map widget where the user can click on a location and get the coordinates

from flask import Flask, render_template, request
import folium

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map', methods=['POST'])
def map():
    lat = request.form['lat']
    lon = request.form['lon']
    map = folium.Map(location=[lat, lon], zoom_start=10)
    map.save('templates/map.html')
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True)

