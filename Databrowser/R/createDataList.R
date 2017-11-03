########################################################################
# createDataList.R
#
# Databrowser specific creation of dataframes for inclusion in dataList.
#
# Author: Jonathan Callahan
########################################################################

createDataList <- function(infoList){

  # Read in the MidYearPop.csv file created by convertMidYearPop.R
  midYearPop = read.csv(paste(infoList$dataDir,'/MidYearPop.csv', sep=''))
  
  # Read in the estimateUpdate.csv file
  estimateUpdateYears = read.csv(paste(infoList$dataDir,'/estimateUpdateYears.csv', sep=''))

  # NOTE:  The estimateUpdateYers.csv file is organized for ease of human editing.
  # NOTE:  It should be modified based on the release notes whenever a new version
  # NOTE:  of the US Census Bureau IDB dataset is released.
  # NOTE:
  # NOTE:    http://www.census.gov/population/international/data/idb/rel_notes.php
  # NOTE:
  # NOTE:  The next three lines drop the 'countryName' column and then reorganize
  # NOTE:  the dataframe to have countryId as columns instead of rows. This then 
  # NOTE:  matches the organization of the midYearPop dataframe.
  estimateUpdateYears <- subset(estimateUpdateYears, select = -c(countryName))
  molten = melt(estimateUpdateYears, id.vars = "countryCode")
  estimateUpdateYears = dcast(molten, variable ~ countryCode)
  
  # Create dataList
  dataList <- list(midYearPop=midYearPop,
                   estimateUpdateYears=estimateUpdateYears)

  return(dataList)
  
}

