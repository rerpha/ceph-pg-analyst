# ceph-pg-analyst

## ceph-pg-analyst analyses some of the data for the CEPH storage and gives statistics such as standard distribution and variance of hosts and placement groups. 

### Requires [NumPy](http://www.numpy.org/) and [matplotlib](http://matplotlib.org/)  modules as it uses them for the statistics and histograms. It does check if these are installed and will print an error code if you don't have them installed. 

note : the python 3 code will be finished after the 2.7 version or may just be merged into the code with a function that checks python version. For the time being, the code is applicable to python 2.7 when being developed.

This program takes two arguments(at the moment); the first being a plain text file with all placement groups of the files in brackets, and the second being a grid tree in JSON format. For example: 

` python -i p2nhcv4.py ./testfiles/PGsPool26 ./testfiles/grid-tree.json 
`

After this you will be shown statistics on the data such as mean, max and min values, variance and standard deviation. It does this for both placement groups on hosts and vice versa, and then asks if you want a histogram drawn which looks like this: ![](http://i.imgur.com/jlTAxBo.png)
Note: you can use the far right button on the histogram window to save it to a PNG formatted image. 

For the test files the histogram will look weird on 'PGsPools25' because the frequency is always 19 however on 'PGsPools25' the histogram looks more normal. 

