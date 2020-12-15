from os import path
import os

from flask import Flask, request, jsonify, render_template, redirect, url_for
from waitress import serve

from textFormater import textFormater
from apiHandler import apiHandler
from fileManager import fileManager

app = Flask(__name__)

@app.route('/')
def home():
    #return the homepage
    return render_template('./index.html')

@app.route('/search/orgnr', methods={'POST'})
def searchOrgNr():

    nr = request.form['nm']

    #format the number
    nr = textFormater.format(nr)

    #get dictionary from api
    opplysningerMapping = apiHandler.getDictionary(nr)

    #get cord from api
    coordinatesMapping = apiHandler.getCoordinates(nr)

    #check if something is saved previously
    information = fileManager.readInfo(nr)

    return render_template('./search.html', nr=nr, information=information, opplysningerMapping=opplysningerMapping, coordinatesMapping=coordinatesMapping)

@app.route('/search/postnr', methods={'POST'})
def searchPostNr():
    nr = request.form['nm']

    #format the number
    nr = textFormater.format(nr)

    companies = apiHandler.getPostNumbers(nr)

    return render_template('./postnr.html', companies = companies)

@app.route('/search/save', methods={'POST'})
def save():
    #pick out relevant information
    nr = request.form['nr']

    #format the number
    nr = textFormater.format(nr)

    #Pick out written text
    writtenInformation = request.form['information']

    #save information
    fileManager.saveInfo(nr, writtenInformation)

    return redirect(url_for('saved'))

@app.route('/search/orgnr/remvove', methods={'POST'})
def remove():
    #get org number that will be deleted
    nr = request.form['delete']

    #remove nr from folder
    fileManager.removeNr(nr)

    #refresh page
    return redirect(url_for('saved'))

@app.route('/saved')
def saved():
    #get filenames from data folder
    orgNrs = fileManager.getAllOrgNr()

    #get names from org numbers
    names = apiHandler.getNames(orgNrs)

    #zip org numbers and names for use in a for-loop later
    orgNrsAndNames = zip(orgNrs, names)

    #return saved.html with names and org.numbers
    return render_template('./saved.html', orgNrsAndNames = orgNrsAndNames)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    #serve(app, host='0.0.0.0', port=8888)