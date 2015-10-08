# ceph-pg-analyst - Analyst tool for placement groups, OSDs and Hosts on Ceph Storage clusters.

## ceph-pg-analyst analyses some of the data for the placement groups and hosts on CEPH storage and gives statistics such as standard distribution and variance. 

### Requires [NumPy](http://www.numpy.org/) and [matplotlib](http://matplotlib.org/)  modules as it uses them for the statistics and histograms. It does check if these are installed and will print an error code if you don't have them installed. 
### flags/usage = '-h "filepath/filename"' will save an image of the histogram to the directory specified and '-H' will show a histogram on screen for further manipulation 


note : the python 3 code will be finished after the 2.7 version or may just be merged into the code with a function that checks python version. For the time being, the code is applicable to python 2.7 when being developed.


This program can take up to 2 PG pools for comparison however will work with one, and will save an image of two plots if two pool arguments are given. they must share the same OSD tree to work, it should be noted that only one JSON tree file can be used for the (up to) 2 arguments for the Placement group pools. With the multi argument histograms a key will be shown in the upper right and both datasets will be plotted. If you have a display manager installed this will show up in a seperate window and can be explored with the matplotlib window. 


` python -i ceph-pg-analyst.py ./testfiles/PGsPool26 ./testfiles/grid-tree.json -H`
will show a histogram of PG pool 26 and 

  `python -i ceph-pg-analyst.py ./testfiles/PGsPool25 ./testfiles/PGsPool26 ./testfiles/grid-tree.json -H`
will show plots of both pools on one histogram 

After this you will be shown statistics on the data such as mean, max and min values, variance and standard deviation. It does this for both placement groups on hosts and vice versa, and then asks if you want a histogram drawn which looks like this: ![](http://i.imgur.com/jlTAxBo.png)
or this:
![](http://i.imgur.com/WP9syXC.png)
Note: you can use the far right button on the histogram window to save it to a PNG formatted image. 

For the test files the histogram will look weird on 'PGsPools25' because the frequency is always 19 however on 'PGsPools25' the histogram looks more normal. 

