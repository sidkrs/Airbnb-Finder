#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: airbnb_analysis.py

Report:
    1. Problem Statement and Background
        In a city like Boston, where there are a mass multitude of AirBNB options, 
        as well as a mass multitude of crime reports, it can be difficult to find 
        the safest places to stay. We believe that our program provides value because 
        from the perspective of AirBNB, it can allow them to better serve their 
        consumer base and allow people to find locations that truly match their 
        preferences. Additionally, for those investing in property or looking to 
        list their property as an AirBNB, our project could allow them to better 
        compare their property to those in their specific area. Ultimately, our program
        allows a user to better evaluate their Airbnb options in the city of Boston 
        based on the factors of cost and safeness.
    
    2. Introduction and Description of Data
        The AirBnb data was collected from their official data source for the total 
        listings in Boston for 2022. The crime data was collected from Analyze Boston 
        which is a resource for numerous Boston Related datasets. When entering the data 
        into Spyder, the standard delimiter “,” was an issue as it conflicted with 
        commas used within the data. Thus, a program was run that converted the 
        delimiters from “,” to “}”. This delimiter was used for both the crime and 
        Airbnb data. 
        
        The Airbnb data included a unique ID for every airbnb listing as well as a URL
        to the specific listing. Information such as price, location (latitude, longitude), 
        accommodation, and neighborhood were also provided and collected. The neighborhood 
        dataset was also provided by airbnb and contained all possible neighborhoods, 
        Airbnb’s could be located in Boston. This information was created into a 
        list. For the crime data, the specific coordinates, type of crime, unique 
        crime id were included in the dataset and collected. For both datasets, the data 
        was condensed into a list of dictionaries where each dictionary contained a 
        specific row of information with the headers as keys. We then utilized these 
        lists for our reports and visualizations.
    
    3. Methods
        In order to find Airbnbs in the neighborhood chosen by the user, we filtered 
        through the data using the key for the neighborhood. To find and append 
        crime reports that fell within the ranges of the neighborhood chosen, we 
        used the lowest and highest longitude and latitude values for Airbnb. We 
        used these values to ensure that we only appended coordinates of crime reports 
        that fell within these boundaries.
        
        To find the safest Airbnb, we had to utilize the distance formula 
        (d = [x^2 − x^1]^2 + [y^2 − y^1]^2) in order to find the distances between each 
        Airbnb and every crime report in that neighborhood. We also found the closest 
        crime report distance for each Airbnb, and the Airbnb with the furthest 
        closest crime report distance would be considered the safest Airbnb.
        
        To find the cheapest Airbnb, we filtered through the Airbnbs in the chosen 
        neighborhood using the key for price. The Airbnb with the lowest value 
        for the price key would be considered the cheapest Airbnb.
        
        We first ran a for loop going through all locations in the neighborhood data 
        set, if the location and the accommodation parameters were set, then a list 
        would be created for all potential Airbnbs for that location. The average 
        price was then taken and then added to a dictionary with the key being the 
        location. After a dictionary was created, the min value, max value, and 
        closest price to the neighborhood choice were then retrieved in a report. 
    
    4. Results, Conclusion, and Future Work
        User Input: The user first inputs which Neighborhood they would like to 
        view Airbnb’s from including the max price they are willing to pay and 
        how many people they want to accommodate. In our example, we chose to select
        Roxbury, 4 people, and a maximum price of $1000.
        
        Report #1: The first report takes into account your accommodation requirements 
        and neighborhood preference and details the cheapest option and safest option 
        while providing a URL to the Airbnbs themselves. It also provides the 
        per-night cost of the cheapest option in the selected neighborhood. The 
        report also details the cheapest, most expensive, and most similar 
        neighborhood to the one you selected based on your accommodation 
        requirements. In our example, the url of the cheapest option is "https://www.airbnb.com/rooms/21597670",
        the cheapest option costed $65, the url of the safest option is "https://www.airbnb.com/rooms/5088560",
        the average price in Roxbury was $207.95, Allston was the most similar location with 
        an average price of $212.93, South Boston Waterfron was the most expensive
        with an average price of $486, and Hyde Park was the cheapest with an average
        price of $127.57.
        
        Visualization #1: This graph details the specific location of all the 
        Airbnb’s that fit your preference including all crime reported in that 
        area. The graph also highlights the cheapest option based on price and 
        safest option relative to the distance from the crime reports. In our 
        example, the safest option is located at around (42.319, -71.025), and 
        the most expensive option is located at around (42.340, -71.084).
        
        Visualization #2:   The second graph is a bar chart that depicts the average 
        price of all neighborhoods based on the accommodation requirement set by the user.
        In our example, the graph displays all the average prices in Boston 
        for Airbnbs that accommodate 4 people.
        
        Strengths:
            1. Able to Identify Cheapest and Safest Option
               One of the largest strengths of our program is that it allows the 
               user to view the location and access and link to both the cheapest 
               and safest Airbnb options based on their preferences. This would allow 
               someone to better understand their Airbnb options when in Boston.
            2. Able to Visualize Proximity to Crime
               Another strength of our program is that it allows a user to view how 
               close their Airbnb options are to crime reports throughout Boston. 
               This would allow someone to better access the safeness of their 
               Airbnb options. 
            3. Able to View Useful Data on Other Options
               A final strength of our program is that it allows the user to learn 
               the average price of their options in their chosen neighborhood, 
               as well as information on the cheapest and most expensive neighborhood 
               based on their accommodation preferences.
                
        Weaknesses:
            1. Unable to Factor Degree of Crime
               One of the weaknesses of our program is that it does not factor 
               how serious a crime report may be. Our data on crime reports ranged 
               from noise complaints to shootings, so the severity of a crime 
               would definitely be useful for a user to know. Therefore, certain 
               times of crime would be much more alarming or notable, and the user 
               currently would not be able to factor that into their Airbnb decision. 
            2. Unable to easily access all options
                Another weakness of our program is that the user does not have the 
                ability to easily access all of the Airbnb options within their 
                selected neighborhood. Since the scatterplot map with Airbnbs does 
                not have labels or a hyperlink to access, the only identifiable means 
                for each Airbnb is their coordinates (unless cheapest or safest option). 
                When comparing all of your options for an Airbnb, it would be useful 
                to be able to easily access each option in the area.

        
        
