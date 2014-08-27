pytonApiChecker
===============

the script can performs GET, POST, PUT and DELETE requests with an additional input file, it also can writes the output on screen or in the specified output file.

usage: apiChecker.py [-h] -u URL -m METHOD [-d DATAFILE] [-o OUTPUTFILE]
                     [-t TOUT] [-cookie COOKIE]

Example

python apiChecker.py -u http://httpbin.org/post -m POST -d input.txt -o out.txt

python apiChecker.py -u http://httpbin.org/status/418 -m GET -o out.txt
