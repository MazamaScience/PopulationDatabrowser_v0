########################################################################
# textList_en.R
#
# English language text strings.
#
# Author: Jonathan Callahan
########################################################################

createTextList <- function(dataList, infoList) {
  
  ########################################
  # Create context dependent text strings
  ########################################
  
  # All language strings are defined in the UTF8-encoded language.json file
  # in the element named "rtxt".  This file is generated with
  # create_language_list.py

  jsonFile <- paste(infoList$dataDir, "language.json", sep='')
  jsonList <- fromJSON(jsonFile, encoding="UTF8")
  rtxt <- jsonList[[infoList$language]]$rtxt
  textList <- as.list(rtxt)

  # TODO:  Is there a way to obtain countryName from language.json?

  # The countryName currently comes in with the request.
  textList$countryName <- infoList$countryName
  
  return(textList)
}
