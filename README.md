# March Madness Alerts (SMS)
Don't miss a beat with the March Madness Alerts system! This system informs you of all
games that come down to the wire. If a game is within 8 points under the 4 minute mark
in the 2nd half, then you will get a text message of the game's score and how much time
there is left to go.
## Getting set up
You will need to create a google account first for this alert system. Something simple like
MarchMadnessAlerts123@gmail.com would work... You will then need to go to the google
account settings. You will then need to turn less secure apps access ON.

![Security account settings](https://i.gyazo.com/fa9a69255a9fc441d020ac41d7ee1a19.png)

![Less Secure Apps](https://i.gyazo.com/7dd5d3566ca92d678d74fc75dab0fbc7.png)

After these steps, you will then need to go into the exampleFile.txt and change the name
of the file to "authentication.txt" as well as replace 'myEmail@gmail.com' with your
email address. Replace 'myGmailPassword' with the password to your gmail account.
The next step is adding in the phone numbers. You will input all the phone numbers
underneath your email and password within the file. An example of a correct authentication
file is provided below.

```
jaredscar@gmail.com
password321

6315554444:verizon
6314445555:tmobile
```

The providers that are supported to be texted by using this system are listed below.

Happy March Madness!
## Providers supported
##### AT&T
Carrier: att
##### T-Mobile
Carrier: tmobile
##### Verizon
Carrier: verizon
##### Sprint
Carrier: sprint