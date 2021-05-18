# -*- coding: utf-8 -*-
"""
Created on Wed May 12 16:04:24 2021

@author: Noa Mor
"""


import json
import requests
import pprint

  
##מציאת שלושת הערים הרחוקות מתל אביב
def threeMost (citiesDict):
    firstKM= 0
    secondKM= 0
    thirdKM= 0  
##מציאת העיר הכי רחוקה מתל אביב
    for key in citiesDict:
        km= str(citiesDict[key]).split()[1].split(',')
        numKMstr=""
        for num in km:
            numKMstr+=num
            numKM=float(numKMstr)
            if numKM >= firstKM :
                firstKM= numKM
                firstCity= key
##מציאת העיר השניה הרחוקה מתל אביב
    for key in citiesDict:
        km= str(citiesDict[key]).split()[1].split(',')
        numKMstr=""
        for num in km:
            numKMstr+=num
            numKM=float(numKMstr)
            if key != firstCity:
                if numKM >= secondKM :
                    secondKM= numKM
                    secondCity= key
##מציאת העיר השלישי הרחוקה מתל אביב
    for key in citiesDict:
        km= str(citiesDict[key]).split()[1].split(',')
        numKMstr=""
        for num in km:
            numKMstr+=num
            numKM=float(numKMstr)
            if key != firstCity and key != secondCity :
                if numKM >= thirdKM :
                    thirdKM= numKM
                    thirdCity= key       
##הדפסת הערים הרחוקות מתל אביב
    print(" ")
    print("The three cities furthest from Tel Aviv:")
    print("1. "+firstCity+ ": "+ str(firstKM)+ " KM")
    print("2. "+secondCity+ ": "+ str(secondKM)+ " KM")
    print("3. "+thirdCity+ ": "+ str(thirdKM)+ " KM")
    
    

##יצירת מילון הכולל 5 ערים ואת המידע עבורם
citiesDict= {}
numOfCities=0
apiKey= input('please enter your API key:')

try:

    file= open("dests.txt" ,encoding='utf-8')
    for city in file:
        numOfCities+=1
        desCity=city.rstrip()
        urlDisMat= "https://maps.googleapis.com/maps/api/distancematrix/json?&origins=תל אביב&destinations=%s&key=%s" % (desCity, apiKey) 
        responseDisMat= requests.get(urlDisMat).json()
        urlGeo= "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (desCity,apiKey)
        responseGeo= requests.get(urlGeo).json()
        title= str(responseDisMat['destination_addresses']).rsplit("'")[1]
        distance= "distance: "+ str(responseDisMat['rows'][0]['elements'][0]['distance']['text'])
        time= "time: "+str(responseDisMat['rows'][0]['elements'][0]['duration']['text'])
        geomLat= "lat: "+ str(responseGeo['results'][0]['geometry']['bounds']['northeast']['lat'])
        geomLng= "lng: "+ str(responseGeo['results'][0]['geometry']['bounds']['northeast']['lng'])
        data= (distance, time, geomLat, geomLng)
        citiesDict[title]= data
    if numOfCities == 5:
        pprint.pprint(citiesDict)
        threeMost(citiesDict)
    if numOfCities < 5:
        print ("The file contains less than five cities")
    if numOfCities > 5:
        print ("The file contains more than five cities")
except:
    print("There is an error in the file")