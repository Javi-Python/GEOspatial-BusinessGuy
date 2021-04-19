# GEOspatial-BusinessGuy

#### What's the best place to start a business?

This project looked to answer this question by using a mongo database of companies worldwide, and attempting to find the city that fit some specific criteria to the max. I used the information given to me in the Mongo database as well as extracted information from the 4square API.


# Requierements
1. Pandas
2. JSON
3. Requests
4. Pymongo 
5. Dotenv
6. OS
7. api_calls

# File Glossary:
## - Geo-Project:
    - Where we create queries in the mongo database and figure out cities and locations to research
## - API Calls with Functions:
    - Where we do calls to the 4square API, and arrange the data into workable frames.
## - Finding Out What Is Near:
    - We count how many venues that we are interested are within 3km of our identified possible offices.
## - api_calls.py:
    -contains the files with the functions that I used

# To Do's:

I didnt have enough time to really expand on the final part, when I have time I hope to rank the different office spaces in Sanfrancisco by the actual proximity to each venue as well as the importance of such venue. Hope you enjoy it.


