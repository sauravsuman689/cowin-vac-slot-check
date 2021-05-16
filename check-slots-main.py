## Import the required python packages
import requests
import json
import telegramalert

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

'''
To Get the State details and state code
'''
#output = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/states",headers=headers)

#print(output.json())

'''
To get the district details using the state code
'''
#state_code = 16  ##Karnataka
#response_district = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(state_code),
#                               headers=headers)
#
#print(response_district.content)

## Define the district variables with their code

bang_rural_dist_id = 276   
bang_urban_dist_id = 265
bbmp_dist_id = 294

todaydate = '17-05-2021'


for dist in (276,265,294):
        response_avai = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(dist,todaydate),
                                headers=headers)
    ## To print the above url output in a file and check the content
    #print(response_avai.content)
    #    f = open("response.output",'wb')
    #    f.write(response_avai.content)
    #    f.close()
    #response_avai.json()
        
        if response_avai.ok:
            resp_input = response_avai.json()
            if resp_input["centers"]:
                for center in resp_input["centers"]:
                    for session in center["sessions"]:
                        
                        if session["min_age_limit"] == 18 and session["available_capacity"] >= 1:
                            
                            vac_date = session["date"]
                            vac_avail_count = session["available_capacity"]
                            district = center["district_name"]
                            vac_type = center["fee_type"]
                            vac_name = session["vaccine"]

                            message = f"{vac_type} - Total {vac_avail_count} Vaccine of company {vac_name} is available in {district} on {vac_date}"

                            ##Cal the telegram function to send alert
                            telegramalert.telegram_bot_sendtext(message)   
                        else:
                            print("No Vaccine is available in any given district.")
                
                