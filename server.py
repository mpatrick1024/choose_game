from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    print("*"*80)
    print("in the root route, index function")
    return render_template('index.html')

@app.route("/downtown")
def downtown():
    print("*"*80)
    print("in the downtown function")
    return render_template ("downtown.html")

@app.route("/downtown/sears_tower")
def sears_tower():
    print("*"*80)
    print("in the sears tower function")
    return render_template ("downtown/sears_tower.html")

@app.route("/downtown/bean")
def bean():
    print("*"*80)
    print("in the bean function")
    return render_template ("downtown/bean.html")

@app.route("/downtown/mag_mile")
def mag_mile():
    print("*"*80)
    print("in the mag_mile function")
    return render_template ("downtown/mag_mile.html")


@app.route("/hyde_park")
def hyde_park():
    print("*"*80)
    print("in the hyde park function")
    return render_template ("hyde_park.html")

@app.route("/hyde_park/giordanos")
def giordanos():
    print("*"*80)
    print("in the giordanos function")
    return render_template ("hyde_park/giordanos.html")

@app.route("/hyde_park/valois")
def valois():
    print("*"*80)
    print("in the valois function")
    return render_template ("hyde_park/valois.html")

@app.route("/hyde_park/mellow_yellow")
def mellow_yellow():
    print("*"*80)
    print("in the mellow yellow function")
    return render_template ("hyde_park/mellow_yellow.html")


@app.route("/north_side")
def north_side():
    print("*"*80)
    print("in the north side function")
    return render_template ("north_side.html")

@app.route("/north_side/thrift_store")
def thrift_store():
    print("*"*80)
    print("in the thrift store function")
    return render_template ("north_side/thrift_store.html")

@app.route("/north_side/chi_music_exchange")
def chi_music_exchange():
    print("*"*80)
    print("in the thrift store function")
    return render_template ("north_side/chi_music_exchange.html")

@app.route("/north_side/vinyl_records")
def vinyl_records():
    print("*"*80)
    print("in the thrift store function")
    return render_template ("north_side/vinyl_records.html")



app.run(debug=True)