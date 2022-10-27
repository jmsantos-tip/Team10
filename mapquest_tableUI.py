import urllib.parse
import requests
from rich.table import Table
from rich.console import Console
from colorama import Fore, Back, Style

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "rJA9z4RMMABsDGttX89b20RnA6NBIMGZ"


while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key":key, 
        "from":orig, "to":dest})
    json_data = requests.get(url).json()
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    table1 = Table(title="API")
    rows1 = [
        [str(json_status), "A successful route call."]
    ]
    column1 = ["Status Code", "Message"]
    table2 = Table(title="Destination")
    rows2 = [
        [(orig),(dest)]
    ]
    column2 = ["From", 'To']
    table3 = Table(title="Trip Details")
    table4 = Table(title="API")
    rows4 = [
        [str(json_status), "Invalid user inputs for one or both locations."]
    ]
    table5 = Table(title="API")
    rows5 = [
        [str(json_status), "Missing and entry for one or both locations."]
    ]
    table6 = Table(title="API")
    rows6 = [
        [str(json_status), "Refer to:", "https://developer.mapquest.com/documentation/directions-api/status-codes"]
    ]
    column6 = ["Status Code", "Message", "Link"]
    table7 = Table(title="Direction")
    column7 = ["Narratives", "Direction"]
    rows7=[
        
    ]
    if json_status == 0:
        rows3 = [
        [(json_data["route"]["formattedTime"]), (str("{:.2f}".format((json_data["route"]["distance"])*1.61)))]
        ]
        column3 = ["Trip Duration", "Kilometers"]
        for column in column1:
            table1.add_column(column)
        for row in rows1:
            table1.add_row(*row, style="bright_green")
        for column in column2:
            table2.add_column(column)
        for row in rows2:
            table2.add_row(*row, style='bright_green')
        for column in column3:
            table3.add_column(column)
        for row in rows3:
            table3.add_row(*row, style="bright_green")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
           rows7.append([(each["narrative"]), " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)")])
        for column in column7:
            table7.add_column(column)
        for row in rows7:
            table7.add_row(*row, style="bright_green")
        console = Console()
        console.print(table1)
        console.print(table2)
        console.print(table3)
        console.print(table7)
    elif json_status == 402:
        for column in column1:
            table4.add_column(column)
        for row in rows4:
            table4.add_row(*row, style="bright_green")
        console = Console()
        console.print(table4)
    elif json_status == 611:
        for column in column1:
            table5.add_column(column)
        for row in rows5:
            table5.add_row(*row, style="bright_green")
        console = Console()
        console.print(table5)
    else:
        for column in column6:
            table6.add_column(column)
        for row in rows6:
            table6.add_row(*row, style="bright_green")
        console = Console()
        console.print(table6)
