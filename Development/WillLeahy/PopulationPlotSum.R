### This is the development file for the PoplationPlot.R that will be a part of the actual databrowser.

#List of information from user interface
createInfoList <- function(){
  
  infoList <- list(responseType = 'json', plotWidth = '500', language = 'en', countryCode = "CA,MX,FR", 
                   plotType = 'TrigFunctions', lineColor = 'black', debug = 'none', cycles = '3', projection="F")
  infoList$countryCode = strsplit(infoList$countryCode, ",")[[1]]
  
  return(infoList)
}
infoList <- createInfoList()


#List of text used for plotting
createTextList <- function(infoList) {
  
  country <- infoList$countryCode
  
  # Create textList
  text <- list(title="Total Midyear Population", xlab="Year", ylab="Population (millions)")
  
  return(text)
}
textList <- createTextList(infoList)

#List of data objects
createDataList <- function() {
  
  df = read.csv("MidYearPop.csv")
  
  # Create dataList
  data <- list(df)
  
  return(data)
}
dataList <- createDataList()



df = dataList[[1]]

mar <- c(2, 2, 2, 1) + 0.1 # default is c(5,4,4,2)+0.1
par(mar=mar)




require(RColorBrewer)

#function that makes the population plot
popPlot <- function(dataList, infoList, textList){
  
  codes = infoList$countryCode
  projection = infoList$projection
  yrange = 
  
  ### create a vector of colors from the RColorBrewer package
  colors <- brewer.pal(length(countryCodes), "Blues")
  
  ### create a mask to hide projected population
  if (infoList$projection == "F"){
    projMask <- df$year < 2014
  } else if (infoList$projection == "T"){
    projMask <- df$year > 0
  }
  
  ###
  ### first plot, total mid year population over time
  ###
  
  ### find maximum population
  popMax <- function(codes)
  popMax <- 0
  for(code in countryCodes){
    popMax <- popMax + max(df[,code][projMask])
  }
  return(popMax)
  
  ### these create vectors that allow the polygon command to simulate stair step lines
  y <- df[,countryCodes[[1]]][projMask] / 1000000
  x <- df$year[projMask]
  y2 <- rep(y, each=2)
  y2 <- y2[-length(y2)]
  x2 <- rep(x, each=2)[-1]
  finalX <- c(min(x2), x2, max(x2))
  finalY <- c(0,y2,0)  ### finalY is updated to be the top of the plot after each new polygon is drawn
  
  ### empty plot for polygons
  plot(x, y, type='n',
       main=textList$title, 
       axes=FALSE,
       ylim=range(0, popMax),
       frame.plot=TRUE)
  
  ### draw axes
  Axis(side=1, labels=TRUE)
  Axis(side=2, labels=TRUE)
  Axis(side=3, labels=FALSE)
  Axis(side=4, labels=FALSE)
  
  ### draw the first polygon
  polygon(finalX,finalY, col=colors[1], border=NA)
  
  ### draw the rest of the polygons
  if(length(countryCodes) > 1) {
    # plot the remaining countryCodes
    for (i in 2:length(countryCodes)){   
      
      ### these create vectors that allow the polygon command to simulate stair step lines
      y <- df[,countryCodes[i]][projMask] / 1000000
      y2 <- rep(y, each=2)
      y2 <- y2[-length(y2)]
      y3 <- c(0,y2,0)
      
      polygon(c(finalX,rev(finalX)), c(finalY,rev(finalY + y3)), col=colors[i], border=NA)
      
      ### update finalY so the next polygon starts at the top
      finalY = finalY + y3
      
    }
  }
  
}

popPlot(dataList, infoList, textList)