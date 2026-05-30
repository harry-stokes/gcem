from flask import Flask, render_template, request
import subprocess
import platform

app = Flask(__name__)

# Detect operating system to select appropriate C executable
IS_WINDOWS = platform.system() == 'Windows'
EXE_NAME = 'integrated.exe' if IS_WINDOWS else './integrated'

# -------------------- MAIN MAP PAGE --------------------

@app.route('/')
def index():
    return render_template('map.html')

@app.route('/map')
def map_page():
    return render_template('map.html')

# -------------------- PATH FINDING --------------------

@app.route('/find_path', methods=['POST'])
def find_path():
    algorithm = request.form['choice']
    source = request.form['source']
    destination = request.form['destination']

    try:
        result = subprocess.run(
            [EXE_NAME, algorithm, source, destination],
            capture_output=True,
            text=True,
            check=True
        )
        output = result.stdout

        # Extract the OpenStreetMap URL (handles standard and prefixed lines)
        osm_link = None
        for line in output.splitlines():
            if "http" in line:
                idx = line.find("http")
                osm_link = line[idx:].strip()
                break

        # For comparison mode, run Dijkstra in the background to fetch the path URL
        if algorithm == '4':
            try:
                comp_res = subprocess.run(
                    [EXE_NAME, '1', source, destination],
                    capture_output=True,
                    text=True,
                    check=True
                )
                comp_out = comp_res.stdout
                for line in comp_out.splitlines():
                    if "http" in line:
                        idx = line.find("http")
                        osm_link = line[idx:].strip()
                        break
            except Exception:
                pass

    except subprocess.CalledProcessError as e:
        output = "Error calculating path: " + str(e)
        osm_link = None

    return render_template('map.html', result=output, osm_link=osm_link)

# -------------------- CAMPUS ZONE PAGES --------------------

@app.route('/gate1')
def gate1():
    return render_template('gate1.html')

@app.route('/btech')
def btech():
    return render_template('btech.html')

@app.route('/chanakya')
def chanakya():
    return render_template('chanakya.html')

@app.route('/kpblock')
def kpblock():
    return render_template('kpblock.html')

@app.route('/Parking')
def Parking():
    return render_template('Parking.html')

@app.route('/gehu')
def gehu():
    return render_template('gehu.html')

@app.route('/convention')
def convention():
    return render_template('convention.html')

@app.route('/marina')
def marina():
    return render_template('marina.html')

@app.route('/qbc')
def qbc():
    return render_template('qbc.html')

@app.route('/gate2')
def gate2():
    return render_template('gate2.html')

@app.route('/geubs')
def geubs2():
    return render_template('geubs.html')

@app.route('/Petroleum')
def Petroleum():
    return render_template('Petroleum.html')

@app.route('/girlshostel')
def girlshostel():
    return render_template('girlshostel.html')

@app.route('/aryabhatt')
def aryabhatt():
    return render_template('aryabhatt.html')

@app.route('/boys')
def boys():
    return render_template('boys.html')

@app.route('/csit')
def csit():
    return render_template('csit.html')

@app.route('/tuck')
def tuck():
    return render_template('tuck.html')

@app.route('/cafe')
def cafe():
    return render_template('cafe.html')

@app.route('/mech')
def mech():
    return render_template('mech.html')

@app.route('/param')
def param():
    return render_template('param.html')

@app.route('/santosh')
def santosh():
    return render_template('santosh.html')

@app.route('/civil')
def civil():
    return render_template('civil.html')

@app.route('/badminton')
def badminton():
    return render_template('badminton.html')

@app.route('/chatbot')
def chatbot():
    return render_template('INDEX.html')

@app.route('/ravi')
def ravi():
    return render_template('ravi.html')

# -------------------- SERVER START --------------------

if __name__ == '__main__':
    app.run(debug=True)
