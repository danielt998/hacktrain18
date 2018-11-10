f = open("2018 Hacktrain - Jul-Oct18 Exit Check Data_2018.11.07.csv")
date = "2018-07-13"

exit_sums = [[0 for i in range(4)] for j in range(24)]

lines_to_keep = []

for line in f:
    segments = line.split(" ")
    if segments[0] == date:
        lines_to_keep.append(segments)

for segments in lines_to_keep:
    time_segments = segments[1].split(":")
    nationality = time_segments[2][2:4]
    quarter = int(int(time_segments[1])/15)
    exit_sums[int(time_segments[0])][quarter] += 1

for sum in exit_sums:
    print(str(sum[0]) + ":" + str(sum[1]) + ":" + str(sum[2]) + ":" + str(sum[3]))
