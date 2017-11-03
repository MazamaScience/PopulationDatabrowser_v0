#List of information from user interface
createInfoList <- function(){
  list(countryCode="UK")
}
infoList <- createInfoList()

#List of text used for plotting
createTextList <- function(infoList) {

  country <- infoList$countryCode
  
  # Create textList
  text <- list(title=paste0("Population (", country, ")"), xlab="Year", ylab="Population (millions)")

  return(text)
}
textList <- createTextList(infoList)

#List of data objects
createDataList <- function() {
  
  dfInit <- read.table("../../StaticData/IDB_Dataset/IDBext001.txt", sep="|")
  
  #assign meaningful names to the dataframe
  names(dfInit) <- c("countryCode", "year", "population")
  
  # "melt" the data frame into long-format data
  molten <- melt(data=dfInit, id.vars = c("countryCode", "year"), measured.vars="population")
  
  # "cast" the data frame into wide-format data
  df <- dcast(molten, year ~ countryCode)
  
  # Create dataList
  data <- list(df)
  
  return(data)
}
dataList <- createDataList()


# plot the specified country
popPlot <- function(dataList, infoList, textList){
  plot(df$year, df[,infoList$countryCode] / 1000000, type='l', xlab=textList$xlab, ylab=textList$ylab, main=textList$title)
}
