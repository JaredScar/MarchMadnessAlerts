from lxml import html
import requests

class Scraper:
    def __init__(self):
        self.page = requests.get('https://www.ncaa.com/scoreboard/basketball-men/d1')
        self.content = html.fromstring(self.page.content)
    def getFirstTeam(self, divIndex):
        teamName = self.content.xpath('//*[@id="scoreboardGames"]/div/div[' + str(divIndex) + ']/a/ul/li[1]/span[2]')[0].text
        return teamName
    def getFirstTeamScore(self, divIndex):
        # //*[@id="scoreboardGames"]/div/div/a/ul/li[1]/span[4]
        teamScore = self.content.xpath('//*[@id="scoreboardGames"]/div/div[' + str(divIndex) + ']/a/ul/li[1]/span')[2].text
        return teamScore
    def getSecondTeam(self, divIndex):
        teamName = self.content.xpath('//*[@id="scoreboardGames"]/div/div[' + str(divIndex) + ']/a/ul/li[2]/span[2]')[0].text
        return teamName
    def getSecondTeamScore(self, divIndex):
        teamScore = self.content.xpath('//*[@id="scoreboardGames"]/div/div[' + str(divIndex) + ']/a/ul/li[2]/span')[2].text
        return teamScore
    def getFirstTeamSeed(self, divIndex):
        seed = self.content.xpath('//*[@id="scoreboardGames"]/div/div[' + str(divIndex) + ']/a/ul/li[1]/span[1]')[0].text
        if seed is None:
            return "NR"
        return seed
    def getSecondTeamSeed(self, divIndex):
        seed = self.content.xpath('//*[@id="scoreboardGames"]/div/div[' + str(divIndex) + ']/a/ul/li[2]/span[1]')[0].text
        if seed is None:
            return "NR"
        return seed
    def getHalf(self, divIndex):
        self.page = requests.Session().get('https://www.ncaa.com/scoreboard/basketball-men/d1')
        self.content = html.fromstring(self.page.content)
        timeStr = self.content.xpath('//*[@id="scoreboardGames"]/div/div[' + str(divIndex) + ']/a/div[2]/span')
        for i in range(len(timeStr)):
            if(":" in timeStr[i].text):
                return timeStr[i].text.split(" ")[1]
    def getTimeLeft(self, divIndex):
        self.page = requests.Session().get('https://www.ncaa.com/scoreboard/basketball-men/d1')
        self.content = html.fromstring(self.page.content)
        #//*[@id="scoreboardGames"]/div/div[3]/a/div[2]/span
        # Regular game: //*[@id="scoreboardGames"]/div/div[3]/a/div[2]/span
        timeStr = self.content.xpath('//*[@id="scoreboardGames"]/div/div[' + str(divIndex) + ']/a/div[2]/span')
        for i in range(len(timeStr)):
            if(":" in timeStr[i].text):
                return timeStr[i].text.split(" ")[0]