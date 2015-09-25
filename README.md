# ceph-pg-analyst
Analyses some of the data for the ceph storage and gives statistics such as standard distribution and variance of hosts and placement groups. 
Requires Numpy and matplotlib modules as it uses them for the statistics and histograms.
This program takes two arguments; the first being a plain text file with all placement groups of the files in brackets, and the second being a grid tree in JSON format. 

For the test files the histogram will look weird on 'PGsPools26' because the frequency is always 19 however on 'PGsPools25' the histogram looks more normal. 
