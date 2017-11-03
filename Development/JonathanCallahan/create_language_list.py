#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# ISO 3166 arrangement of countries into regions

import sys
from babel import Locale


######################################################
###### english titles for R and JS to reference ######
######################################################

rtxt_titles = ["population", "ylab1", "ylab2", "subtitle", "growth", "decline", "million", "thousand", "millions", "thousands"]
html_titles = ["country", "group", "header", "select_country"]



#######################
###### ISO codes ######
#######################

language_codes = ['en', 'de', 'fr', 'es', 'de', 'it', 'ru', 'tr']

flag_codes = ['US', 'DE', 'FR', 'ES', 'DE', 'IT', 'RU', 'TR']

# carribiean minus GP, MQ
# south america minus GF
region_codes = [
                # North America
                "US,CA,MX",
                # Central America
                "BZ,CR,GT,HN,NI,PA,SV",
                # Caribbean
                "AG,AW,CU,DM,DO,HT,JM,LC,PR,TT",
                # South America
                "AR,BO,BR,CL,CO,EC,GY,PE,SR,UY,VE",
                # Europe
                "AL,BA,BG,DK,IE,AT,CZ,FI,FR,DE,GR,HR,HU,IS,IT,LV,BY,LT,SK,LI,MK,BE,ME,NL,NO,PL,PT,RO,RU,RS,SI,ES,SE,CH,TR,GB,UA,EE",
                # European Union
                "AT,BE,BG,CY,CZ,DK,EE,FI,FR,DE,GR,HU,IE,IT,LV,LT,LU,MT,NL,PL,PT,RO,SK,SI,ES,SE,GB",
                # Former Soviet Union
                "AM,AZ,BY,EE,GE,KZ,KG,LV,LT,MD,RU,TJ,TM,UA,UZ",
                # Middle East
                "AE,BH,IL,IR,IQ,JO,KW,LB,OM,PS,QA,SA,SY,YE",
                # North Africa
                "DZ,EG,LY,MA,TN,EH",
                # Sub-Saharan Africa
                "CG,CD,NG,RW,SN,SL,SO,SD,TZ,UG,BJ,BI,CM,TD,CF,GQ,ER,ET,GM,GA,GH,GN,CI,KE,LR,ML,MR,NE,AO,BW,LS,MG,MW,MZ,NA,SZ,ZA,ZM,ZW",
                # OECD
                "AT,BE,DZ,DK,FI,FR,DE,GR,HU,IS,IE,IT,LU,NL,NO,PL,PT,SK,ES,SE,CH,TR,GB,AU,CA,JP,MX,NZ,KR,US",
                # OPEC
                "DZ,AO,EC,IR,IQ,KW,LY,NG,QA,SA,AE,VE",
                ]

country_codes = ["AW","AG","AE","AF","DZ","AZ","AL","AM","AD","AO","AS","AR","AU","AT","AI","BH","BB","BW","BM","BE","BS","BD","BZ","BA","BO","MM","BJ","BY","SB","BR","BT","BG","BN","BI","CA","KH","TD","LK","CG","CD","CN","CL","KY","CM","KM","CO","MP","CR","CF","CU","CV","CK","CY","DK","DJ","DM","DO","EC","EG","IE","GQ","EE","ER","SV","ET","CZ","FI","FJ","FM","FO","PF","FR","GM","GA","GE","GH","GI","GD","GG","GL","DE","GU","GR","GT","GN","GY","PS","HT","HK","HN","HR","HU","IS","ID","IM","IN","IR","IL","IT","CI","IQ","JP","JE","JM","JO","KE","KG","KP","KI","KR","KW","NA","KZ","LA","LB","LV","LT","LR","SK","LI","LS","LU","LY","MG","MO","MD","MN","MS","MW","ME","MK","ML","MC","MA","MU","MR","MT","OM","MV","MX","MY","MZ","NC","NE","VU","NG","NL","SX","NO","NP","NR","SR","NI","NZ","PY","PE","PK","PL","PA","PT","PG","PW","GW","QA","RS","MH","MF","RO","PH","PR","RU","RW","SA","PM","KN","SC","ZA","SN","SH","SI","SL","SM","SG","SO","ES","LC","SD","SE","SY","CH","BL","TT","TH","TJ","TC","TO","TG","ST","TN","TL","TR","TV","TW","TM","TZ","CW","UG","GB","UA","US","BF","UY","UZ","VC","VE","VG","VN","VI","WF","EH","WS","SZ","YE","ZM","ZW"]


