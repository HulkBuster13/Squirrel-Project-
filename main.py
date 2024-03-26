import csv

import pandas

        # Reading the file "2018_Central_Park_Squirrel_Census_-_Squirrel_Data (1).csv"

sd = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data (1).csv")

        # How you did it

#colors_to_list = sd["Primary Fur Color"].to_list()

        # Using a dictionary with key/value pairs

#squirrel_df = {
#   "colors": {"Gray": 0, "Cinnamon": 0, "Black": 0},
#}

#created_squirrel_df = pandas.DataFrame(squirrel_df)

# for i in colors_to_list:
#     if i == "Gray":
#         created_squirrel_df.colors.Gray += 1
#     if i == "Cinnamon":
#         created_squirrel_df.colors.Cinnamon += 1
#     else:
#         created_squirrel_df.colors.Black += 1

#created_squirrel_df.to_csv("Squirrel Color Counts.csv")





        # How the instructor did it

grey = len(sd[sd["Primary Fur Color"] == "Gray"])
cinnamon = len(sd[sd["Primary Fur Color"] == "Cinnamon"])
black = len(sd[sd["Primary Fur Color"] == "Black"])

new_squirrel_df = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey, cinnamon, black]
}

more_squirrel_df = pandas.DataFrame(new_squirrel_df)
more_squirrel_df.to_csv("Instructor way squirrel color counts.csv")





