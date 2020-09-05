ABU-Accommodation is a python script that notifies students when Accomodation is opened by sending them a text message.
This is based on a University website call ABU in Nigeria.

How it works

The app uses python the request liberary to scrape the website and BeutifulSoap liberary to structure the data and some logics to figure out wheather
the accommodation is open or not. It's using Twillio to send the message


Use case

You only need to set your Twillio information and your phone number

Step 1: Go and register with Twillio and get account_id and auth_id
Step 2: Replace it with the one in ABU-accomodation.py file
Step 3: Go to Twillio and add the phone number you want to send to(Your phone number)
Stp 4: Replace the phone number in "to" section of ABU-accomodation.py
Step 5: Get copy the phone number given to you in Twillio which will be used to send the message
Step 6: Replace it in "from" section of ABU-accomodation.py 
 
What to edit 

account_sid = 'AC820d0ab6865bfdcae706e38a280a9da5'
auth_token = '60e88a540e223c132681328c6feb1778'                    
 
from_='+12566678481',
to='+2349054141255'