################################################################
###### each language is an instance of the Language class ######
################################################################

class Language:
	def __init__(self, language, rtxt, html, region_names):
		self.language = language
		self.rtxt = rtxt
		self.html = html
		self.region_names = region_names
		codes = []
		locale = Locale(language)
		for code in country_codes:
			codes.append(locale.territories[code])
		self.country_names = codes


################################################################
###### create language objects and store them in an array ######
################################################################

en = Language('en',["Population 2014","Population","Annual change","Data: U.S. Census Bureau IDB | Graphic: mazamascience.com","99% growth since 2000","99% decline since 2000","million","thousand","millions","thousands"], ["Country","Group","Population Databrowser","Select a country"], ["North America","Central America","Caribbean","South America","Europe","European Union","Former Soviet Union","Middle East","North Africa","Sub-Saharan Africa","OECD","OPEC"])

de = Language('de', ["Bevölkerung 2014", "Bevölkerung", "Veränderung gegenüber Vorjahr", "Daten: US Census Bureau IDB | Grafik: mazamascience.com", "99% Wachstum seit 2000", "99% Rückgang seit 2000:", "Millionen", "Tausend", "Millionen", "Tausende"], ["Land", "Gruppe", "Databrowser Bevölkerung", "Wählen Sie ein Land"], ["Nordamerika", "Zentralamerika", "Karibik", "Südamerika", "Europa", "Europäische Union", "ehemalige Sowjetunion", "Nahost", "Nordafrika", "Afrika südlich der Sahara", "OECD", "OPEC"])

fr = Language('fr', ["Population 2014", "Population", "Variation annuelle", "Données: US Census Bureau BID | Graphique: mazamascience.com", "Croissance de 99% depuis 2000", "99% de déclin depuis 2000", "million", "mille", "millions", "milliers"], ["Pays", "Groupe", "Population Databrowser", "Sélectionnez un pays"], ["Amérique du Nord", "Amérique centrale", "Caraïbes"," Amérique du Sud","Europe","l'Union européenne","ex-Union soviétique","Moyen-Orient","Afrique du Nord","l'Afrique sub-saharienne","OCDE","OPEP"])

es = Language('es', ["Población 2014", "Población", "Variación anual", "Datos: Censo de los EE.UU. Oficina del BID | Gráfico: mazamascience.com", "Crecimiento del 99% desde el año 2000", "99% de disminución desde el año 2000:" , "millones", "mil", "millones", "miles"], ["País", "Grupo", "Población Databrowser", "Seleccione un país"], ["América del Norte", "América Central", "Caribe", "América del Sur", "Europa", "Unión Europea", "ex Unión Soviética", "Oriente Medio", "África del Norte", "África subsahariana", "OCDE", "La OPEP"])

it = Language('it', ["Popolazione 2014", "Popolazione", "Variazione annuale", "Data: US Census Bureau IDB | Graphic: mazamascience.com", "Il 99% di crescita dal 2000", "99% in calo dal 2000:" , "milioni", "mille", "milioni", "migliaia"], ["Paese", "Gruppo", "Population Databrowser", "Scegliere un paese"], ["America del Nord", "America centrale", "Caraibi", "Sud America", "Europa", "Unione europea", "Ex Unione Sovietica", "Medio Oriente", "Africa del Nord", "Africa sub-sahariana", "OCSE", "OPEC"])

ru = Language('ru', ["Население 2014", "Население", "Годовое изменение", "данных: Бюро переписи населения США ИБР | Графический: mazamascience.com", "99%-ный рост с 2000 года", "99%-ное снижение с 2000 года:" , "миллион", "тысяча", "миллионы", "тысячи"], ["Страна", "Группа", "Население Databrowser", "Выберите страну"], ["Северная Америка", "Центральная Америка", "карибский", "Южная Америка", "Европа", "Европейский Союз", "бывший Советский Союз", "Ближний Восток", "Северная Африка", "К югу от Сахары", "ОЭСР", "ОПЕК"]) 

tr = Language('tr', ["Nüfus 2014", "Nüfus", "Yıllık değişim", "Veri: US Census Bureau IDB | Grafik: mazamascience.com", "2000 yılından bu yana% 99 büyüme", "2000 yılından bu yana% 99 düşüş:" , "milyon", "bin", "milyon", "binlerce"], ["Ülke", "Grup", "Nüfus DataBrowser", "bir ülke seçin"], ["Kuzey Amerika", "Orta Amerika", "Karayip", "Güney Amerika", "Avrupa", "Avrupa Birliği", "Eski Sovyetler Birliği", "Ortadoğu", "Kuzey Afrika", "Sahraaltı Afrika", "OECD", "OPEC"]) 

