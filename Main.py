from Scraper import Scraper
from time import sleep
import datetime
import SMS

scraper = Scraper()
alreadyNotified = list()
alreadyPrinted = list()
startDate = datetime.datetime.now()
while True:
    for i in range(1, 25):
        try:
            half = scraper.getHalf(i)
            firstTeamName = scraper.getFirstTeam(i)
            firstTeamSeed = scraper.getFirstTeamSeed(i)
            firstTeamScore = int(scraper.getFirstTeamScore(i))
            secTeamName = scraper.getSecondTeam(i)
            secTeamSeed = scraper.getSecondTeamSeed(i)
            secTeamScore = int(scraper.getSecondTeamScore(i))
            minsLeft = int(scraper.getTimeLeft(i).split(":")[0])
            if i not in alreadyPrinted:
                print("Tracked index " + str(i) + ": ")
                print("[Madness Notifier]\n(" + firstTeamSeed + ")" + firstTeamName + " - " + str(firstTeamScore)
                                     + "\nvs\n(" + secTeamSeed + ")" + secTeamName + " - " + str(secTeamScore)
                                     + "\nwith " + str(minsLeft) + " mins to go")
                print()
                print(str(len(alreadyPrinted)) + " games have been tracked!")
                print()
                alreadyPrinted.append(i)
            if ("2" in half):
                if (firstTeamScore - secTeamScore <= 8 and firstTeamScore > secTeamScore) or (secTeamScore - firstTeamScore <= 8 and secTeamScore > firstTeamScore):
                    if (minsLeft <= 4):
                        if (i not in alreadyNotified):
                            # It is a game deemed worth watching, now we msg ourselves to let us know
                            print("Game is " + firstTeamName + " vs " + secTeamName)
                            print("Half is " + half)
                            print("Minsleft is " + str(minsLeft))
                            SMS.send("[Madness Notifier]\n(" + firstTeamSeed + ")" + firstTeamName + " - " + str(firstTeamScore)
                                     + "\nvs\n(" + secTeamSeed + ")" + secTeamName + " - " + str(secTeamScore)
                                     + "\nwith " + str(minsLeft) + " mins to go")
                            print("Message has been sent")
                            print()
                            alreadyNotified.append(i)
        except Exception as e:
            continue
    sleep(20)  # Sleeps every 20 seconds
    if startDate.day != datetime.datetime.now().day:
        startDate = datetime.datetime.now()
        alreadyNotified = list()
        alreadyPrinted = list()