# compute score for an entry in the KDD'99 classifier learning contest 
# copyright (c) Charles Elkan, first version written 8/5/99, all rights reserved
BEGIN { 
# initialize matrix cost[actual,predicted] 
# note that all other entries of the cost matrix are zero, so the computed 
# total cost is too low if either actual or predicted is ever out-of-range

for (i = 0; i <= 4; i++) 
      for (j = 0; j <= 4; j++) 
            if (i == j) cost[i,j] = 0; 
            else cost[i,j] = 2;

cost[0,1] = 1; 
cost[1,0] = 1; 
cost[2,1] = 1; 
cost[3,0] = 3; 
cost[4,0] = 4;

n = 311029;

i = 0; 
totalcost = 0; 
sqtotal = 0; 
}

{ 
# assume that the file to be scored has one "predicted" value per line 
# assume that the "answers" file has the same format

predicted = $1 + 0; 
pcount[predicted]++;

getline < "/home/elkan/attacks/answers" 
real = $1; 
count[real]++;

c = cost[real,predicted]; 
totalcost += c; 
sqtotal += c*c; 
matrix[real,predicted]++; 
i++; 
}

END { 
print "\nKDD'99 contest scoring report for file", FILENAME;

print "\nConfusion matrix:";

printf "      predicted  "; 
for (predicted = 0; predicted <= 4; predicted++) printf "%6.0f\t", predicted; 
printf "  %%correct\n"; 
print "actual  \\---------------------------------------------------------"; 
for (real = 0; real <= 4; real++) { 
      printf real "\t|\t ";

      for (predicted = 0; predicted <= 4; predicted++) 
            printf "%6.0f\t", matrix[real,predicted]+0;

      pcorrect = 100.0*matrix[real,real]/count[real]+0; 
      printf "%6.1f%%\n", pcorrect; 
      }

printf "\t|\n%%correct|\t"; 
for (predicted = 0; predicted <= 4; predicted++) { 
      if (pcount[predicted] > 0) 
            pcorrect = 100.0*matrix[predicted,predicted]/pcount[predicted]+0; 
      else pcorrect = 0; 
      printf "%6.1f%%\t", pcorrect; 
      }

print "\n\nTotal cost", totalcost, "over", i, "predictions";

mean = totalcost/i; 
variance = sqtotal - mean*totalcost; 
stddev = sqrt( variance / i );

print mean, "+/-", stddev, "is mean +/- std. dev. cost for file", FILENAME, "\n";

}