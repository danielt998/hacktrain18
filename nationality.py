def getNationalities():
    f = open("2018 Hacktrain - Jul-Oct18 Exit Check Data_2018.11.07.csv")
    date = "01/08/2018"

    exit_file = open("2018 Hacktrain - Jul-Oct18 Exit Check Data_2018.11.07.csv")
    exit_date = "2018-08-01"

    eu_nations = ['ALB','AND','ARM','AUT','AZE','BLR','BEL','BIH','BGR','HRV','CYP','CZE','DNK','EST','FIN','FRA','GEO','DEU','GRC','HUN','ISL','IRL','ITA','KAZ','LVA','LIE','LTU','LUX','MKD','MLT','MDA','MCO','MNE','NLD','NOR','POL','PRT','ROU','RUS','SMR','SRB','SVK','SVN','ESP','SWE','CHE','TUR','UKR','GBR']

    return_vals = []

    exit_sums = [[0 for i in range(4)] for j in range(24)]

    exit_lines_to_keep = []
    for line in exit_file:
        segments = line.split(" ")
        if segments[0] == exit_date:
            exit_lines_to_keep.append(segments)

    for curr_hour in range(0,24):
        for curr_quarter in range(0, 4):
            eu_count = 0
            non_eu_count = 0
            for segments in exit_lines_to_keep:
                time_segments = segments[1].split(":")
                nationality = ''.join(time_segments[2][2:6].split())
                quarter = int(int(time_segments[1])/15)
                exit_sums[int(time_segments[0])][quarter] += 1

                if int(time_segments[0]) == curr_hour and quarter == curr_quarter:
                    if nationality in eu_nations :
                       # print(nationality)
                        eu_count += 1
                    else:
                        non_eu_count += 1

            return_vals.append(str(eu_count) +"," + str(non_eu_count))
    return return_vals
            #print(str(curr_hour) + ":" + str(curr_quarter * 15) + ", eu count:" + str(eu_count) +", non EU count:" + str(non_eu_count))
            #print(non_eu_count)
    #return exit_lines_to_keep
