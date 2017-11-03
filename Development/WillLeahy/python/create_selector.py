#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# ISO 3166 arrangement of countries into regions

import sys
from babel import Locale

locale = Locale('en')


databrowser_countries = ["AW","AG","AE","AF","DZ","AZ","AL","AM","AD","AO","AS","AR","AU","AT","AI","BH","BB","BW","BM","BE","BS","BD","BZ","BA","BO","MM","BJ","BY","SB","BR","BT","BG","BN","BI","CA","KH","TD","LK","CG","CD","CN","CL","KY","CM","KM","CO","MP","CR","CF","CU","CV","CK","CY","DK","DJ","DM","DO","EC","EG","IE","GQ","EE","ER","SV","ET","CZ","FI","FJ","FM","FO","PF","FR","GM","GA","GE","GH","GI","GD","GG","GL","DE","GU","GR","GT","GN","GY","PS","HT","HK","HN","HR","HU","IS","ID","IM","IN","IR","IL","IT","CI","IQ","JP","JE","JM","JO","KE","KG","KP","KI","KR","KW","NA","KZ","LA","LB","LV","LT","LR","SK","LI","LS","LU","LY","MG","MO","MD","MN","MS","MW","ME","MK","ML","MC","MA","MU","MR","MT","OM","MV","MX","MY","MZ","NC","NE","VU","NG","NL","SX","NO","NP","NR","SR","NI","NZ","PY","PE","PK","PL","PA","PT","PG","PW","GW","QA","RS","MH","MF","RO","PH","PR","RU","RW","SA","PM","KN","SC","ZA","SN","SH","SI","SL","SM","SG","SO","ES","LC","SD","SE","SY","CH","BL","TT","TH","TJ","TC","TO","TG","ST","TN","TL","TR","TV","TW","TM","TZ","CW","UG","GB","UA","US","BF","UY","UZ","VC","VE","VG","VN","VI","WF","EH","WS","SZ","YE","ZM","ZW"]

print('          <select id="subset" name="subset">')
for code in databrowser_countries:
     print('              <option value="' + code + '">' + locale.territories[code] + '</option>')
print('          </select>')

