from flask import Blueprint
from flask import request,Response
from flask import url_for,redirect
from flask import jsonify
import os
import sys

import json

#defining new Blueprint
iterBp=Blueprint("iteration",__name__)


import calculation 
from calculation import *

@iterBp("/api/iterations",methods=['POST'])
def iterPost():
       
    if request.form=='POST':
        iterations()
        # # taking current features from json file
        # dicts=json.loads("iteration.json")
        # # traversing through dict
        # for dict_ in dicts:
        #     dict_['step'] 

        #     #redirecting to /api/iterations/step:int
        #     return redirect("/api/iterations/)
        # redirecting current route to /api/iterations/step:int
        dicts=json.loads("iteration.json")
        return jsonify(dicts)


@iterBp("/api/iterations/int:<step>",methods=['GET'])
def iterGet(step):
    #taking steps
    if request.method=='GET':
        data=request.get_json()

        return render_template_string("<label>{}</label>" \
        "<label>{}</label>" \
        "<label>{}</label>" \
        .format(data['step'],data['relativeError'],data['success']))
        


    

