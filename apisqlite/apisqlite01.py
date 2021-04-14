#!/usr/bin/env python3
""" Author: RZFeeser || Alta3 Research
Gather data returned by various APIs published on OMDB, and cache in a local SQLite DB
"""

import json
import sqlite3
import requests

# Define the base URL
OMDBURL = "http://www.omdbapi.com/?"

# search for all movies containing string
def movielookup(mykey, searchstring):
    try:
        ## open URL to return 200 response
        resp = requests.get(f"{OMDBURL}apikey={mykey}&s={searchstring}")
        ## read the file-like object decode JSON to Python data structure
        return resp.json()
    except:
        return False

def trackmeplease(datatotrack):
    conn = sqlite3.connect('mymovie.db')
    try:
        conn.execute('''CREATE TABLE IF NOT EXISTS MOVIES (TITLE TEXT PRIMARY KEY NOT NULL, YEAR INT  NOT NULL);''')

        # loop through the list of movies that was passed in
        for data in datatotrack:
            # in the line below, the ? are examples of "bind vars"
            # this is best practice, and prevents sql injection attacks
            # never ever use f-strings or concatenate (+) to build your executions
            conn.execute("INSERT INTO MOVIES (TITLE,YEAR) VALUES (?,?)",(data.get("Title"), data.get("Year")))
            conn.commit()

        print("Database operation done")
        conn.close()
        return True
    except:
        return False

# Read in API key for OMDB
def harvestkey():
    with open("/home/student/pyapi/apisqlite/omdb.key") as apikeyfile:
        return apikeyfile.read().rstrip("\n") # grab the api key out of omdb.key

def printlocaldb():
    pass
    #cursor = conn.execute("SELECT * from MOVIES")
    #for row in cursor:
    #    print("MOVIE = ", row[0])
    #    print("YEAR = ", row[1])


def main():

    print("Particulating Splines...")

    # read the API key out of a file in the home directory
    mykey = harvestkey()

    # initialize answer
    answer = "go"

    while True:
        answer = ""
        while answer == "":
            print("""\n**** Welcome to the OMDB Movie Client and DB ****
            ** Returned data will be written into the local database **
            1) Search for All Movies Containing String
            2) Search Movie by Type
            3) Search by Year of release
            4) Search by Type and Year of release
            5) See all LOCAL database
            99) Exit""")

            answer = input("> ")

        if answer == "1":
            searchstring = input("Search all movies in the OMDB. Enter search string: ")
            resp = movielookup(mykey, searchstring)["Search"]
            if resp:
                # display the results
                print(resp)
                # write the results into the database
                trackmeplease(resp)
            else:
                print("That search did not return any results.")

        elif answer == "2":
            print("Entered option 2!")
            print("Sorry under construction. See you soon!")
            break

        elif answer == "3":
            print("Entered option 3!")
            print("Sorry under construction. See you soon!")
            break

        elif answer == "4":
            print("Entered option 4!")
            print("Sorry under construction. See you soon!")
            break

        elif answer == "5": 
            print("Entered option 5!")
            print("Sorry under construction. See you soon!")
            break

        elif answer == "99":
            print("See you next time!")
            break

if __name__ == "__main__":
    main()

