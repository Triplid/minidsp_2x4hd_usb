from flask import Flask, jsonify, request
import hid

app = Flask(__name__)

VENDOR = 0x2752
PRODUCT = 0x0011

def open_device():
    dev = hid.device()
    dev.open(VENDOR, PRODUCT)
    return dev

def get_status():
    dev = open_device()
    dev.send_feature_report([0x00, 0x01])
    reply = dev.get_feature_report(0x01, 64)
    preset = reply[4]
    source = reply[5]
    dev.close()
    return preset, source

@app.get("/status")
def status():
    preset, source = get_status()
    return jsonify({"preset": preset, "source": source})

@app.post("/preset")
def set_preset():
    new = int(request.json["preset"])
    dev = open_device()
    dev.send_feature_report([0x00, 0x20, new])
    dev.close()
    return jsonify({"ok": True, "preset": new})

@app.post("/source")
def set_source():
    new = int(request.json["source"])
    dev = open_device()
    dev.send_feature_report([0x00, 0x21, new])
    dev.close()
    return jsonify({"ok": True, "source": new})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
