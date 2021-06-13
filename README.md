# COVID-19 Vaccine Tracker
The purpose of this project is to notify the availability of vaccines at the specified disctrict in India.
It uses the APIs of the CoWIN website to access this information.
The vaccine availability is periodically checked and once available, it is notified via desktop notifications.

The following parameters can be set to track the vaccine:

* MAX_ATTEMPTS : Maximum Number of Attempts on the COWIN Site 
* MAX_CENTERS  : Maximum No. of Centers to be shown If Slots are Available
* DISTRICT_ID  : Id of the district Eg. Hyderabad: 581, Chennai: 571
* DATE         : Date From which Availability needs to be checked
* VACCINE      : Options for vaccine: COVISHIELD, COVAXIN,
