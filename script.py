destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'Sao Paulo, Brazil', 'Cairo, Egypt']



def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

attractions = {}


def add_attraction(attractions, key, value):
    if key in attractions:
        # Key exist in dict.
        # Check if type of valuee of key is list or not
        if not isinstance(attractions[key], list):
            # If type is not list, then make it list
            attractions[key] = [attractions[key]]
        # Append the value in list
        attractions[key].append(value)
    else:
        # As key is not in dict,
        # so, add key-value pair
        attractions[key] = [value]

add_attraction(attractions, "Los Angeles, USA", ['Venice Beach',['beach']])
add_attraction(attractions, "Paris, France", ["The Louvre", ["art", "museum"]])
add_attraction(attractions, "Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction(attractions, "Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction(attractions, "Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction(attractions, "Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction(attractions, "Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction(attractions, "Los Angeles, USA", ["test", ["test", "museum"]])
add_attraction(attractions, "Sao Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction(attractions, "Sao Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction(attractions, "Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction(attractions, "Cairo, Egypt", ["Egyptian Museum", ["museum"]])

print(attractions)
def find_acttractions(destination, interests):
    attractions_with_interests = []
    attraction_in_city = attractions.get(destination)

    for i in range(len(attraction_in_city)):
        for j in range(len(attraction_in_city[i])):
            if interests in attraction_in_city[i][j]:
                attractions_with_interests.append(attraction_in_city[i])
                place = attractions_with_interests[0]
                place = place [0]
    return place


    #return attractions_with_interests

print(find_acttractions('Cairo, Egypt', 'museum'))

test_traveler = ['Mirjam Böhm', 'Los Angeles, USA', 'art']

def get_attractions_for_traveler(traveler):
    traveler_name = traveler[0]
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    places_to_go = find_acttractions(traveler_destination,traveler_interests)
    print("Hi " + str(traveler_name) + ", we think you´ll like these places around " + str(traveler_destination) + ": " + str(places_to_go))

get_attractions_for_traveler(test_traveler)