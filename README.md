pytonApiChecker
===============

the script can performs GET, POST, PUT and DELETE requests with an additional input file, it also can writes the output on screen or in the specified output file.

usage: apiChecker.py [-h] -u URL -m METHOD [-d DATAFILE] [-o OUTPUTFILE]
                     [-t TOUT] [-cookie COOKIE]

optional arguments:
  -h, --help      show this help message and exit
  -u URL          URL to call
  -m METHOD       method (GET, POST, DELETE, PUT)
  -d DATAFILE     path of the file that contains the body data to send
  -o OUTPUTFILE   path of the output log file, default out.txt
  -t TOUT         timeout for the response in second, default 10
  -cookie COOKIE  add cookie session to header
  
  
  
Example

python apiChecker.py -u http://httpbin.org/post -m POST -d input.txt -o out.txt

python apiChecker.py -u http://httpbin.org/status/418 -m GET -o out.txt
