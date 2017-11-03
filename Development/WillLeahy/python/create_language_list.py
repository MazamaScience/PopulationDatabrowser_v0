#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# ISO 3166 arrangement of countries into regions

import sys
from babel import Locale
import json
from collections import OrderedDict


##############################################################
###### functions for making list and dictionary objects ######
##############################################################

def makeList( keys, values):
	tempList = []
	for key, value in zip(keys, values):
		tempDict = {}
		tempDict["code"] = key
		tempDict["name"] = value
		tempList.append(tempDict)
	return tempList

def makeDict( keys, values):
	tempDict = OrderedDict([])
	for key, value in zip(keys, values):
		tempDict[key] = value
	return tempDict


######################################################
###### english titles for R and JS to reference ######
######################################################

rtxt_titles = ["population", "ylab1", "ylab2", "subtitle", "growth", "decline", "million", "thousand", "millions", "thousands"]
html_titles = ["country", "group", "header", "select_country"]

#######################
###### ISO codes ######
#######################

class Flag:
	def __init__(self,flag,language):
		self.flag = flag
		self.language = language

def makeFlag(language_codes, flag_codes, language_names):
	tempDict = OrderedDict([])
	for code, flag, name in zip(language_codes, flag_codes, language_names):
		tempDict[code] = Flag(flag, name)
	return tempDict

language_codes = ['en', 'de', 'fr', 'es', 'it', 'ru', 'tr']

flag_codes = ['US', 'DE', 'FR', 'ES', 'IT', 'RU', 'TR']

language_names = ['English','Deutsch','français', 'español', 'italiano', 'русский', 'Türk']

flags = makeFlag(language_codes, flag_codes, language_names)

region_codes = [
                # North America
                "US,CA,MX",
                # Central America
                "BZ,CR,GT,HN,NI,PA,SV",
                # Caribbean minus GP, MQ
                "AG,AW,CU,DM,DO,HT,JM,LC,PR,TT",
                # South America minus GF
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
		self.country_names = makeList(country_codes, codes)


################################################################
###### create language objects and store them in an array ######
################################################################

en = Language('en', makeDict(rtxt_titles, ["Population 2014","Population","Annual change","Data: U.S. Census Bureau IDB | Graphic: mazamascience.com","99% growth since 2000","99% decline since 2000","million","thousand","millions","thousands"]), makeDict(html_titles, ["Country","Group","Population Databrowser","Select a country"]), makeList(region_codes, ["North America","Central America","Caribbean","South America","Europe","European Union","Former Soviet Union","Middle East","North Africa","Sub-Saharan Africa","OECD","OPEC"]))

de = Language('de', makeDict(rtxt_titles, ["Bevölkerung 2014", "Bevölkerung", "Veränderung gegenüber Vorjahr", "Daten: US Census Bureau IDB | Grafik: mazamascience.com", "99% Wachstum seit 2000", "99% Rückgang seit 2000:", "Millionen", "Tausend", "Millionen", "Tausende"]), makeDict(html_titles, ["Land", "Gruppe", "Databrowser Bevölkerung", "Wählen Sie ein Land"]), makeList(region_codes, ["Nordamerika", "Zentralamerika", "Karibik", "Südamerika", "Europa", "Europäische Union", "ehemalige Sowjetunion", "Nahost", "Nordafrika", "Afrika südlich der Sahara", "OECD", "OPEC"]))

fr = Language('fr', makeDict(rtxt_titles, ["Population 2014", "Population", "Variation annuelle", "Données: US Census Bureau BID | Graphique: mazamascience.com", "Croissance de 99% depuis 2000", "99% de déclin depuis 2000", "million", "mille", "millions", "milliers"]), makeDict(html_titles, ["Pays", "Groupe", "Population Databrowser", "Sélectionnez un pays"]), makeList(region_codes, ["Amérique du Nord", "Amérique centrale", "Caraïbes"," Amérique du Sud","Europe","l'Union européenne","ex-Union soviétique","Moyen-Orient","Afrique du Nord","l'Afrique sub-saharienne","OCDE","OPEP"]))

es = Language('es', makeDict(rtxt_titles, ["Población 2014", "Población", "Variación anual", "Datos: Censo de los EE.UU. Oficina del BID | Gráfico: mazamascience.com", "Crecimiento del 99% desde el año 2000", "99% de disminución desde el año 2000:" , "millones", "mil", "millones", "miles"]), makeDict(html_titles, ["País", "Grupo", "Población Databrowser", "Seleccione un país"]), makeList(region_codes, ["América del Norte", "América Central", "Caribe", "América del Sur", "Europa", "Unión Europea", "ex Unión Soviética", "Oriente Medio", "África del Norte", "África subsahariana", "OCDE", "La OPEP"]))

it = Language('it', makeDict(rtxt_titles, ["Popolazione 2014", "Popolazione", "Variazione annuale", "Data: US Census Bureau IDB | Graphic: mazamascience.com", "Il 99% di crescita dal 2000", "99% in calo dal 2000:" , "milioni", "mille", "milioni", "migliaia"]), makeDict(html_titles, ["Paese", "Gruppo", "Population Databrowser", "Scegliere un paese"]), makeList(region_codes, ["America del Nord", "America centrale", "Caraibi", "Sud America", "Europa", "Unione europea", "Ex Unione Sovietica", "Medio Oriente", "Africa del Nord", "Africa sub-sahariana", "OCSE", "OPEC"]))

ru = Language('ru', makeDict(rtxt_titles, ["Население 2014", "Население", "Годовое изменение", "данных: Бюро переписи населения США ИБР | Графический: mazamascience.com", "99%-ный рост с 2000 года", "99%-ное снижение с 2000 года:" , "миллион", "тысяча", "миллионы", "тысячи"]), makeDict(html_titles, ["Страна", "Группа", "Население Databrowser", "Выберите страну"]), makeList(region_codes, ["Северная Америка", "Центральная Америка", "карибский", "Южная Америка", "Европа", "Европейский Союз", "бывший Советский Союз", "Ближний Восток", "Северная Африка", "К югу от Сахары", "ОЭСР", "ОПЕК"])) 

tr = Language('tr', makeDict(rtxt_titles, ["Nüfus 2014", "Nüfus", "Yıllık değişim", "Veri: US Census Bureau IDB | Grafik: mazamascience.com", "2000 yılından bu yana% 99 büyüme", "2000 yılından bu yana% 99 düşüş:" , "milyon", "bin", "milyon", "binlerce"]), makeDict(html_titles, ["Ülke", "Grup", "Nüfus DataBrowser", "bir ülke seçin"]), makeList(region_codes, ["Kuzey Amerika", "Orta Amerika", "Karayip", "Güney Amerika", "Avrupa", "Avrupa Birliği", "Eski Sovyetler Birliği", "Ortadoğu", "Kuzey Afrika", "Sahraaltı Afrika", "OECD", "OPEC"]))

test = OrderedDict([("flags",flags), ("en",en), ("de",de), ("fr",fr), ("es",es), ("it",it), ("ru",ru), ("tr",tr)])

# foo = u'Δ, Й, ק, ‎ م, ๗, あ, 叶, 葉, and 말.'
# f = open('./unicodeTest.txt', 'w')
# f.write(foo.encode('utf8'))
# f.close()

jsonFile = open('./language.json', 'w')

jsonFile.write(json.dumps(test, default=lambda o: o.__dict__, indent = 4).encode('utf8'))

jsonFile.close()


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

