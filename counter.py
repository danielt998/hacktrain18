f = open("/home/dtm/Desktop/Baggage Challenge/Check in data (July 2018-October 2018)/2018 Hacktrain - Jul-Oct18 Check in Data_2018.11.07.csv", "r")

CHECK_IN_TIME_COL = 3
DATE="13/07/2018"

lines_to_keep = []
check_in_sums = [[0 for i in range(4)] for j in range(24)]

def get_segment(minute):
    return int(minute / 15)

for line in f:
    cols = line.split(",")
    if cols[3].split(" ")[0] == DATE:
        lines_to_keep.append(cols)

for line in lines_to_keep:
    time = line[3].split(" ")[1]
    time_segments = time.split(":")
    hours = int(time_segments[0])
    mins = int(time_segments[1])
    check_in_sums[hours][get_segment(mins)] += 1

for segs in check_in_sums:
    print(str(segs[0]) + ":" + str(segs[1]) + ":" + str(segs[2]) + ":" + str(segs[3]))
