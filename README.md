# Airbnb-Finder
Find the Best Option Airbnb in specific Neighborhoods in Boston based on price and safety

        The AirBnb data was collected from their official data source for the total 
        listings in Boston for 2022. The crime data was collected from Analyze Boston 
        which is a resource for numerous Boston Related datasets.
        
        The Airbnb data included a unique ID for every airbnb listingands a URL
        to the specific listing. Information such as price, location (latitude, longitude), 
        accommodation, and neighborhood was also provided and collected. The neighborhood 
        dataset was also provided by airbnb and contained all possible neighborhoods, 
        Airbnb’s could be located in Boston. This information was created into a 
        list. For the crime data, the specific coordinates, type of crime, and unique 
        crime id were included in the dataset and collected. For both datasets, the data 
        was condensed into a list of dictionaries where each dictionary contained a 
        specific row of information with the headers as keys.
    
    
        In order to find Airbnbs in the neighborhood chosen by the user, the program filters 
        through the data using the key for the neighborhood. To find and append 
        crime reports that fell within the ranges of the neighborhood chosen, the 
        lowest and highest longitude and latitude values for Airbnb in the neighborhood
        was set as the filter for coordinates of crime reports that fell within these 
        boundaries.
        
        To find the safest Airbnb, the program uses the distance formula 
        (d = [x^2 − x^1]^2 + [y^2 − y^1]^2) to find the distances between each 
        Airbnb and every crime report in that neighborhood. The formula is 
        also used to measure the closest crime report distance for each Airbnb, and the 
        Airbnb with the furthest "closest crime report distance" would be considered the 
        safest Airbnb.
        
        To find the cheapest Airbnb, the program filtered through the Airbnbs in the chosen 
        neighborhood using the key for price. The Airbnb with the lowest value 
        for the price key would be considered the cheapest Airbnb.
        
