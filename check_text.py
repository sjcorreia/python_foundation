from __future__ import print_function

def read_test():
	quotes = open("movie_quotes.txt")
	contents = quotes.read()
	print(contents)
	# wdyl.com/profamity?q=
	# http://www.wdylike.appspot.com/?q=shot

read_test()
