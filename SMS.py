import smtplib
carriers = {
    'att': '@mms.att.net',
    'tmobile': '@tmomail.net',
    'verizon': '@vtext.com',
    'sprint': '@page.nextel.com'
}

def send(message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    file = open('authentication.txt', 'r')
    ind = 0
    loginUser = ''
    loginPass = ''
    for line in file:
        if (len(line) > 2):
            if(ind == 0):
                loginUser = line
                ind += 1
            elif(ind == 1):
                loginPass = line
                ind += 1
                server.login(loginUser, loginPass)
            else:
                # These are the phone numbers we text
                to_number = line.split(":")[0]
                to_number += carriers[line.split(":")[1]]
                server.sendmail(loginUser, to_number, message)
# Example:
#send("[Madness Notifier]\n(5)Michigan - 56\nvs\n(2)Michigan State - 59")