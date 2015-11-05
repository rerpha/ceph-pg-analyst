#!/usr/bin/env python
# requires: numpy, matplotlib
# complies with PEP 008
# written in python 2.7, however a library called 2to3
# allows this program to be run on python 3.x
from sys import argv  # imports argv from sys module
from sys import exit
import os
from os.path import splitext
from collections import Counter  # imports Counter from collections module
from json import load  # imports load from the json module
import matplotlib
if not os.environ.get('DISPLAY'):
    matplotlib.use('Agg')
import numpy  # imports the entire numpy module
import matplotlib.pyplot as plt  # imports pyplot from matplotlib, calls at plt
from imp import find_module  # imports find_module from imp
from shutil import rmtree
from matplotlib.widgets import Slider
import mpld3
import socket
from socket import gethostbyname as ghbn
plot_file='' #needs to be set up outside function otherwise try: is needed
def statprint(host_per_pg, pg_per_host):
    val = pg_per_host.values()  # sets val to a list of the values in pg_per_host
    mean = numpy.mean(val)
    maxvalue = numpy.amax(val)
    minvalue = numpy.amin(val)
    std = numpy.std(val)
    median = numpy.median(val)
    variance = numpy.var(val)
    print "for placement groups on hosts: "
    print "the mean is: ", mean
    print "the max value is: ", maxvalue
    print "the min value is: ", minvalue
    print "the standard deviation is: ", std
    print "the median is: ", median
    print "the variance is: ", variance
    # prints statements for stats
    host_mean = numpy.mean(host_per_pg)
    host_max = numpy.amax(host_per_pg)
    host_min = numpy.amin(host_per_pg)
    host_std = numpy.std(host_per_pg)
    host_median = numpy.median(host_per_pg)
    host_variance = numpy.var(host_per_pg)
    # these are the variables for hosts/pgs
    print "hosts per placement group: "
    print "the mean is: ", host_mean
    print "the max value is: ", host_max
    print "the min value is: ", host_min
    print "the standard deviation is: ", host_std
    print "the median is: ", host_median
    print "the variance is: ", host_variance

try:
    find_module('numpy')  # makes sure numpy is installed
    find_module('matplotlib')  # makes sure matplotlib is installed
    foundmodule = True  # sets foundmodule to boolean True
except ImportError:  # if there is an importerror, one module isnt installed
    foundmodule = False  # sets foundmodule to boolean False
module_error_message = ("You dont appear to have either numpy \
 or matplotlib installed. The program will not work without these.\
 please press ctrl+D to finish")  # string with error message
if foundmodule == False:  # if the foundmodule is anything but True
    print(module_error_message)  # outputs the error message string
else:
    pass  # otherwise, code continues running

def process_tree(tf):
    with open(tf) as treefile:
         tree = load(treefile)

    hosts = filter(lambda x: True if x['type'] == 'host' else False, tree['nodes'])

    osd2host = {}

    for h in hosts:
        name = h['name']
        for c in h['children']:
            osd2host[c] = name
    return osd2host

def process_pool(pf, osd2host):
    with open(pf) as pfd:
        osd_lists = map(eval, map(str.strip, pfd.readlines()))
        host_per_pg = []
        pg_per_host = Counter()
        for pg in osd_lists:
            pg_hosts = set()
            for osd in pg:
                hostname = osd2host[osd]
                pg_per_host[hostname] += 1
                pg_hosts.add(hostname)
            host_per_pg.append(len(pg_hosts))
    return host_per_pg, pg_per_host

del(argv[0])
if argv[0] in ['-h','-H','-s','-b','-v','-w','-o']:
    hist_opt = argv[0][1]
    if hist_opt == 's':
        plot_file = argv[1]
        del(argv[1])
    del(argv[0])
else:
    hist_opt = None


tf = argv[0]
del(argv[0])

poolfiles = argv

osd2host = process_tree(tf)

try:
    host_per_pg_dict = { splitext(x)[0]: process_pool(x, osd2host) for x in poolfiles }
except:
    print("file error; one of the files is not compatible with this program. ")
    exit()

if os.path.isfile(plot_file): 
    file_opt = raw_input("this file already exists. do you want to overwrite? (y/n) \n").lower()
    if file_opt == 'y' :
        pass
    else: 
        exit()
def iter_pool():
    print pool
    statprint(*series)
    plt.hist(series[0], alpha=1, label=pool,histtype='bar', stacked=True)
def hist_labels():
    plt.legend(loc='upper right')
    plt.title("Hosts per pg histogram")
    plt.xlabel("No. of hosts")
    plt.ylabel("Frequency")

if hist_opt:
    colors = ['b','g','r','c','m','y','k','w']
    if hist_opt == 'H':
        for pool, series in host_per_pg_dict.items():
            iter_pool()
        hist_labels()
        if os.environ.get('DISPLAY'):
            plt.show()
        else:
            print("no display manager installed, a histogram will not display. use '-s' to save the file or '-w' to start a webserver. \n")
    elif hist_opt == 's':
        plt.savefig(plot_file)
    elif hist_opt == 'h':
        for pool, series in host_per_pg_dict.items():
            iter_pool()
            plt.show()
    elif hist_opt == 'b':
        for pool, series in host_per_pg_dict.items():
            plt.hist(series[0], alpha=1, label=pool,histtype='bar', stacked=True)
        hist_labels()
        plt.show()
    elif hist_opt == 'v':
        for pool, series in host_per_pg_dict.items():
            iter_pool()
    elif hist_opt == 'w':
        for pool, series in host_per_pg_dict.items():
            plt.hist(series[0], alpha=1, label=pool,histtype='bar', stacked=True)
        hist_labels()
        plt.legend(fontsize= 'small', framealpha= 0)
        mpld3.show(ip=ghbn(socket.gethostname()))
    elif hist_opt == 'o':
        fig = plt.figure()
        for pool, series in host_per_pg_dict.items():
            plt.hist(series[0], alpha=1, label=pool,histtype='bar', stacked=True)
        hist_labels()
        plt.legend(fontsize= 'small', framealpha= 0)
        mpld3.save_html(fig, './output.html')
        print("saved. should display in the apache server now. ")

#   elif hist_opt == 'x':
#        for pool, series in host_per_pg_dict.items():
#            plt.hist(series[0], alpha=1, label=pool,histtype='bar', stacked=True)
#            mpld3.display(plt)
#    else:
#        print "No flag selected, default is -H"
#        hist_opt = 'H'
