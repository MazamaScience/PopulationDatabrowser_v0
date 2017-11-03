#!/usr/bin/python
# -- coding: utf-8 --
#
# ISO 3166 arrangement of countries into regions

import sys
from babel import Locale
import json

country_codes = ["AW","AG","AE","AF","DZ","AZ","AL","AM","AD","AO","AS","AR","AU","AT","AI","BH","BB","BW","BM","BE","BS","BD","BZ","BA","BO","MM","BJ","BY","SB","BR","BT","BG","BN","BI","CA","KH","TD","LK","CG","CD","CN","CL","KY","CM","KM","CO","MP","CR","CF","CU","CV","CK","CY","DK","DJ","DM","DO","EC","EG","IE","GQ","EE","ER","SV","ET","CZ","FI","FJ","FM","FO","PF","FR","GM","GA","GE","GH","GI","GD","GG","GL","DE","GU","GR","GT","GN","GY","PS","HT","HK","HN","HR","HU","IS","ID","IM","IN","IR","IL","IT","CI","IQ","JP","JE","JM","JO","KE","KG","KP","KI","KR","KW","NA","KZ","LA","LB","LV","LT","LR","SK","LI","LS","LU","LY","MG","MO","MD","MN","MS","MW","ME","MK","ML","MC","MA","MU","MR","MT","OM","MV","MX","MY","MZ","NC","NE","VU","NG","NL","SX","NO","NP","NR","SR","NI","NZ","PY","PE","PK","PL","PA","PT","PG","PW","GW","QA","RS","MH","MF","RO","PH","PR","RU","RW","SA","PM","KN","SC","ZA","SN","SH","SI","SL","SM","SG","SO","ES","LC","SD","SE","SY","CH","BL","TT","TH","TJ","TC","TO","TG","ST","TN","TL","TR","TV","TW","TM","TZ","CW","UG","GB","UA","US","BF","UY","UZ","VC","VE","VG","VN","VI","WF","EH","WS","SZ","YE","ZM","ZW"]


################################################################
###### each language is an instance of the Language class ######
################################################################

# class Language:
# 	def __init__(self, language, rtxt, html, region_names):
# 		self.language = language
# 		self.rtxt = rtxt
# 		self.html = html
# 		self.region_names = region_names
# 		codes = []
# 		locale = Locale(language)
# 		for code in country_codes:
# 			codes.append(locale.territories[code])
# 		self.country_names = makeList(country_codes, codes)

locale = Locale("en")

class countryObject:
	def __init__(self, code, year, name):
		self.code = code
		self.year = year
		self.name = name

d0 = {}
for item in country_codes:
	d0[item] = 1950

# print("countryID,lastUpdateYear,countryName")

# for item in country_codes:
# 	print(item + "," + str(1950) + "," + locale.territories[item])



y1997 = ["Argentina","Bolivia","Cape Verde","Cote d'Ivoire","El Salvador","Eritrea","French Polynesia","Guinea","Haiti","Liberia","Mozambique","Panama","Puerto Rico","Qatar","Sierra Leone","South Africa","Sudan","United Arab Emirates","United States", "Albania","Algeria","Andorra","Angola","Anguilla","Antigua and Barbuda","Argentina","Armenia","Australia","Austria","Azerbaijan","Bahamas, The","Barbados","Belarus","Belgium","Bosnia and Herzegovina","Botswana","Brazil","Brunei","Bulgaria","Burkina Faso","Burma","Burundi","Cameroon","Canada","Central African Republic","Chile","China","Colombia","Comoros","Congo (Brazzaville)","Congo (Kinshasa)","Costa","Cote d'Ivoire","Croatia","Cuba","Czech Republic","Denmark","Dominica","Dominican Republic","Ecuador","Egypt","El Salvador","Eritrea","Estonia","Ethiopia","Faroe Islands","Finland","France","French","French","Gaza Strip","Georgia","Germany","Gibraltar","Greece","Grenada","Guadeloupe","Guatemala","Guyana","Haiti","Honduras","Hong Kong S.A.R.","Hungary","Iceland","India","Ireland","Israel","Italy","Jamaica","Japan","Jordan","Kazakhstan","Kenya","Kuwait","Kyrgyzstan","Latvia","Lebanon","Lesotho","Libya","Liechtenstein","Lithuania","Luxembourg","Macau","Macedonia, The Former Yugo. Rep. of ","Malaysia","Mali","Malta","Man, Isle of","Martinique","Mauritania","Mauritius","Mexico","Moldova","Montenegro","Morocco","Namibia","Nepal","Netherlands","New","New","Nicaragua","Nigeria","North Korea","Northern Mariana Islands","Norway","Oman","Pakistan","Panama","Paraguay","Peru","Poland","Portugal","Puerto Rico","Qatar","Romania","Russia","Rwanda","Saint","Saint","Saint Helena","Saint Vincent and the Grenadines","San Marino","Sao Tome and Principe","Serbia","Seychelles","Singapore","Slovakia","Slovenia","Somalia","South Africa","South Korea","Spain","Sri Lanka","Suriname","Swaziland","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Trinidad and Tobago","Tunisia","Turkmenistan","Ukraine","United Kingdom","United States","Uruguay","Uzbekistan","Vietnam","Virgin Islands","West Bank","Yemen","Zambia","Zimbabwe"]

