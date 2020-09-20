import sys
import fitz
import os
import random
from flask import Flask, request, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename

from routes.sync import sync
from routes.reset import reset
from routes.upload import upload
from routes.covers import covers
from routes.toc import toc
from routes.toa import toa
from routes.cases import cases
from routes.review import createOutputFile
from routes.covers_key import covers_key
from routes.toc_key import toc_key
from routes.toa_key import toa_key
from routes.toc_insert import toc_insert
from routes.delete_case import delete_case
from routes.covers_pdf import covers_pdf
from routes.toc_pdf import toc_pdf
from routes.toa_pdf import toa_pdf
from routes.delete_toc_entry import delete_toc_entry
from routes.delete_toa_entry import delete_toa_entry
from routes.delete_toc_entries import delete_toc_entries
from routes.delete_toa_entries import delete_toa_entries
from routes.toa_insert import toa_insert


from utils.misc.find_index_of_entry_with_id import find_index_of_entry_with_id

from doc import get_my_doc, set_my_doc
from check_server import check_server

# TO START THE SERVER IN THE COMMAND LINE
# set FLASK_APP=app.py
# python -m flask run

app = Flask(__name__, static_url_path="", static_folder="static")
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
CORS(app)

check_server()


@app.route('/sync', methods=['GET'])
def syncRoute():
    default_data = sync()
    return default_data


@app.route('/reset', methods=['GET'])
def resetRoute():
    data = reset()
    return data


@app.route('/upload', methods=['POST'])
def uploadRoute():
    upload_data = upload(request)
    return upload_data


@app.route('/cases', methods=['POST'])
def casesRoute():
    upload_page = cases(request)
    return upload_page


@app.route('/cases/<id_number>', methods=['DELETE'])
def caseDelete(id_number):
    uploads = delete_case(id_number)
    return uploads


@app.route('/covers', methods=['GET'])
def coversRoute():
    cover_page = covers()
    return cover_page


@app.route('/covers/<key>', methods=['POST'])
def coversKeyRoute(key):
    cover_page = covers_key(key, request)
    return cover_page


@app.route('/covers/pdf', methods=['GET'])
def coversPDFRoute():
    output = covers_pdf()
    return send_file(output)


@app.route('/toc/pdf', methods=['GET'])
def tocPDFRoute():
    output = toc_pdf()
    return send_file(output)


@app.route('/toa/pdf', methods=['GET'])
def toaPDFRoute():
    output = toa_pdf()
    return send_file(output)


@ app.route('/toc', methods=['GET'])
def tocRoute():
    toc_page = toc()
    return toc_page


@ app.route('/toc/entries/<IDNumber>', methods=['DELETE'])
def tocDelete(IDNumber):
    entries = delete_toc_entry(IDNumber)
    return entries


@ app.route('/toc/entries', methods=['DELETE'])
def tocDeleteAll():
    entries = delete_toc_entries()
    return entries


@ app.route('/toa/entries', methods=['DELETE'])
def toaDeleteAll():
    entries = delete_toa_entries()
    return entries


@ app.route('/toc/entries/<IDNumber>/<direction>', methods=['PUT'])
def tocChange(IDNumber, direction):
    if str(direction) != str(0):
        entries = toc_insert(IDNumber, direction)
        return entries
    else:
        entries = toc_key(request)
        return entries


@ app.route('/toa', methods=['GET'])
def toaRoute():
    toa_page = toa()
    return toa_page


@ app.route('/toa/entries/<IDNumber>/<direction>', methods=['PUT'])
def toaChange(IDNumber, direction):
    if str(direction) != str(0):
        entries = toa_insert(IDNumber, direction)
        return entries
    else:
        entries = toa_key(request)
        return entries


@ app.route('/toa/entries/<IDNumber>', methods=['DELETE'])
def toaDelete(IDNumber):
    entries = delete_toa_entry(IDNumber)
    return entries


@ app.route('/review', methods=['GET'])
def reviewRoute():
    output_path = createOutputFile()
    return {
        'outputPath': output_path
    }


if __name__ == '__main__':
    app.run(host='localhost', debug=True)
