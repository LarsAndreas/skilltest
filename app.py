from os import path
import os

from flask import Flask, request, jsonify, render_template, redirect, url_for
from waitress import serve

from apiHelper import brregApiHandler

app = Flask(__name__)

@app.route('/')
def home():
    #return the homepage
    return render_template('./index.html')

def getHtmlWithInformation(nr, nrType):

    #remove whitespace
    nr = nr.replace(" ", "")

    #instantiate apiHelper
    apiHelper = brregApiHandler(nr)

    #get information from apiHandler class
    opplysningerMappingNameToValue = apiHelper.getopplMappingNameToValue()

    #check if something is saved previously
    if path.exists(f'static/data/{nrType}/{nr}'):
        with open(f'static/data/{nrType}/{nr}', 'r') as textfile:
            #return render template with saved information
            information = textfile.read()

            #check if there is any information regarding that number
            if(apiHelper.isError()):
                return render_template('./search.html', nr=nr, nrType=nrType, information=information, error=True)

            #return render template with relevant information
            return render_template('./search.html', nr=nr, nrType=nrType, information=information, opplysningerMapping=opplysningerMappingNameToValue)

    #check if there is any information regarding that number
    if(apiHelper.isError()):
        return render_template('./search.html', nr=nr, nrType=nrType, error=True)

    #There is no saved information, so don't append any
    return render_template('./search.html', nr=nr, nrType=nrType, opplysningerMapping=opplysningerMappingNameToValue)

@app.route('/search/orgnr', methods={'POST'})
def searchOrdNr():
    #check if request method is post
    if request.method == 'POST':
        #get number from form
        nr = request.form['nm']

        #return the right render template based on nr
        return getHtmlWithInformation(nr, "orgnr")
    return redirect(url_for('home'))

@app.route('/search/save', methods={'POST'})
def save():
    if request.method == 'POST':
        #pick out relevant information
        nr = request.form['nr']

        #remove whitespace
        nr = nr.replace(" ", "")

        typeNr = request.form['nrType']
        informationAboutCompany = request.form['information']

        #save information
        with open(f'static/data/{typeNr}/{nr}', 'w') as textfile:
            textfile.write(informationAboutCompany)
        return redirect(url_for('saved'))

@app.route('/search/orgnr/remvove', methods={'POST'})
def remove():
    if request.method == 'POST':
    #get org number that will be deleted
        nr = request.form['delete']
        path = f'./static/data/orgnr/{nr}'

        #check that you have a saved version of that org number
        if os.path.exists(path):
            #delete that file
            os.remove(path)

        #refresh page
        return redirect(url_for('saved'))

@app.route('/saved')
def saved():
    #get filenames from data folder
    orgNrs = list(os.listdir("./static/data/orgnr"))

    #get names from org numbers
    names = []
    for nr in orgNrs:
        apiHelper = brregApiHandler(nr)
        if not apiHelper.isError():
            names.append(apiHelper.getJsonFromApi()["navn"])
        else:
            names.append("Unknown Name")

    #zip org numbers and names for use in a for-loop later
    orgNrsAndNames = zip(orgNrs, names)

    #return saved.html template with org numbers and post numbers
    return render_template('./saved.html', orgNrsAndNames = orgNrsAndNames)

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)