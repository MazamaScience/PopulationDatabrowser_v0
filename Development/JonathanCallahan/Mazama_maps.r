############################################################
# country_map
#
# Plots a map in which individual nations may be colored independently.
#
#   countries   array of identifiers for countries within a group (some may be non-ISO2 e.g. 'BP_FSU')
#   col         array of colors to associate with each identifier
#   view        identifier for the named view ('auto' pickes the best view for a single country)
#   resolution  hi/lo resolution dataset to use (hi|lo)
#   axes        plot axes (TRUE|FALSE)
#
# TODO:  Add more information about the source of the map data
#
# Uses the sp package and works with geodata such as the world outlines described here:
#   http://markmail.org/thread/jhmvmuvslzxemgyl

country_map <- function(data,info,text) {

  world_countries = data$world_countries

  countries = info$countries
  col = info$col
  view = 'auto'
  resolution = 'lo'
  axes = ifelse(is.null(info$axes),FALSE,info$axes)

  ########################################
  # Invoke script with shared color definitions
  ########################################

  r_script = paste(info$script_dir,'shared_colors.r',sep='')
  source(r_script,local=TRUE)

  ########################################
  # Define different views that will be used in the creation of maps
  ########################################
 
  north_america = c('CA','MX','US')
  # CA  Canada
  # MX  Mexico
  # US  United States

  central_america = c('BZ','CR','GT','HN','NI','PA','SV')
  # BZ  Belize
  # CR  Costa Rica
  # GT  Guatemala
  # HN  Honduras
  # NI  Nicaragua
  # PA  Panama
  # SV  El Salvador

  caribbean = c('AG','CU','DM','DO','GP','HT','JM','LC','MQ','PR','TT')
  # AG  Antigua and Barbuda
  # CU  Cuba
  # DM  Dominica
  # DO  Dominican Republic
  # GP  Guadeloupe
  # HT  Haiti
  # JM  Jamaica
  # LC  Saint Lucia
  # MQ  Martinique
  # PR  Puerto Rico
  # TT  Trinidad and Tobago

  south_america = c('AG','AR','BO','BR','CL','CO','EC','GF','GY','PE','SR','UY','VE')
  # AG  Antigua and Barbuda
  # AR  Argentina
  # BO  Bolivia
  # BR  Brazil
  # CL  Chile
  # CO  Colombia
  # EC  Ecuador
  # GF  French Guiana
  # GY  Guyana
  # PE  Peru
  # SR  Suriname
  # UY  Uruguay
  # VE  Venezuela
  
  europe = c('AL','BA','BG','DK','IE','AT','CZ','FI','FR','DE','GR','HR','HU',
             'IS','IT','LV','BY','LT','SK','LI','MK','BE','ME','NL','NO','PL','PT',
             'RO','RU','RS','SI','ES','SE','CH','TR','GB','UA','EE')
  # AL  Albania
  # BA  Bosnia and Herzegovina
  # BG  Bulgaria
  # DK  Denmark
  # IE  Ireland
  # AT  Austria
  # CZ  Czech Republic
  # FI  Finland
  # FR  France
  # DE  Germany
  # GR  Greece
  # HR  Croatia
  # HU  Hungary
  # IS  Iceland
  # IT  Italy
  # LV  Latvia
  # BY  Belarus
  # LT  Lithuania
  # SK  Slovakia
  # LI  Liechtenstein
  # MK  The former Yugoslav Republic of Macedonia
  # BE  Belgium
  # ME  Montenegro
  # NL  Netherlands
  # NO  Norway
  # PL  Poland
  # PT  Portugal
  # RO  Romania
  # RU  Russia
  # RS  Serbia
  # SI  Slovenia
  # ES  Spain
  # SE  Sweden
  # CH  Switzerland
  # TR  Turkey
  # GB  United Kingdom
  # UA  Ukraine
  # EE  Estonia

  middle_east = c('AE','BH','IL','IR','IQ','JO','KW','LB','OM','PS','QA','SA','SY','YE')
  # AE  Untied Arab Emirates
  # BH  Bahrain
  # IL  Israel
  # IR  Iran (Islamic Republic of)
  # IQ  Iraq
  # JO  Jordan
  # KW  Kuwait
  # LB  Lebanon
  # OM  Oman
  # PS  Palestine
  # QA  Qatar
  # SA  Saudi Arabia
  # SY  Syrian Arab Republic
  # YE  Yemen

  north_africa = c('DZ','EG','LY','MA','TN','EH')
  # DZ  Algeria
  # EG  Egypt
  # LY  Libyan Arab Jamahiriya
  # MA  Morocco
  # TN  Tunisia
  # EH  Western Sahara

  central_africa = c('CG','CD','NG','RW','SN','SL','SO','SD','TZ','UG','BJ','BI','CM','TD',
                     'CF','GQ','ER','ET','GM','GA','GH','GN','CI','KE','LR','ML','MR','NE')
  # CG  Congo
  # CD  Democratic Republic of the Congo
  # NG  Nigeria
  # RW  Rwanda
  # SN  Senegal
  # SL  Sierra Leone
  # SO  Somalia
  # SD  Sudan
  # TZ  United Republic of Tanzania
  # UG  Uganda
  # BJ  Benin
  # BI  Burundi
  # CM  Cameroon
  # TD  Chad
  # CF  Central African Republic
  # GQ  Equatorial Guinea
  # ER  Eritrea
  # ET  Ethiopia
  # GM  Gambia
  # GA  Gabon
  # GH  Ghana
  # GN  Guinea
  # CI  Cote d'Ivoire
  # KE  Kenya
  # LR  Liberia
  # ML  Mali
  # MR  Mauritania
  # NE  Niger

  southern_africa = c('AO','BW','LS','MG','MW','MZ','NA','SZ','ZA','ZM','ZW')
  # AO  Angola
  # BW  Botswana
  # LS  Lesotho
  # MG  Madagascar
  # MW  Malawi
  # MZ  Mozambique
  # NA  Namibia
  # SZ  Swaziland
  # ZA  South Africa
  # ZM  Zambia
  # ZW  Zimbabwe

  south_asia = c('AF','BD','BT','IN','LK','NP','PK')
  # AF  Afghanistan
  # BD  Bangladesh
  # BT  Bhutan
  # IN  India
  # LK  Sri Lanka
  # NP  Nepal
  # PK  Pakistan

  southeast_asia = c('BN','MM','KH','LA','MY','PH','SG','TH','VN','ID')
  # BN  Brunei Darussalam
  # MM  Burma
  # KH  Cambodia
  # LA  Lao People's Democratic Republic
  # MY  Malaysia
  # PH  Philippines
  # SG  Singapore
  # TH  Thailand
  # VN  Viet Nam
  # ID  Indonesia

  east_asia = c('CN','JP','KP','KR','HK','TW')
  # CN  China
  # JP  Japan
  # KP  Korea, Democratic People's Republic of
  # KR  Korea, Republic of
  # HK  Hong Kong
  # TW  Taiwan

  australasia = c('AU','NC','NZ')
  # AU  Australia
  # NC  New Caledonia
  # NZ  New Zealand

  ########################################
  # BEGIN BP groupings as defined in the Statistical Review

  BELU = c('BE','LU')
  # Belgium, Luxembourg

  FSU = c('AM','AZ','BY','EE','GE','KZ','KG','LV','LT','MD','RU','TJ','TM','UA','UZ')
  # Armenia, Azerbaijan, Belarus, Estonia, Georgia, Kazakhstan, Kyrgyzstan, Latvia, 
  # Lithuania, Moldova, Russian Federation, Tajikistan, Turkmenistan, Ukraine, Uzbekistan

  # OECD members (Organization For Economic Co-operation and Development)
  OECD_EUROPE = c('AT','BE','DZ','DK','FI','FR','DE','GR','HU','IS','IE','IT',
                  'LU','NL','NO','PL','PT','SK','ES','SE','CH','TK','GB')
  # Europe: Austria, Belgium, Czech Republic, Denmark, Finland, France, Germany, Greece, Hungary, Iceland, Republic of Ireland, Italy
  #         Luxembourg, Netherlands, Norway, Poland, Portugal, Slovakia, Spain, Sweden, Switzerland, Turkey, United Kingdom
  OECD_NONEUROPE = c('AU','CA','JP','MX','NZ','KR','US')
  # Other member countries: Australia, Canada, Japan, Mexico, New Zealand, South Korea, USA. 

  OECD = append(OECD_EUROPE, OECD_NONEUROPE)

  EUROPE = append(OECD_EUROPE, c('AL','BA','BG','HR','CY','MK','ME','MT','RO','RS','SI'))
  # Europe:
  # European members of the OECD plus
  # Albania, Bosnia-Herzegovina, Bulgaria, Croatia, Cyprus, Macedonia, Montenegro, [Gibraltar,] Malta, Romania, Serbia, Slovenia.

  EUROPE_EURASIA = append(EUROPE, FSU)
  # Europe and Eurasia:
  # All countries listed above under the headings Europe and the Former Soviet Union 

  EU = c('AT','BE','BG','CY','CZ','DK','EE','FI','FR','DE','GR','HU',
         'IE','IT','LV','LT','LU','MT','NL','PL','PT','RO','SK','SI','ES','SE','GB')
  # European Union members 
  # Austria, Belgium, Bulgaria, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece,  Hungary, 
  # Republic of Ireland, Italy, Latvia, Lithuania, Luxembourg, Malta, Netherlands, Poland, Portugal, Romania, Slovakia, 
  # Slovenia, Spain, Sweden, UK. 

  OSCA = c('BZ','CR','GT','HN','NI','PA','SV','AG','CU','DM','DO','GP','HT','JM','LC','MQ','PR','TT','AG',
           'GF','GY','PY','SR','UY')
  # central_america, caribbean, French Guyana, Guyana, Paraguay, Suriname, Uraguay

  OEE = c('GL','BE','LU','LV','EE','AL','BA','HR','CY','MK','ME','RS','SI','MD','GE','AM','KG','TJ')
  # Other Europe & Eurasia
  # Belgium, Luxembourg, Latvia, Estonia, Albania, Bosnia-Herzegovina, Croatia, Cyprus, Macedonia, Montenegro, Serbia, Slovenia
  # Moldova, Georgia, Armenia, Kyrgyzstan, Tajikistan

  OME = c('IL','JO','LB')
  # Israel, Jordan, Lebanon

  OAF = c('MA','EH','MR','ML','BF','NE','ER','ET','DJ','SO',
          'SN','GM','GW','GN','SL','LR','CI','GH','TG','BJ',
          'CF','CD','UG','KE','RW','BI',
          'TZ','ZM','NA','BW','MZ','LS','SZ','MG')
  # Morocco, Western Sahara, Mauritania, Mali, Burkina Faso, Niger, [Chad, Sudan,] Eritrea, Ethiopia, Djibouti, Somailia
  # Senegal, Gambia, Guinea-Bissau, Guinea, Sierra-Leone, Liberia, Cote dIvoire, Ghana, Togo, Benin, [Nigeria, Cameroon,]
  # Central African Republic, [Equatorial Guinea, Gabon, Congo (Brazzaville),] DR Congo, Uganda, Kenya, Rwanda, Burundi,
  # Tanzania, Zambia, [Angola,] Namibia, Botswana, [Zimbabwe,] Mozambique, [South Africa,] Lesotho, Swaziland, Madagascar

  OAP = c('AF','KP','MN','NP','BT','BD','LK','LA','KH','PG')
  # Other Asia-Pacific
  # Afghanistan, North Korea, Mongolia, Nepal, Bhutan, Bangladesh, Sri Lanka, [Myanmar,] Laos, Cambodia, Papua-New Guinea

  OPEC10 = c('IR','KW','QA','SA','AE','DZ','LY','NG','ID','VE')
  OPEC = c('IR','IQ','KW','QA','SA','AE','DZ','LY','AO','NG','ID','VE')
  # OPEC members (Organization of the Petroleum Exporting Countries) 
  # Middle East: Iran, Iraq, Kuwait, Qatar, Saudi Arabia, United Arab Emirates. 
  # North Africa: Algeria, Libya. 
  # West Africa: Angola, Nigeria. 
  # Asia Pacific: Indonesia. South America: Venezuela.  

#
#North Africa:
#Territories on the north coast of Africa from Egypt to Western Sahara. 
#
#West Africa:
#Territories on the west coast of Africa from Mauritania to Angola, including Cape Verde, Chad 
#
#East and Southern Africa:
#Territories on the east coast of Africa from Sudan to Republic of South Africa. Also Botswana, Madagascar, Malawi, Namibia, Uganda, Zambia, Zimbabwe. 
#
#Asia Pacific:
#Brunei, Cambodia, China, China Hong Kong SAR*, Indonesia, Japan, Laos, Malaysia, Mongolia, North Korea, Philippines, Singapore, South Asia (Afghanistan, Bangladesh, India, Myanmar, Nepal, Pakistan and Sri Lanka), South Korea, Taiwan, Thailand, Vietnam, Australia, New Zealand, Papua New Guinea and Oceania. 
#*Special Administrative Region
#
#Australasia:
#Australia, New Zealand. 
#
#
#Other EMEs (Emerging Market Economies)
#South and Central America, Africa, Middle East, Non-OECD Asia and Non-OECD Europe. 

  # END BP groupings
  ########################################

  caribbean = c('MX','BZ','CR','GT','HN','NI','PA','SV','AG','CU','DM','DO','GP','HT','JM','LC','MQ','PR','TT','CO','EC','VE')
  # Mexico, central_america, caribbean, Columbia, Ecuador, Venezuela

  scandinavia = c('IS','NO','SE','FI')
  # Iceland, Norway, Sweden, Finland

  northern_europe = c('GB','IE','NL','BE','LU','DE','DK','PL','LT','LV',
                           'EE','CZ','SK','BY')
  # England, Ireland, Netherlands, Belgium, Luxembourg, Germany, Denmark, Poland, Lithuania, Latvia, 
  # Estonia, Czech Rep., Slovakia, Belrus,

  southern_europe = c('PT','ES','FR','IT','LI','CH','AT','HU','SK','HR',
                      'BA','AL','BG','GR','MK','ME','RO','UA','MD','TR')
  # Portugal, Spain, France, Italy, Switzerland, Lichtenstein, Austria, Hungary, Slovakia, Croatia,
  # Bosinia & Herzegovina Albania, Bulgaria, Greece, Macedonia, Montenegro, Romania, Ukraine, Moldova, Turkey

  caspian = c('AM','AZ','GE','KG','TJ','TM','UZ')
  # Armenia, Azerbaijan, Georgia, Kyrgyzstan, Tajikistan, Turkmenistan, Uzbekistan

  if (view == 'auto') {
    # Pick a view that matches the first country
    if (countries[1] %in% north_america) { view = 'north_america' }
    else if (countries[1] %in% central_america) { view='caribbean' }
    else if (countries[1] %in% caribbean) { view='caribbean' }
    else if (countries[1] %in% south_america) { view='south_america' }
    else if (countries[1] %in% scandinavia) { view='scandinavia' }
    else if (countries[1] %in% northern_europe) { view='northern_europe' }
    else if (countries[1] %in% southern_europe) { view='southern_europe' }
    else if (countries[1] %in% caspian) { view='caspian' }
    else if (countries[1] %in% middle_east) { view='middle_east' }
    else if (countries[1] %in% north_africa) { view='north_africa' }
    else if (countries[1] %in% central_africa) { view='central_africa' }
    else if (countries[1] %in% southern_africa) { view='southern_africa' }
    else if (countries[1] %in% south_asia) { view='south_asia' }
    else if (countries[1] %in% east_asia) { view='east_asia' }
    else if (countries[1] %in% southeast_asia) { view='southeast_asia' }
    else if (countries[1] %in% australasia) { view='australasia' }
    # A few more special cases
    else if (countries[1] == 'RU') { view='russia' }
    else if (countries[1] == 'KZ') { view='kazakhstan' }
    else { view='world' }
  }

  # Set the boundaries for the plot (default to global)
  xlim = c(-180,180)
  ylim = c(-55,75)

  if (view == 'world') {
    xlim = c(-170,170)
    ylim = c(-55,75)

  } else if (view == 'north_america') {
    xlim=c(-175,-40)
    ylim=c(15,70)

  } else if (view == 'caribbean') {
    xlim=c(-120,-40)
    ylim=c(-5,35)

  } else if (view == 'south_america') {
    xlim=c(-140,-25)
    ylim=c(-55,10)

  } else if (view == 'scandinavia') {
    xlim=c(-20,30)
    ylim=c(55,70)

  } else if (view == 'europe') {
    xlim=c(-25,60)
    ylim=c(35,65)

  } else if (view == 'northern_europe') {
    xlim=c(-5,25)
    ylim=c(47,61)

  } else if (view == 'southern_europe') {
    xlim=c(-8,42)
    ylim=c(32,53)

  } else if (view == 'caspian') {
    xlim=c(35,65)
    ylim=c(35,52)

  } else if (view == 'middle_east') {
    xlim=c(30,70)
    ylim=c(12,42)

  } else if (view == 'north_africa') {
    xlim=c(-20,60)
    ylim=c(15,45)

  } else if (view == 'central_africa') {
    xlim=c(0,50)
    ylim=c(-15,25)

  } else if (view == 'west_africa') {
    xlim=c(5,25)
    ylim=c(-18,16)

  } else if (view == 'southern_africa') {
    xlim=c(0,50)
    ylim=c(-35,-5)

  } else if (view == 'africa') {
    xlim=c(-20,60)
    ylim=c(-35,40)

  } else if (view == 'east_asia') {
    xlim=c(90,130)
    ylim=c(15,55)

  } else if (view == 'south_asia') {
    xlim=c(60,100)
    ylim=c(5,40)

  } else if (view == 'southeast_asia') {
    xlim=c(90,160)
    ylim=c(-15,25)

  } else if (view == 'australasia') {
    xlim=c(90,180)
    ylim=c(-50,-5)

  } else if (view == 'asia_pacific') {
    xlim=c(60,180)
    ylim=c(-45,50)

  # Special views

  } else if (view == 'russia') {
    xlim=c(20,80)
    ylim=c(35,65)

  } else if (view == 'kazakhstan') {
    xlim=c(40,100)
    ylim=c(35,60)

  } else if (view == 'north_sea') {
    xlim=c(-15,20)
    ylim=c(49,65)

  } else if (view == 'former_soviet_union') {
    xlim=c(-25,90)
    ylim=c(35,65)

  } else if (view == 'opec') {
    xlim=c(-90,150)
    ylim=c(-20,40)

  }

  # Plot the basemap
  plot(world_countries,axes=FALSE,xlim=xlim,ylim=ylim,bg=color_water_map)
  plot(world_countries,add=TRUE,col=c(color_blank_map))

  # Plot each individual country in the appropriate color
  # The 'Other groupings contain countries that are not listed in BP datafiles and therefor colored as 'missing'.
  country_index = 0
  for (ISO2 in countries) {  
    country_index = country_index + 1
    country_color = col[country_index]
    if ( ISO2 == 'BP_BELU' ) {
      plot(world_countries[world_countries$ISO2 %in% BELU,],add=TRUE,col=c(country_color))
    } else if ( ISO2 == 'BP_FSU' ) {
      plot(world_countries[world_countries$ISO2 %in% FSU,],add=TRUE,col=c(country_color))
    } else if ( ISO2 == 'BP_OSCA' ) {
      plot(world_countries[world_countries$ISO2 %in% OSCA,],add=TRUE,col=c(color_missing_map))
    } else if ( ISO2 == 'BP_OEE' ) {
      plot(world_countries[world_countries$ISO2 %in% OEE,],add=TRUE,col=c(color_missing_map))
    } else if ( ISO2 == 'BP_OME' ) {
      plot(world_countries[world_countries$ISO2 %in% OME,],add=TRUE,col=c(color_missing_map))
    } else if ( ISO2 == 'BP_OAF' ) {
      plot(world_countries[world_countries$ISO2 %in% OAF,],add=TRUE,col=c(color_missing_map))
    } else if ( ISO2 == 'BP_OAP' ) {
      plot(world_countries[world_countries$ISO2 %in% OAP,],add=TRUE,col=c(color_missing_map))
    } else {
      plot(world_countries[world_countries$ISO2==ISO2,],add=TRUE,col=c(country_color))
    }
  }

}
