import smtplib, requests, time
from plyer import notification #for getting notification on your PC

#-------------------------------
MAX_ATTEMPTS = 10000            #Maximum Number of Attempts on the COWIN Site 
MAX_CENTERS  = 5                #Maximum No. of Centers to be shown If Slots are Available
DISTRICT_ID  = '581'            #Id of the district Eg. Hyderabad: 581, Chennai: 571
DATE         = '12-05-2021'     #Date From which Availability needs to be checked
VACCINE      = 'COVISHIELD'     #Options for vaccine: COVISHIELD, COVAXIN,
#-------------------------------

try:
    headers = { 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36' }
    url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={district_id}&date={date}'.format(
          district_id = DISTRICT_ID,
          date = DATE
          )
    for i in range(0,MAX_ATTEMPTS) :
        resp = requests.get(url, headers = headers)
        print("Response code:", resp)
        resp_json = resp.json()
        centers = resp_json['centers']
        cntr = 0
        for c in centers :
        
            if cntr >= MAX_CENTERS :
                break
                
            for s in c['sessions'] :
                if s['vaccine'] == VACCINE and s['available_capacity'] > 0:
                    print('-----------')
                    print(c['name'])
                    print(s)
                    print('-----------')
                    print('COUNTER:', cntr)
                    notification.notify(
                            #title of the notification,
                            title = "{vaccine} {available_capacity} at {centername} : {block}".format(
                                vaccine            = VACCINE
                                available_capacity = s['available_capacity'],
                                centername         = c['name'],     
                                block              = c['block_name']
                            ),
                            #the body of the notification
                            message = c['address'],
                            #creating icon for the notification
                            #we need to download a icon of ico file format
                            app_icon = None,
                            # the notification stays for 300sec (5 mins)
                            timeout = 300
                        )
                    cntr  = cntr + 1
                    time.sleep(10)
                    break
            
            
            
        time.sleep(5)
     
except:
    print("exception")
    