languages = [en, de, fr, es, it, ru, tr]


# foo = u'Δ, Й, ק, ‎ م, ๗, あ, 叶, 葉, and 말.'
# f = open('./unicodeTest.txt', 'w')
# f.write(foo.encode('utf8'))
# f.close()

# jsonFile = open('./language.json', 'w')


# #######################################################################
# ###### function that writes commas except after the last element ######
# #######################################################################

# def fencepost( item, items ):
# 	if (items.index(item) != len(items) - 1):
# 		print(',')
# 	return


# ##############################
# ###### start json file #######
# ##############################

# print('{')

# # object of flag and language pairs
# print('"flags":{')
# for language, flag in zip(language_codes, flag_codes):
# 	print('"' + language + '":"' + flag + '"')
# 	fencepost(language, language_codes)

# print('}, ')
# # language object
# for item in languages: 

# 	#start country
# 	print('"' + item.language + '":{')
	
# 	# rtext
# 	print('"rtxt": {')
# 	for title, txt in zip(rtxt_titles, item.rtxt):
# 		print('"' + title + '":"' + txt + '"')
# 		fencepost(title, rtxt_titles)
# 	print('},')

# 	#html
# 	print('"html": {')
# 	for title, txt in zip(html_titles, item.html):
# 		print('"' + title + '":"' + txt + '"')
# 		fencepost(title, html_titles)
# 	print('},')

# 	# #array of code country pairs
# 	print('"countries": [')
# 	for code, name in zip(country_codes,item.country_names):
# 		print('{"code":"' + code + '", "name":"' + name + '"}')
# 		fencepost(code, country_codes)
# 	print('],')
	
# 	# #array of code region pairs
# 	print('"regions": [')
# 	for code, name in zip(region_codes,item.region_names):
# 		print('{"code":"' + code + '", "name":"' + name + '"}')
# 		fencepost(code, region_codes)
# 	print(']')

# 	# end country
# 	print('}')
# 	if (languages.index(item) != len(languages) - 1):
# 		print(',')

# print('}')


# jsonFile.close()

###############################
###### text to translate ######
###############################

# Population
# YoY change
# Data: U.S. Census Bureau IDB | Graphic: mazamascience.com
# growth since 2000
# decline since 2000
# million
# thousand
# millions
# thousands

# Country
# Group
# IDB Population Databrowser
# Group
# Select a country

# North America
# Central America
# Caribbean
# South America
# Europe
# Middle East
# North Africa
# Central Africa
# Southern Africa
# South Asia
# Southeast Asia
# East Asia
# Australasia

##########################
###### region codes ######
##########################

# # north america
# "US,CA,MX"
# # central america
# "BZ,CR,GT,HN,NI,PA,SV "
# # caribbean
# "AG,CU,DM,DO,GP,HT,JM,LC,MQ,PR,TT"
# # south america
# "AG,AR,BO,BR,CL,CO,EC,GF,GY,PE,SR,UY,VE"
# # europe
# "AL,BA,BG,DK,IE,AT,CZ,FI,FR,DE,GR,HR,HU,IS,IT,LV,BY,LT,SK,LI,MK,BE,ME,NL,NO,PL,PT,RO,RU,RS,SI,ES,SE,CH,TR,GB,UA,EE"
# # middle east
# "AE,BH,IL,IR,IQ,JO,KW,LB,OM,PS,QA,SA,SY,YE"
# # north africa
# "DZ,EG,LY,MA,TN,EH"
# # central africa
# "CG,CD,NG,RW,SN,SL,SO,SD,TZ,UG,BJ,BI,CM,TD,CF,GQ,ER,ET,GM,GA,GH,GN,CI,KE,LR,ML,MR,NE"
# # southern africa
# "AO,BW,LS,MG,MW,MZ,NA,SZ,ZA,ZM,ZW"
# # south asia
# "AF,BD,BT,IN,LK,NP,PK"
# # southeast asia
# "BN,MM,KH,LA,MY,PH,SG,TH,VN,ID"
# # east asia
# "CN,JP,KP,KR,HK,TW"
# # australasia
# "AU,NC,NZ"

