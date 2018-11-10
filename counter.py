entry_file = open("/home/dtm/Desktop/Baggage Challenge/Check in data (July 2018-October 2018)/2018 Hacktrain - Jul-Oct18 Check in Data_2018.11.07.csv", "r")

CHECK_IN_TIME_COL = 3
DATE = "13/07/2018"

entry_lines_to_keep = []
check_in_sums = [[0 for i in range(4)] for j in range(24)]

def get_segment(minute):
    return int(minute / 15)

# count = 0
for line in entry_file:
    # if count < 4:
    #     count++
    #     continue
    cols = line.split(",")
    if cols[3].split(" ")[0] == DATE:
        entry_lines_to_keep.append(cols)

for line in entry_lines_to_keep:
    time = line[3].split(" ")[1]
    time_segments = time.split(":")
    hours = int(time_segments[0])
    mins = int(time_segments[1])
    check_in_sums[hours][get_segment(mins)] += 1

###########################################group data

# for curr_hour in range(0,24):
#     for curr_quarter in range(0, 4):
#  #        for segments in entry_lines_to_keep:
#
#         pnrs = {}
#         for line in entry_lines_to_keep:
#             time_segments = line[1].split(" ")[1].split(":")
#             # nationality = ''.join(time_segments[2][2:6].split())
#             quarter = int(int(time_segments[1])/15)
#             # exit_sums[int(time_segments[0])][quarter] += 1
#
#             if int(time_segments[0]) == curr_hour and quarter == curr_quarter:
#                 pnr = line[10]
#                 if pnrs.get(pnr) != None:
#                     pnrs[pnr] = pnrs[pnr] + 1
#                 else:
#                     pnrs[pnr] = 1
#
#     #for pnr, count in pnrs.items():
#     #    if count != 1:
#     #        print(str(pnr) + "," + str(count))
#
#         group_numbers = [0] * 100000 #number of groups of each size
#         for pnr, count in pnrs.items():
#             group_numbers[count] += 1
#
#         for index, count in enumerate(group_numbers):
#             if count != 0:
#                 #print(str(curr_hour) + ":" + str(curr_quarter * 15) + ", index:" + str(index) + ":" + str(count))
#                 print(", index:" + str(index) + ":" + str(count))
#         print("------------------------------------")
###################

exit_file = open("2018 Hacktrain - Jul-Oct18 Exit Check Data_2018.11.07.csv")
exit_date = "2018-07-13"

exit_sums = [[0 for i in range(4)] for j in range(24)]

exit_lines_to_keep = []

for line in exit_file:
    segments = line.split(" ")
    if segments[0] == exit_date:
        exit_lines_to_keep.append(segments)

for segments in exit_lines_to_keep:
    time_segments = segments[1].split(":")
    nationality = time_segments[2][2:4]
    quarter = int(int(time_segments[1])/15)
    exit_sums[int(time_segments[0])][quarter] += 1

difference = [[0 for i in range(4)] for j in range(24)]

for i in range(0,24):
    for j in range(0,4):
        difference[i][j] = check_in_sums[i][j] - exit_sums[i][j]


#add extra stuff
from nationality import getNationalities
nationalities = getNationalities()


total = 0
for hour, sum in enumerate(difference):
    for i in range(0,4):
        total = total + (difference[hour][i])
        print(str(hour) + ":" + str(i * 15) + "," + str(difference[hour][i]) + "," + nationalities[(hour * 4) + i])

print(total)
