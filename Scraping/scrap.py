import requests
import bs4

res = requests.get("https://aws.amazon.com/pm/amplify/?trk=51792fca-94b4-4ad5-8968-246e39b3a631&sc_channel=ps&ef_id=Cj0KCQjw37nNBhDkARIsAEBGI8P1Czja3B2iFbxub1M2JY3b12KeTwgkyUesA0vg5Pbuf7otB8gnZOsaAiBbEALw_wcB:G:s&s_kwcid=AL!4422!3!798550392232!p!!g!!static%20website!23600695122!192406566454&gad_campaignid=23600695122&gbraid=0AAAAADjHtp_nP8-DYr6lFQQyY6vUWjVGw&gclid=Cj0KCQjw37nNBhDkARIsAEBGI8P1Czja3B2iFbxub1M2JY3b12KeTwgkyUesA0vg5Pbuf7otB8gnZOsaAiBbEALw_wcB")

soup = bs4.BeautifulSoup(res.text, "lxml")
computer = soup.select('.rglg_8e9ae6ea')[0]
print(computer['src'])

image_link = requests.get('https://d1.awsstatic.com/amplify-frameworks-logo-grid/swift-color.3f286601613a0eb276b8fe040f9330ed279327a8.svg')

f = open('swift-color.svg', 'wb')
f.write(image_link.content)
f.close()