"""
# imports necessary functions
import matplotlib.pyplot as plt
from numpy import mean
import math


def user_choice(location):
    """ Save the choices the user makes on Airbnb preference
    location - List of all possible locations.

    Return: the choices the user made
    """
    # Display possible locations to pick from
    for i in location:
        print(i)
    # Save user choices
    location = input("\nFrom which neighborhood listed above are you looking for an Airbnb? \n").title()
    accommodate = int(input("How many people are you looking to accommodate? \n"))
    max_price = float(input("What is the maximum price you are willing to pay? (per night) \n$"))
    return location, accommodate, max_price


def read_airbnb(filename, delimiter=','):
    """ Read a csv file to a list of dictionaries
    filename - the name of the file.  File must have a header.
    delimiter - field delimiter (Default: ',')

    Return: a table of data as a list of dictionaries
    """

    # creates list for airbnb dictionaries
    data = []
    with open(filename, 'r') as infile:
        # Read the header
        header = infile.readline().strip().split(delimiter)
        # Read remaining lines
        for line in infile:
            rowdict = {}
            # parse values
            vals = line.strip().split(delimiter)
            # Store key value pairs
            for i in range(len(vals)):
                key = header[i]
                value = vals[i]
                if value.isnumeric():
                    value = int(value)
                else:
                    value = value
                rowdict[key] = value

            data.append(rowdict)  # add row to data
    return data


def read_crime(filename, delimiter=','):
    """ Read a csv file to a list of dictionaries
    filename - the name of the file.  File must have a header.
    delimiter - field delimiter (Default: ',')
    Return: a table of data as a list of dictionaries
    """
    # creates list for crime dictionaries
    data = []
    with open(filename, 'r') as infile:
        # Read the header
        header = infile.readline().strip().split(delimiter)
        # Read remaining lines
        for line in infile:
            rowdict = {}
            # parse values
            vals = line.strip().split(delimiter)
            # Store key value pairs
            for i in range(len(vals)):
                key = header[i]
                value = vals[i]
                if value.isnumeric():
                    value = int(value)
                else:
                    value = value
                rowdict[key] = value
            data.append(rowdict)  # add row to data
    return data


def clean_data(airbnb, crimes):
    """ Convert numbers into floats for the airbnb and crime dataset 
    airbnb - airbnb dataset. 
    crime - crime dataset. 
    Return: Both datasets with value types correctly assigned """

    # Clean all numerals and convert them into floats crime and airbnb data set
    for i in airbnb:
        i['longitude'] = float(i['longitude'])
        i['latitude'] = float(i['latitude'])
        # Remove dollar sign and remove commas for numbers such as $1,000
        i['price'] = i['price'].lstrip('$')
        i['price'] = float((i['price'].replace(',', '')))
    for i in crimes:
        i['Lat'] = float(i['Lat'])
        i['Long'] = float(i['Long'])
    return airbnb, crimes


def neighborhoods(filename):
    """ Read lines of csv file 
    filename - the name of the file
    Return: data as list of lists
    """
    # creates list for neighborhoods
    data = []
    with open(filename, 'r') as infile:
        # read lines in file
        for line in infile:
            # parse values
            data.append(line.strip())
    return data


def user_pref(user, airbnb):
    """ Creates list for Airbnb preferences
	Parameters: user, airbnb
	Return: pref_airbnb
    """
    # creates list for airbnb preferences
    pref_airbnb = []
    for i in airbnb:
        # checks if airbnb matches user preferences
        if i['neighbourhood_cleansed'] == user[0] and (i['accommodates'] == user[1]) and (i['price'] <= user[2]):
            pref_airbnb.append(i)  # appends values to list
    return pref_airbnb


def crime_analysis(select_airbnb, crimes):
    """Creates list for crime data
       Parameters: select_airbnb, crimes
       Return: crimes_refined (list)
    """

    # creates and assigns initial values for variables of minimum and maximum longitude and latitude values
    min_long = 100
    max_long = -100
    min_lat = 100
    max_lat = -100

    # creates list for crime data for chosen neighborhood
    crimes_refined = []

    # iterates through airbnb data 
    for i in select_airbnb:
        # checks if longitude is current smallest or largest value
        if i['longitude'] < min_long:
            min_long = i['longitude']  # assigns new min_long value if smallest
        elif i['longitude'] > max_long:
            max_long = i['longitude']  # assigns new max_long value is largest

        # checks if latitude is current smallest or largest value
        if i['latitude'] < min_lat:
            min_lat = i['latitude']  # assigns new min_lat value if smallest
        elif i['latitude'] > max_lat:
            max_lat = i['latitude']  # assigns new max_lat value if largest

    # iterates through each crime report in crime data
    for i in crimes:
        # checks if coordinates of crime report fall within boundaries of minimum and maximum longitude and latitude 
        # +/- 0.005 creates buffer for crimes in proximity of airbnbs
        if i['Lat'] >= (min_lat - 0.005) and i['Lat'] <= (max_lat + 0.005) and \
                i['Long'] >= (min_long - 0.005) and i['Long'] <= (max_long + 0.005):
            crimes_refined.append(i)  # appends crime report to crimes_refined if coordinates fall within boundaries

    return crimes_refined


def lowest_cost(select_airbnb):
    """ Returns the location, url, and price of cheapest airbnb
       Parameters: select_airbnb
       Return: lowest_url, lowest_lat, lowest_long, lowest_cost"""
    # sets initial value for lowest cost 
    lowest_cost = 10000

    # iterates through option in select_airbnb
    for i in select_airbnb:
        # checks if price for airbnb is less than lowest_cost
        if i['price'] < lowest_cost:
            # creates variable and assigns value for lowest url, cost, longitude, and latitude
            lowest_url = i['listing_url']
            lowest_cost = i['price']
            lowest_long = i['longitude']
            lowest_lat = i['latitude']

    return lowest_url, lowest_lat, lowest_long, lowest_cost


def safest_airbnb(select_airbnb, crimes_refined):
    """ Returns the position and url of the safest airbnb
       Parameters: select_airbnb, crimes_refined
       Return: farthest_url, farthest_lat, farthest_long"""
    # creates list for closest distance to crime report for each airbnb
    closest_list = []

    # iterates through each airbnb in select_airbnb
    for airbnb in select_airbnb:
        # assigns initial value for distance and closest distance value 
        distance = 0
        closest = 100000

        # creates variables for longitude and latitude values for airbnb
        airbnb_long = airbnb['longitude']
        airbnb_lat = airbnb['latitude']

        # iterates through crime report in crimes_refined
        for crime in crimes_refined:
            # creates variables for longitude and latitude values for crime report
            crime_long = crime['Long']
            crime_lat = crime['Lat']

            # uses distance formula to calculate distance between crime report and airbnb
            distance = math.sqrt((crime_long - airbnb_long) ** 2 + (crime_lat - airbnb_lat) ** 2)

            # checks if distance is less than current closest distance value
            if distance < closest:
                closest = distance  # assigns new closest value if fulfilled

        # appends closest value to list 
        closest_list.append(closest)

    # finds index for largest value in closest_list 
    farthest_index = closest_list.index(max(closest_list))

    # creates variables and assigns value for farthest longitude, latitude, and airbnb url
    farthest_long = select_airbnb[farthest_index]['longitude']
    farthest_lat = select_airbnb[farthest_index]['latitude']
    farthest_url = select_airbnb[farthest_index]['listing_url']

    return farthest_url, farthest_lat, farthest_long


def visualize_map(select_airbnb, crimes_refined, cheapest_option, safest_option):
    """ Grapgs the coordinates of the airbnbs and crime in the area
       Parameters: select_airbnb, crimes_refined, cheapest_option, safest_option
       Return: none"""
    # creates variable for neighborhood of airbnbs
    location = select_airbnb[0]['neighbourhood_cleansed']

    # creates list for airbnb longitude and latitude values
    airbnb_long = []
    airbnb_lat = []

    # creates lists for crime report longitude and latitude values
    crimes_long = []
    crimes_lat = []

    # iterates through option in select_airbnb
    for i in select_airbnb:
        # appends longitude and latitude values to respective lists
        airbnb_long.append(i['longitude'])
        airbnb_lat.append(i['latitude'])

    # iterates through crime in crimes_refined
    for i in crimes_refined:
        # appends longitude and latitude values to respective lists
        crimes_long.append(i['Long'])
        crimes_lat.append(i['Lat'])
    
    plt.figure(dpi=700)
    # creates scatter plot for crime reports
    plt.scatter(crimes_lat, crimes_long, marker=".", s=10, color="RED", alpha=0.1,
                label="Crime Reports")

    # creates scatter plot for airbnb locations 
    plt.scatter(airbnb_lat, airbnb_long, marker="*", s=75, color="GREEN",
                label="AirBNB Options")

    # plots coordinate for cheapest airbnb option
    plt.scatter(cheapest_option[1], cheapest_option[2], marker="*", s=150,
                color="PURPLE", label="Cheapest Option")

    # plots coordinate for safest airbnb option
    plt.scatter(safest_option[1], safest_option[2], marker="*", s=150,
                color="BLUE", label="Safest Option")

    # assigns title, xlabel, ylabel to graph, limits to x and y axis, and creates legend, saves figure, and displays figure
    plt.title(f"Map of AirBNB Options & Local Crime Reports in {location}", fontweight="bold")
    plt.xlabel("Latitude")
    plt.ylabel("Longitude")
    plt.xlim((min(airbnb_lat) - 0.005), (max(airbnb_lat) + 0.005))
    plt.ylim((min(airbnb_long) - 0.005), (max(airbnb_long) + 0.005))
    plt.legend()
    plt.savefig('AirBNB_Crime_Map.png', bbox_inches='tight')
    plt.show()

    # prints report with the cheapest option url, price, and safest option url in chosen neighborhood
    print(f"\nIn {location}:")
    print(f"Cheapest Option URL: {cheapest_option[0]}")
    print(f"The cheapest option costs ${cheapest_option[3]}\n")
    print(f"Safest Option URL: {safest_option[0]}\n")


def alternative(airbnb, locations, user):
    """ Provides alternative neighborhood options from the choice selected based on price
       Parameters: airbnb, locations, user
       Return: location_prices"""
    location_price = {}
    user_location = user[0]
    # Cycle through each possible location
    for place in locations:
        place_prices = []
        # Match the airbnb with the location and accomodation requirement
        for listing in airbnb:
            if listing['neighbourhood_cleansed'] == place and listing['accommodates'] == user[1]:
                # Append price to list of prices
                place_prices.append(listing['price'])
        # Take the average of the prices and make a key value pair in a dictionary for each location
        location_price[place] = mean(place_prices)

    # Assign a unique value to the user's location and remove it from the list
    value = location_price[user_location]
    location_prices = location_price
    del location_price[user_location]
    # Calculate most similar value compared to the users choice
    res_key, res_val = min(location_price.items(), key=lambda x: abs(value - x[1]))

    # Print report    
    print(f"To accommodate {user[1]} people:")
    print(f"{user[0]} had an average price of ${round(value, 2)}")
    print(f"The most similar location is {res_key} with an average price of ${round(res_val, 2)}")
    # Get the highest and loweest price from the dictionary
    high = max(location_price.values())
    high_location = max(location_price, key=location_price.get)
    low = min(location_price.values())
    low_location = min(location_price, key=location_price.get)
    print(f"{high_location} is the most expensive at ${round(high, 2)}")
    print(f"{low_location} is the cheapest at ${round(low, 2)}")

    return location_prices


def visualize_prices(prices, user):
    """ Grapgs the average prices of a specified accomodation per neighborhood
       Parameters: prices, user
       Return: none"""
    # Label the graph
    plt.figure(dpi=700)
    plt.xlabel('Neighborhoods')
    plt.ylabel('Average Price')
    plt.title(f'Average Prices to Accommodate {user[1]} People', fontweight="bold")
    # Plot the range of values in the prices list and the values for the height
    plt.bar(x=range(len(prices)), height=list(prices.values()), tick_label=list(prices.keys()))
    # Rotate the x label 90 degrees
    plt.xticks(rotation=90)
    plt.show(block=True)


def main():
    airbnb_list = read_airbnb("airbnb_list.csv", delimiter='}')
    crime_data = read_crime("crime.csv", delimiter='}')

    locations = neighborhoods("neighbourhoods.csv")

    dataset = clean_data(airbnb_list, crime_data)
    airbnb = dataset[0]
    crimes = dataset[1]

    user_choices = user_choice(locations)
    select_airbnb = user_pref(user_choices, airbnb)

    crimes_refined = crime_analysis(select_airbnb, crimes)
    cheapest_option = lowest_cost(select_airbnb)
    safest_option = safest_airbnb(select_airbnb, crimes_refined)
    visualize_map(select_airbnb, crimes_refined, cheapest_option, safest_option)

    price_at_locations = alternative(airbnb, locations, user_choices)
    visualize_prices(price_at_locations, user_choices)


if __name__ == '__main__':
    main()