y1998 = ["American Samoa","Bangladesh","Cambodia","Guam","India","Iraq","Malawi","North Korea","Palau","Puerto Rico","Uganda","Bermuda","Chile","Cuba","Cyprus","Macau","Mayotte","Netherlands Antilles","Palau","Turks and Caicos Islands","United Kingdom","United States","British Virgin Islands","Bangladesh","Guam","Iran","Libya","Northern Mariana Islands","Peru","Turkey","Virgin Islands, U.S.","Puerto Rico","United States"]

y1999 = ["American Samoa","Guam","Northern Mariana Islands","Puerto Rico","United States","U.S. Virgin Islands"]

y2000 = ["Antigua and Barbuda","Australia","Barbados","Bermuda","Canada","Gibraltar","Grenada","Hong Kong, S.A.R.","Liechtenstein","Man, Isle of ","Mongolia","Montserrat","Singapore","United Kingdom","Virgin Islands, British"]

y2002 = ["Argentina","Bangladesh","Bermuda","Brazil ","Cayman Islands","China","Egypt","India","Iran","Korea, North","Korea, South","Laos","Marshall Islands","Mongolia","Philippines","Puerto Rico","Taiwan","United States","Vietnam"]

y2003 = ["American Samoa","Cuba","Guam","Macau S.A.R.","Micronesia, Federated States of","Mozambique","Northern Mariana Islands","Puerto Rico","Virgin Islands"]

y2004 = ["Armenia","China","Croatia","Estonia","Georgia","Hong Kong S.A.R.","Iceland","Kazakhstan","Kyrgyzstan","Latvia","Lithuania","Malta","Portugal","Russia","Serbia and Montenegro","Singapore","Slovenia","Afghanistan","Algeria","Chile","Ecuador","Iran","Nicaragua","Pakistan","Peru","Saudi Arabia","Tunisia","Uruguay"]

y2005 = ["Bosnia and Herzegovina","Korea, South","Poland","Ukraine","Guatemala","Puerto Rico"]

y2006 = ["Azerbaijan","Belarus","Guatemala","India","Indonesia","Iran","Madagascar","Moldova","Montenegro","Serbia","Sri Lanka","Suriname","Tajikistan","Western Sahara","Puerto Rico"]

y2007 = ["Aruba","Brunei","Comoros","Dominica","France","Japan","Mongolia","Sudan","Taiwan","Turkmenistan","United Arab Emirates","Venezuela","Moldova"]

