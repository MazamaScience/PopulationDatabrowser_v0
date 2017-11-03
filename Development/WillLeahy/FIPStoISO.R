### This is the initial script for converting FIPS codes to ISO. The final version is in the data directory

convertCountryCode <- function(countryCode){
  fips2iso <- read.csv("fips2iso.csv", sep=';')
  
  #find index of give fips code
  fipsMask <- fips2iso$fips == countryCode

  #return iso form of country code
  return(fips2iso$iso[fipsMask])
}
