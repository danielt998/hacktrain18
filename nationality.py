f = open("2018 Hacktrain - Jul-Oct18 Exit Check Data_2018.11.07.csv")
date = "2018-07-13"

exit_file = open("2018 Hacktrain - Jul-Oct18 Exit Check Data_2018.11.07.csv")
exit_date = "2018-07-13"

eu_nations = ['ALB','AND','ARM','AUT','AZE','BLR','BEL','BIH','BGR','HRV','CYP','CZE','DNK','EST','FIN','FRA','GEO','DEU','GRC','HUN','ISL','IRL','ITA','KAZ','LVA','LIE','LTU','LUX','MKD','MLT','MDA','MCO','MNE','NLD','NOR','POL','PRT','ROU','RUS','SMR','SRB','SVK','SVN','ESP','SWE','CHE','TUR','UKR','GBR']
eu_count = 0
non_eu_count = 0

exit_sums = [[0 for i in range(4)] for j in range(24)]

exit_lines_to_keep = []

for line in exit_file:
    segments = line.split(" ")
    if segments[0] == exit_date:
        exit_lines_to_keep.append(segments)

for segments in exit_lines_to_keep:
    time_segments = segments[1].split(":")
    nationality = time_segments[2][2:6]
    quarter = int(int(time_segments[1])/15)
    exit_sums[int(time_segments[0])][quarter] += 1

    if nationality in eu_nations:
        print(nationality)
        eu_count += 1
    else:
        non_eu_count += 1

print(eu_count)
print(non_eu_count)
