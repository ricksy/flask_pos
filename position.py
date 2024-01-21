""" position.py


"""

from flask import Flask, render_template
from OpenSSL import SSL

import folium
import folium.plugins as plugins
app = Flask(__name__)

context = ('certs/cert.pem', 'certs/privkey.pem')

@app.route("/")
def components():
    """Extract map components and put those on a page."""
    m = folium.Map(
        location=[52.5200, 13.4050],
        width='50%',
        height='50%',
    )
    folium.plugins.LocateControl().add_to(m)

    m.get_root().render()
    header = m.get_root().header.render()
    body_html = m.get_root().html.render()
    script = m.get_root().script.render()
    return render_template('index.html', header=header, body_html=body_html, script=script)
 


if __name__ == "__main__":
    app.run(host='faraskur.com', port=8080, threaded=True, ssl_context=context, debug=True)