import json
import urllib.parse
import requests

main_api = "http://www.mapquestapi.com/directions/v2/alternateroutes?"
key = "46cjGY1pPvRH1j4A5H0TkABTAtXSsksV"

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    maxRoute = input("Max Routes: ") # the maximum number of routes to return. def: 1
    if maxRoute == "quit" or maxRoute == "q":
        break
    timeOverage = input("Time Overage: ") # The percentage by which the expected drive time of an alternate is allowed to exceed the expected drive time of the original route. def: 25
    if timeOverage == "quit" or timeOverage == "q":
            break
        
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest, "maxRoute": maxRoute, "timeOverage": timeOverage})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Alternate Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
        print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print ("Route Type:      "+ (json_data["route"]["options"]["routeType"]))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")

