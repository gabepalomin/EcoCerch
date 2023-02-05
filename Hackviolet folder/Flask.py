from flask import Flask, redirect, url_for, render_template, request
import requests
from bs4 import BeautifulSoup
import html.parser
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys



app = Flask(__name__)

@app.route('/', methods=["GET", "POST"],)
def home():
    if request.method == "POST":

        certsGathered=[]

        orgName= request.form["organize"]
        GS_URL1 = ("https://certified.greenseal.org/companies?limit=120&filters%5Bletter_start%5D=0&filters%5Bletter_end%5D=0&offset=0#index-table")
        GS_URL2 = ("https://certified.greenseal.org/companies?limit=120&filters%5Bletter_start%5D=0&filters%5Bletter_end%5D=0&offset=120#index-table")
        GS_URL3 = ("https://certified.greenseal.org/companies?limit=120&filters%5Bletter_start%5D=0&filters%5Bletter_end%5D=0&offset=240#index-table")
        gs_urls = [GS_URL1, GS_URL2, GS_URL3]


        #Climate Neutral URLS
        CN_URL1 = ("https://www.climateneutral.org/certified-brands")
        CN_URL2 = ("https://www.climateneutral.org/certified-brands?page=2")
        CN_URL3 = ("https://www.climateneutral.org/certified-brands?page=3")
        CN_URL4 = ("https://www.climateneutral.org/certified-brands?page=4")
        CN_URL5 = ("https://www.climateneutral.org/certified-brands?page=5")
        CN_URL6 = ("https://www.climateneutral.org/certified-brands?page=6")
        CN_URL7 = ("https://www.climateneutral.org/certified-brands?page=7")
        CN_URL8 = ("https://www.climateneutral.org/certified-brands?page=8")
        CN_URL9 = ("https://www.climateneutral.org/certified-brands?page=9")
        CN_URL10 = ("https://www.climateneutral.org/certified-brands?page=10")
        CN_URL11 = ("https://www.climateneutral.org/certified-brands?page=11")
        CN_URL12 = ("https://www.climateneutral.org/certified-brands?page=12")
        CN_URL13 = ("https://www.climateneutral.org/certified-brands?page=13")
        CN_URL14 = ("https://www.climateneutral.org/certified-brands?page=14")
        CN_URL15 = ("https://www.climateneutral.org/certified-brands?page=15")
        CN_URL16 = ("https://www.climateneutral.org/certified-brands?page=16")
        CN_URL17 = ("https://www.climateneutral.org/certified-brands?page=17")
        CN_URL18 = ("https://www.climateneutral.org/certified-brands?page=18")
        CN_URL19 = ("https://www.climateneutral.org/certified-brands?page=19")
        CN_URL20 = ("https://www.climateneutral.org/certified-brands?page=20")
        CN_URL21 = ("https://www.climateneutral.org/certified-brands?page=21")
        cn_urls = [CN_URL1, CN_URL2, CN_URL3, CN_URL4, CN_URL5, CN_URL6, CN_URL7, CN_URL8, CN_URL9, CN_URL10, CN_URL11, CN_URL12, CN_URL13, CN_URL14, CN_URL15, CN_URL16, CN_URL17, CN_URL18, CN_URL19, CN_URL20, CN_URL21]


        #Rainforest Alliance URLS
        RA_URL1 = ("https://www.rainforest-alliance.org/find-certified/?fwp_by_consumer_location=united-states&fwp_by_commodity=coffee")
        RA_URL2 = ("https://www.rainforest-alliance.org/find-certified/?fwp_by_consumer_location=united-states&fwp_by_commodity=coffee&fwp_paged=2")
        RA_URL3 = ("https://www.rainforest-alliance.org/find-certified/?fwp_by_consumer_location=united-states&fwp_by_commodity=coffee&fwp_paged=3")
        RA_URL4 = ("https://www.rainforest-alliance.org/find-certified/?fwp_by_consumer_location=united-states&fwp_by_commodity=coffee&fwp_paged=4")
        RA_URL5 = ("https://www.rainforest-alliance.org/find-certified/?fwp_by_consumer_location=united-states&fwp_by_commodity=coffee&fwp_paged=5")
        RA_URL6 = ("https://www.rainforest-alliance.org/find-certified/?fwp_by_consumer_location=united-states&fwp_by_commodity=coffee&fwp_paged=6")
        RA_URL7 = ("https://www.rainforest-alliance.org/find-certified/?fwp_by_consumer_location=united-states&fwp_by_commodity=coffee&fwp_paged=7")
        RA_URL8 = ("https://www.rainforest-alliance.org/find-certified/?fwp_by_consumer_location=united-states&fwp_by_commodity=coffee&fwp_paged=8")
        RA_URL9 = ("https://www.rainforest-alliance.org/find-certified/?fwp_by_consumer_location=united-states&fwp_by_commodity=coffee&fwp_paged=9")
        RA_URL10 = ("https://www.rainforest-alliance.org/find-certified/?fwp_by_consumer_location=united-states&fwp_by_commodity=coffee&fwp_paged=10")
        ra_urls = [RA_URL1, RA_URL2, RA_URL3, RA_URL4, RA_URL5, RA_URL6, RA_URL7, RA_URL8, RA_URL9, RA_URL10]


        #Leaping Bunny URLS
        LB_URL1 = ("https://www.leapingbunny.org/shop-cruelty-free/where-buy")


        #defining lists for each certification
        gs_companies = []
        cn_companies = []
        ra_companies = []
        lb_companies = []

        #Search bar
        search= orgName
        search_lower = search.replace(' ', '-').lower()


        #Green Seal code
        for url in gs_urls:
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')
            for name in soup.find_all('img'):
                gs_companies.append(name.get('alt'))

        gs_companies_str = [str(company) for company in gs_companies]
        gs_companies_lower = [company.replace(' ', '-').lower() for company in gs_companies_str]

        saying = "green seal-certified products and services from "

        if saying + search_lower in gs_companies_lower:
            
            green_seal ='Green Seal Certification'
            certsGathered.append(green_seal)


        #Climate Neutral code
        for url in cn_urls:
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')
        for name in soup.find_all('img'):
            cn_companies.append(name.get('alt'))

        cn_companies_str = [str(company) for company in cn_companies]
        cn_companies_lower = [company.replace(' ', '-').lower() for company in cn_companies_str]

        if search_lower in cn_companies_lower:
            climate_neutral = 'Climate Neutral Certification'
            certsGathered.append(climate_neutral)
        


        #Rainforest Alliance code
        for url in ra_urls:
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')
            for link in soup.find_all('a'):
                ra_companies.append(link.get('href'))

        ra_companies_str = [str(company) for company in ra_companies]
        ra_companies_lower = [company.replace(' ', '-').lower() for company in ra_companies_str]

        ra_saying = "https://www.rainforest-alliance.org/find-certified/"

        if ra_saying + search_lower + "/" in ra_companies_lower:
            rainforest_alliance='Rainforest Alliance Certification'
            certsGathered.append(rainforest_alliance)

        


        #Leaping Bunny code
        r = requests.get(LB_URL1)
        soup = BeautifulSoup(r.content, 'html.parser')
        for name in soup.find_all('a'):
            link = name.get('href')
            link_str = str(link)
            index = link_str.find(search_lower)
            if index != -1:
                lb_companies.append(search_lower)

        lb_companies_str = [str(company) for company in lb_companies]
        lb_companies_lower = [company.replace(' ', '-').lower() for company in lb_companies_str]

        if search_lower in lb_companies_lower:
            leaping_bunny='Leaping Bunny Certification'
            certsGathered.append(leaping_bunny)
        
        
        return f'{orgName} has these certifications.....{certsGathered}'

    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)

    
    
