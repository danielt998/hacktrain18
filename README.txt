The code will have the following structure

                               groups.py
                                    |
                                    |
                                   \ /
                                    .
 chckinout.py ================>  main.py <=============== nationality.py
                                    |
                                    |
                                   \ /
                                    .
                                 out.csv

where
  groups.py will collect data about different groups of people and sizes
  checkinout.py will collect information about the numbers of people checking in and out
  nationality.py will collect information about the nationality of different passengers
  main.py will read in the data from these three classes and put them into a single csv with times split into 15 minute segments
