from __future__ import print_function
import urllib.request
# urllib.request is the module needed for Python 3.4.3
# perhaps with Python 2.7 there is a different way to use urllib

PROFANITY_DETECTED = False

def read_test():
    quotes = open("text/movie_quotes.txt")
    contents = quotes.read()
    # print(contents)
    # wdyl.com/profanity?q=
    # http://www.wdylike.appspot.com/?q=shot
    
    # Test this again without iterating over each word in the list!!
    # Think about performance, but at least this works
    contentList = contents.split()
    quotes.close()
    for word in contentList:
        check_profanity(word)

def check_profanity(text_to_check):
    # print(text_to_check)
    proxy_settings = urllib.request.getproxies()
    # urllib.request.ProxyHandler(proxy_settings)
    url_text = "http://www.wdylike.appspot.com/?q="
    new_url = url_text + text_to_check
    # print(new_url)
    # url_text = r"http://www.wdylike.appspot.com/?q=shot"
    response = urllib.request.urlopen(new_url)
    output = response.read()
    if output == b'true':
        print("Profanity detected!!")
        PROFANITY_DETECTED = True
    # print(output)
    response.close()

if __name__ == "__main__":
    read_test()
    if not PROFANITY_DETECTED:
        print("The text is acceptable :)")
    print(urllib.request.getproxies.__module__)
