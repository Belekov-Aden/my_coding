#1 Problem
########################################
import requests
import pprint

url_site = 'https://api.github.com/emojis'

read = requests.get(url_site)

pprint.pprint(read.json())

########################################



#2 Problem
#########################################
import requests
import pprint

url_site = 'https://httpbin.org/post'

info = {
    'name':'Aden',
    'model':'Lenovo'
}

write_url = requests.post(url_site, info)


print(write_url.status_code)
pprint.pprint(write_url.json())
##########################################

