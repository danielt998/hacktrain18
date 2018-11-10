exit_file = open("/home/dtm/Desktop/Baggage Challenge/Check in data (July 2018-October 2018)/2018 Hacktrain - Jul-Oct18 Check in Data_2018.11.07.csv", "r")

CHECK_IN_TIME_COL = 3
DATE="13/07/2018"

exit_lines_to_keep = []
check_in_sums = [[0 for i in range(4)] for j in range(24)]

def get_segment(minute):
    return int(minute / 15)

for line in exit_file:
    cols = line.split(",")
    if cols[3].split(" ")[0] == DATE:
        exit_lines_to_keep.append(cols)

for line in exit_lines_to_keep:
    time = line[3].split(" ")[1]
    time_segments = time.split(":")
    hours = int(time_segments[0])
    mins = int(time_segments[1])
    check_in_sums[hours][get_segment(mins)] += 1

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

for i in range(0,23):
    for j in range(0,3):
        difference[i][j] = check_in_sums[i][j] - exit_sums[i][j]

for sum in difference:
    print(str(sum[0]) + ":" + str(sum[1]) + ":" + str(sum[2]) + ":" + str(sum[3]))
