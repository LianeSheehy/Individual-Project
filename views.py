"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from rest_framework.decorators import api_view 
from rest_framework.response import Response 


@api_view(['GET']) 

def barchart_data(request): 

    data = [ 

        {"id":  1, "description" : "North", "value": 25 }, 

        {"id" : 2, "description" : "South", "value" : 15}, 

        {"id" : 3, "description" : "East", "value" : 12}, 

        {"id" : 4, "description" : "West", "value" : 18} 

        ] 

    return Response({"data": data}) 

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'About.',
            'year':datetime.now().year,
        }

    )
import urllib.request 

import json 

 

 

def callRStudioTest(request): 

    """Renders the about page.""" 

    assert isinstance(request, HttpRequest) 

 

    data = { 

            "Inputs": { 

            }, 

        "GlobalParameters":  { 

        } 

    } 

 

    body = str.encode(json.dumps(data)) 

 

 

    # this will use my web services .. .after you test this replace with your own, get the url and api key from the studio ux 

 

    url = 'https://ussouthcentral.services.azureml.net/workspaces/2bb040b1a7184e8f8244b76a330078df/services/3aaacdec379d49109f7404f966ce0a09/execute?api-version=2.0&format=swagger' 

    api_key = 'Zr7naJiYSccvYTXQEKUWXCEgnxVqNA+kz9+U8SlN3UiYEv5XsPUGP4o9dJlrVBYKAgy+1oRJiT2oGOuFcllCmQ==' # Replace this with the API key for the web service 

    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)} 

 

    req = urllib.request.Request(url, body, headers) 

    response = urllib.request.urlopen(req) 

 

    result = response.read() 

    #print(result) 

 

    return render( 

        request, 

        'app/CallRStudioTest.html', 

        { 

            'title':'Call RStudio Test', 

            'server_response':result, 

            'year':datetime.now().year, 

        } 

    ) 

def d3js_barchart(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/d3js_barchart.html',
        {
            'title':'d3.js Bar Chart',
            'message':'D3.js Bar chart.',
            'year':datetime.now().year,
        }

    )





