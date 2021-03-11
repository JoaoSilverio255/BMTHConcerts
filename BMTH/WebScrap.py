from bs4 import BeautifulSoup
import requests

URL = "https://www.songkick.com/artists/347077-bring-me-the-horizon/calendar"
SOUP = BeautifulSoup(requests.get(URL).text, "lxml")
COUNTRY_LIST = ["UK" , "Russian Federation" , "Portugal" , "Germany" , "Norway" , "Switzerland" , "Austria" , "Ukraine"]

def bmth_concert():

    print("List of all locations available ")
    print(COUNTRY_LIST)
    print("")
    print("Please insert your prefered location and month: ")
    print("If you would like to see all , press Q ")
    LOCATION_FILTER = input(">")

    CONCERTS_LIST1 = SOUP.find_all("li", class_="event-listing after-ad")
    for INDEX, CONCERT_LIST1 in enumerate(CONCERTS_LIST1):
        CONCERTS_LOCATION1 = CONCERT_LIST1.find("strong", class_="primary-detail").text
        CONCERTS_ARENA = CONCERT_LIST1.find("p", class_= "secondary-detail").text
        CONCERTS_MONTH = CONCERT_LIST1.find("h4", class_="month").text
        CONCERTS_DAY = CONCERT_LIST1.find("h3", class_="date").text.strip()

        if CONCERTS_DAY == "1":
            CONCERTS_DAY = (f"{CONCERTS_DAY}st")
        elif CONCERTS_DAY == "2":
                CONCERTS_DAY = (f"{CONCERTS_DAY}nd")
        elif CONCERTS_DAY == "3":
            CONCERTS_DAY = (f"{CONCERTS_DAY}rd")
        else:
            CONCERTS_DAY = (f"{CONCERTS_DAY}th")


            if LOCATION_FILTER != "Q":
                if LOCATION_FILTER in CONCERTS_LOCATION1:
                    MONTH_FILTER = input(">")
                    if MONTH_FILTER in CONCERTS_MONTH:
                        with open(f"Files/{INDEX}.txt", "w") as TextFiles:
                            print(f"The concert will be at {CONCERTS_LOCATION1} on {CONCERTS_MONTH} {CONCERTS_DAY} \n")
                            print(f"Arena : {CONCERTS_ARENA} \n")
                            TextFiles.write(f"The concert will be at {CONCERTS_LOCATION1} on {CONCERTS_MONTH} {CONCERTS_DAY} \n")
                            TextFiles.write(f"Arena : {CONCERTS_ARENA} \n")
                    else :
                        print(f"There no concerts in {LOCATION_FILTER} in {MONTH_FILTER}")
            elif LOCATION_FILTER == "Q" :
                with open (f"Files/{INDEX}.txt", "w") as TextFiles:
                    print(f"The concert will be at {CONCERTS_LOCATION1} on {CONCERTS_MONTH} {CONCERTS_DAY}")
                    print(f"Arena : {CONCERTS_ARENA} \n")
                    TextFiles.write(f"The concert will be at {CONCERTS_LOCATION1} on {CONCERTS_MONTH} {CONCERTS_DAY} \n")
                    TextFiles.write(f"Arena : {CONCERTS_ARENA} \n")

bmth_concert()


