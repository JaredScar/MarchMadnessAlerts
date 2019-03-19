from Scraper import Scraper
from time import sleep
import datetime
import SMS

scraper = Scraper()
alreadyNotified = list()
startDate = datetime.datetime.now()
while True:
    sleep(20) # Sleeps every 20 seconds
    for i in range(1, 25):
        half = scraper.getHalf(i)
        firstTeamName = scraper.getFirstTeam(i)
        firstTeamSeed = scraper.getFirstTeamSeed(i)
        firstTeamScore = int(scraper.getFirstTeamScore(i))
        secTeamName = scraper.getSecondTeam(i)
        secTeamSeed = scraper.getSecondTeamSeed(i)
        secTeamScore = int(scraper.getSecondTeamScore(i))
        minsLeft = int(scraper.getTimeLeft(i).split(":")[0])
        if ("2" in half):
            if (firstTeamScore - secTeamScore <= 8 and firstTeamScore > secTeamScore) or (secTeamScore - firstTeamScore <= 8 and secTeamScore > firstTeamScore):
                if (minsLeft <= 4):
                    if (i not in alreadyNotified):
                        # It is a game deemed worth watching, now we msg ourselves to let us know
                        alreadyNotified.append(i)
                        SMS.send("[Madness Notifier]\n(" + firstTeamSeed + ")" + firstTeamName + " - " + str(firstTeamScore)
                                 + "\nvs\n(" + secTeamSeed + ")" + secTeamName + " - " + str(secTeamScore))
    if startDate.day != datetime.datetime.now().day:
        startDate = datetime.datetime.now()
        alreadyNotified = []