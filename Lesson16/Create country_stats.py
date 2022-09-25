average_heights_and_weights = {
    "Canada": (185, 150),
    "United States": (186, 158),
    "India": (180, 156),
    "Brazil": (181, 149)
}


def get_avg_weight(country):
    return average_heights_and_weights[country][0]


def get_avg_avg_weight():
    total_weight = 0
    for heights_and_weights in average_heights_and_weights.values():
        total_weight += int(heights_and_weights[0])
    average_weight = total_weight // len(average_heights_and_weights.values())
    return average_weight


def add_new_country():
    country_name = input("Please enter the country name: ")
    average_weight = input("Please enter the average weight of the country: ")
    average_height = input("Please enter the average height of the country: ")
    average_heights_and_weights[country_name] = (average_weight, average_height)


def update_country_stats(country):
    new_average_weight = input("Please enter the new average weight of the country: ")
    new_average_height = input("Please enter the new average height of the country")
    average_heights_and_weights[country] = (new_average_weight, new_average_height)


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