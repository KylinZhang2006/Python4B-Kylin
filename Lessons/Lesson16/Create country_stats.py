average_heights_and_weights = {
    "Canada": (185, 150),
    "United States": (186, 158),
    "India": (180, 156),
    "Brazil": (181, 149)
}


def get_avg_weight(country):
    if country in average_heights_and_weights:
        return average_heights_and_weights[country][1]
    else:
        print("The country is not in our dictionary!")


def get_avg_avg_weight():
    total_weight = 0
    for heights_and_weights in average_heights_and_weights.values():
        total_weight += heights_and_weights[1]
    if len(average_heights_and_weights) != 0:
        return total_weight / len(average_heights_and_weights)
    return 0


def add_new_country():
    country_name = input("Please enter the country name: ")
    if country_name in average_heights_and_weights:
        print("The country is already in the dictionary!")
        return
    average_height = input("Please enter the average height of the country: ")
    average_weight = input("Please enter the average weight of the country: ")
    if average_height.isdecimal() and average_weight.isdecimal():
        average_heights_and_weights[country_name] = (int(average_height), int(average_weight))
    else:
        print("Invalid input!")


def update_country_stats(country):
    if country in average_heights_and_weights:
        new_average_height = input("Please enter the new average height of the country: ")
        new_average_weight = input("Please enter the new average weight of the country: ")
        if average_height.isdecimal() and average_weight.isdecimal():
            average_heights_and_weights[country] = (int(new_average_height), int(new_average_weight))
        else:
            print("Invalid input!")
    else:
        print("The country is not in the dictionary!")


print("Average weight of all countries: ")
print(get_avg_avg_weight())

print("Average weight of Canada: ")
print(get_avg_weight("Canada"))

add_new_country()

print("Average weight of all countries: ")
print(get_avg_avg_weight())

update_country_stats("United States")

print("New average weight of United States: ")
print(get_avg_weight("United States"))
