# ceph-pg-analyst - Analyst tool for the distribution of placement groups, OSDs and Hosts on Ceph Storage clusters.

## ceph-pg-analyst analyses some of the data for the placement groups and hosts on Ceph storage and gives statistics such as standard distribution and variance. 

### Requires [NumPy](http://www.numpy.org/) and [matplotlib](http://matplotlib.org/)  modules as it uses them for the statistics and histograms. It does check if these are installed and will print an error code if you don't have them installed. 
### flags/usage = `ceph-pg-analyst.py -s "filepath/filename ~json tree~ ~pool names~"` will save an image of the histogram to the directory specified and `ceph-pg-analyst.py -H ~json tree~ ~pool names~` will show a histogram on screen for further manipulation, `ceph-pg-analyst.py -h ~filenames~ ` will show a seperate histogram for each data set, `-b` = only show histogram, `v` = only show stats , `-w`  = start webserver on localhost:8888


note : the python 3 code will be finished after the 2.7 version or may just be merged into the code with a function that checks python version. For the time being, the code is applicable to python 2.7 when being developed.


This program can (now) take any amount of pools providing they share the same JSON tree. the usage of this is shown above. 


` ceph-pg-analyst.py -H ./testfiles/grid-tree.json ./testfiles/PGsPool26 `
will show a histogram of PG pool 26 and 

  `python -i  ceph-pg-analyst.py -H ./testfiles/grid-tree.json ./testfiles/PGsPool25 ./testfiles/PGsPool26`
will show plots of both pools on one histogram 

After this you will be shown statistics on the data such as mean, max and min values, variance and standard deviation. It does this for both placement groups on hosts and vice versa, and then asks if you want a histogram drawn which looks like this: ![](http://i.imgur.com/jlTAxBo.png)

or this:

![](http://i.imgur.com/WP9syXC.png)
Note: you can use the far right button on the histogram window to save it to a PNG formatted image. 

For the test files the histogram will look strange on 'PGsPools25' because the frequency is always 19 however on 'PGsPools25' the histogram looks more normal. 

