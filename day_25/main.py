# data = []
# with open("weather_data.csv") as file:
#     lines = file.readlines()
#     for line in lines:
#         s = line.strip()
#         data.append(s)
#         print(data)
#         data = []
# print("\n\n\n")
import csv
with open("weather_data.csv") as file:
    temp = []
    data = csv.reader(file)
    print(data)
    for row in data:
       if row[1] != "temp":
        temp.append(int(row))
    print(temp)

# import pandas
#
# # data = pandas.read_csv("weather_data.csv")
# # # data_dic = data.to_dict()
# # # temp_list = data['temp'].tolist()
# # # print(data['temp'].max())
# # #print(data[data.day == "Friday"])
# #
# # monday = data[data.day == "Monday"]
# # print(monday.temp[0])
#
# data_dic = {
#     "students":["amy", "james", "ravi"],
#     "scores": [100, 90, 80]
# }
# data = pandas.DataFrame(data_dic)
# data.to_csv("new_dic.csv")