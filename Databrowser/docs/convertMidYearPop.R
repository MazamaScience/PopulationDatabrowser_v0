# converts data in the IDB dataset from FIPS codes to ISO codes.
# The conversion chart is from http://opengeocode.org/download.php#fips2iso
# isocsv takes two arguments, an old filename and a new filesname. The contents 
# of the first file are reshaped so each column name is a countrycode and then converts
# those from FIPS to ISO amd saves the results as a new csv file.

makePopISO <- function(oldFile, newFile) {
  
  # require reshape2 to melt and cast dataframe
  library("reshape2")
  
  dfInit <- read.table(oldFile, sep="|")
  
  # assign meaningful names to the dataframe
  names(dfInit) <- c("countryCode", "year", "population")
  
  # "melt" the data frame into long-format data
  molten <- melt(data=dfInit, id.vars = c("countryCode", "year"), measured.vars="population")
  
  # "cast" the data frame into wide-format data with country code column names
  df <- dcast(molten, year ~ countryCode)
  
  # get list of FIPS country codes
  fips <- colnames(df)[-1]
  
  # read conversion table of FIPS to ISO
  fips2iso <- read.csv("fips2iso.csv", sep=',', stringsAsFactors = FALSE, header=TRUE)
  
  # function which reads a csv table of FIPS to ISO conversions and converts the given country code accordingly
  convertCountryCode <- function(countryCode){
    # find index of give fips code
    fipsMask <- fips2iso$fips == countryCode
    
    # return iso form of country code
    if(!(any(fipsMask))){ # if the country code doesn't exist
      return ('DROP') 
    } else if(toString(fips2iso$iso[fipsMask]) != ''){ # if there is a direct conversion
      return(toString(fips2iso$iso[fipsMask]))
    } else if (toString(fips2iso$inclusive[fipsMask]) != '') { # if that country is now part of another country
      return(toString(fips2iso$inclusive[fipsMask]))
    } else {
      return('DROP')
    } 
  }

  newColNames <- c()
  
  # replace each FIPS code with the ISO code
  for(i in 1:length(fips)){
    iso <- convertCountryCode(fips[i])  # return iso code and convert to characters
    newColNames <- c(newColNames, iso)
  }
  
  # add 'year' back into column names
  newColNames <- c('year', newColNames)
  
  # attach the new column names to the original dataframe
  colnames(df) <- newColNames
  
  # remove country with no country code for now (kosovo)
  df <- subset(df, select = -c(DROP) )
  
  # combine two palestine populations
  df$PS <- df$PS + df$PS.1
  df <- subset(df, select = -c(PS.1) )
  
  write.csv(df, file=newFile, row.names=FALSE)
}

# test run
oldFile <- 'IDBext001.txt'
newFile <- 'MidYearPop.csv'
makePopISO(oldFile, newFile)

