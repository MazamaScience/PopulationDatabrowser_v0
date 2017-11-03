### This is the development file for the PoplationPlot.R that will be a part of the actual databrowser.

#########################
### required packages ###
#########################

### install packages if need be
# install.packages("stringr")
# install.packages("RJSONIO")

library(stringr)
library(RJSONIO)

###############################################################
### select a language and country or countries              ###
### separate multiple countries with commas e.g. "US,CA,MX" ###
###############################################################

language = "en"
country = "US"

###########################
### plotting parameters ###
###########################

infoList <- list(responseType = 'json', plotWidth = '500', language = language, 
                   countryCode = infoList$countryCode = strsplit(country, ",")[[1]],
                   countryTitle = "France", plotType = 'PopulationPlot', projection = T)

####################################################
### list with plot labels in different languages ###
####################################################

json_file <- "./language.json"
json_data <- fromJSON(json_file, encoding="UTF8")
rtxt <- json_data[[infoList$language]]$rtxt

textList <- list(main_title = paste(infoList$countryTitle, ":", sep=''),
                 ylab1 = rtxt[["ylab1"]],
                 ylab2 = rtxt[["ylab2"]],
                 subtitle = rtxt[["subtitle"]],
                 growth = rtxt[["growth"]],
                 decline = rtxt[["decline"]],
                 million = rtxt[["million"]],
                 thousand = rtxt[["thousand"]],
                 millions = rtxt[["millions"]],
                 thousands = rtxt[["thousands"]],
                 population = rtxt[["population"]])

#######################
### population data ###
#######################

df = read.csv("MidYearPop.csv")

###################
### make figure ###
###################

png('populationOverTime.png', width = 550, height = 550)
populationOverTime()
dev.off()