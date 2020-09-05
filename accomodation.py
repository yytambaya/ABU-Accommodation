import requests;
import selenium;
from selenium import webdriver;
from bs4 import BeautifulSoup;
from twilio.rest import Client;



url = 'https://portal.abu.edu.ng/index.php';
accom_url = 'https://portal.abu.edu.ng/accommodation/reservation.php';
params = {'username': 'u19cs100', 'password': 'passowrd'};
s = requests.session();
response = s.post(url, data=params);
if(response.status_code == 200):
    soap = BeautifulSoup(response.content, 'html.parser');
    #print(soap.prettify());
    accom = s.get(accom_url);
    if(accom.status_code == 200):
        accom_soap = BeautifulSoup(accom.content, "html.parser");
        #print(accom_soap.prettify());
        rooms_url = 'https://portal.abu.edu.ng/accommodation/reservation.php';
        rooms = s.post(rooms_url);
        if(rooms.status_code == 200):
            r_soup = BeautifulSoup(rooms.content, "html.parser")
            text = r_soup.get_text()
            if(text.find('Shehu') != -1 or text.find('Dan') != -1):
                #print(text);
                account_sid = 'xxxxxxxxxxxxxxxxxxxxxxxx'
                auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                body ='ABU accommodation is opened! check now',
                from_='xxxxxxxxxxx',
                to='xxxxxxxxxxx'
                )

                print("Found and Sent!");
            else:
                print("Blocks not uploaded");

    else:
        print("Request not successful")
else:
    print("Request not successful");


