#!/usr/bin/python

import sys, getopt, os.path 
import argparse
import json
import httplib

def main(argv):
    outputfile = 'log.txt'

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", dest="url", required=True, help="URL to call")
    parser.add_argument("-m", dest="method", required=True, default=None,  help="method (GET, POST, DELETE, PUT)")
    parser.add_argument("-d", dest="dataFile", default=None, help="path of the file that contains the body data to send")
    parser.add_argument("-o", dest="outputfile", default="out.txt", help="path of the output log file, default out.txt")
    parser.add_argument("-t", dest="tout", default=10, help="timeout for the response in second, default 10")
    parser.add_argument("-cookie", dest="cookie", default=None, help="add cookie session to header")
    parser.add_argument("-v", action='store_true', dest="verbose", default=False, help="verbose mode, shows the output of the request")
    args = parser.parse_args()

    readFileLines(args.url, args.outputfile, args.tout, args.cookie, args.method, args.dataFilei, args.verbose)

def readFileLines(url, outputfile, tout, cookie, method, dataFilei, verbose):
    urlModel = urlFormat(url)
    url = urlModel['url']
    params = urlModel['params'] 
    conn = httplib.HTTPConnection(url, 80)

    if dataFile:
        dataContent = open(dataFile, 'r').read() 
        header = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        body = dataContent
        conn.request(method, params, body)
    else:    
        header = ''
        body = ''
        conn.request(method, params) 

    if cookie:
        req.add_header("Cookie", cookie);

    resp = conn.getresponse()
    content = resp.read()
    status = resp.status
    outstring =  str(url).rstrip("\n") + str(params).rstrip("\n")  + ' | status: ' + str(status) + "\n" + content
    if (verbose):
        print outstring
    fout = open(outputfile, 'w') 
    fout.write(outstring)

def urlFormat(url):
    url = url.replace("http://", "") 
    slashPos = url.index('/')
    return {'url': url[0:slashPos], 'params': url[slashPos:]} 

if __name__ == "__main__":
    main(sys.argv[1:])