y2008 = ["Anguilla","Bhutan","Canada","Equatorial Guinea","Faroe Islands","France","Israel","Mauritius","New Zealand","Puerto Rico","Saint Barthelemy","Saint Martin","American Samoa","Andorra","Antigua and Barbuda","Argentina","Australia","Brazil","Cook Islands","Gaza Strip","Greenland","Macau S.A.R.","Maldives","Montserrat","Panama","Philippines","Qatar","Saint Lucia","South Korea","Uzbekistan","Virgin Islands, U.S.","Wallis and Futuna","West Bank","Bangladesh","Bermuda","Bolivia","Ecuador","Korea, North","Kosovo","Mauritania","Nauru","Nepal","Niger","Palau","Puerto Rico","Saint Vincent and the Grenadines","Senegal","Serbia","Seychelles","Turkey","Turkmenistan","United States"]

y2009 = ["Afghanistan","Bahamas","Burundi","Colombia","Cyprus","Djibouti","Egypt","Ghana","Gibraltar","Guyana","India","Jordan","Malawi","Mali","Morocco","Northern Mariana Islands","Pakistan","Papua New Guinea","Puerto Rico","Rwanda","Sierra Leone","Swaziland","Syria","United States","Vietnam","Yemen","Burma","Cape Verde","Central African Republic","China","Costa Rica","El Salvador","Grenada","Kiribati","Lebanon","Lesotho","Liberia","Monaco","Oman","Paraguay","Saint Kitts and Nevis","Saint Pierre and Miquelon","Samoa","San Marino","Sao Tome and Principe","Tuvalu","Western Sahara"]

y2010 = ["Albania","Bangladesh","Cambodia","Dominican Republic","Fiji","Guernsey","Haiti","Hungary","Iran","Ireland","Isle of Man","Jersey","Laos","Malaysia","Nauru","New Caledonia","Pakistan","Puerto Rico","Romania","Saudi Arabia","Senegal","Solomon Islands","Spain","Sudan","Togo","United Kingdom","United States","Zambia","Bahrain ","Congo (Kinshasa)","Cuba","The Gambia","Germany","Italy","North Korea","Kuwait","Mayotte","Mozambique","Nicaragua","Peru","Somalia","Sri Lanka","Tonga","Tunisia","Turks and Caicos Islands","Uruguay"]

y2011 = ["Afghanistan","Angola","Azerbaijan","Comoros","Curacao","French Polynesia","Japan","Kazakhstan","Kenya","Liechtenstein","Moldova","Netherlands","Nigeria","Qatar","Singapore","Sint Maarten","Suriname","United States","Virgin Islands, British"]

y2012 = ["Algeria","American Samoa","Belarus","Bosnia and Herzegovina","Brazil","Chile","Ethiopia","France","Ghana","Guam","Indonesia","Kyrgyzstan","Libya","Madagascar","Mali","Niger","Northern Mariana Islands","Puerto Rico","Russia","South Sudan","Sudan","Switzerland","Taiwan","Tanzania","Timor-Leste","Uganda","United States","Vanuatu","Virgin Islands, U.S.","Zambia"]

y2013 = ["Armenia","Burundi","Cameroon","Congo (Brazzaville)","Czech Republic","Estonia","Georgia","Hong Kong","Mexico","Mongolia","Norway","Puerto Rico","Sweden","Thailand","United States","Yemen"]

allYears = y1997 + y1998 + y1999 + y2000 + y2002 + y2003 + y2004 + y2005 + y2006 + y2007 + y2008 + y2009 + y2010 + y2011 + y2012 + y2013
allYears = list(set(allYears))
allYears.sort()

d1 = {1997:y1997, 1998:y1998, 1999:y1999, 2000:y2000, 2002:y2002, 2003:y2003, 2004:y2004, 2005:y2005, 2006:y2006, 2007:y2007, 2008:y2008, 2009:y2009, 2010:y2010, 2011:y2011, 2012:y2012, 2013:y2013}

d2 = {}

for item in allYears:
	d2[item] = 1950
	for key,value in d1.iteritems():
		if item in value:
			d2[item] = key
	
f = open('estimateUpdateYears.csv', 'w')

f.write("countryCode, countryName, lastUpdateYear\n")

for key,value in d0.iteritems():
	altKey = locale.territories[key]
	if altKey in d2:
		d0[key] = d2[altKey]
	f.write(key + ", " + altKey.encode("utf-8") + ", " + str(d0[key]) + "\n")

f.close()



