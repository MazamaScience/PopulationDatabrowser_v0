### This is the development file for the PoplationPlot.R that will be a part of the actual databrowser.

#List of information from user interface
createInfoList <- function(){
  return (list(responseType = 'json', plotWidth = '500', language = 'en', 
               countryCode = 'AF', countryTitle = "Afganistan", plotType = 'PopulationPlot', projection = "F"))
}
infoList <- createInfoList()


#List of text used for plotting
createTextList <- function(infoList) {
  
  country <- infoList$countryCode
  
  # Create textList
  text <- list(title=paste0("Midyear Population: ", infoList$countryTitle), xlab="Year", ylab="Population (millions)",
               attribution="Data: US Census Bureau IDB    Graphic: mazamascience.com", popChange="YoY change")
  
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

mar <- c(5,4,4,4) + 0.1 # default is c(5,4,4,2)+0.1
par(mar=mar)

df = dataList[[1]]







#########################################
### style section
#########################################

lineWidth <- 1 #width of standard plot
axisSize <- 0.8 # cex of numbers on axes
axisLine <-0.3 # distance of axes from plot
labSize <- 0.9 # text size of axis labels
labLine <- 2.2 # distance of labels from plot
tick <- -0.016 # width of axis ticks
gridWidth <- 1 # width of gridlines
#colors <- brewer.pal(length(countryCodes), "Blues")



#########################################
### function that makes the population plot
#########################################

popPlot <- function(dataList, infoList, textList){
  
  ### create a mask to hide projected population
  if (infoList$projection == "F"){
    projMask <- df$year <= 2014
  } else if (infoList$projection == "T"){
    projMask <- df$year > 0
  }
  
  years <- df$year[projMask]
  txt <- textList
  
  ### if there are multiple country codes add their populations
  if(length(infoList$countryCode)>1){
    population <- apply(df[,infoList$countryCode], 1, sum)[projMask]
  } else {
    population <- df[,infoList$countryCode][projMask]
  }
  
  ### find maximum population
  pMax <- max(population)
  
  ### adjust labels and population if max population is over/under 1,000,000
  if(pMax < 1000000){
    txt$ylab <- "Population (thousands)"
    txt$millions <- paste0(round(pMax/1000, digits=1), "\nthousand")
    population <- population / 1000
    pMax <- pMax / 1000
  } else if(pMax > 1000000){
    txt$millions <- paste0(round(pMax/1000000, digits=1), "\nmillion")
    population <- population / 1000000
    pMax <- pMax / 1000000  
  }
  
  ### find growth for subtitle
  oldPop <- population[match(2000, years)]
  currentPop <- population[match(2014, years)]
  percentGrowth <- round(100 * (currentPop - oldPop) / oldPop, digits=0)
  txt$subtitle <- paste0(percentGrowth, "% growth since 2000")

  #########################################
  ### change in population per year barplot
  #########################################

  par(fig=c(0,1,0,0.4), yaxs='i', xaxs='i', new=TRUE, lty=0, mgp = c(0, 0.5, 0))
  
  ### calculate the percentage change from year to year
  y <- diff(population)
  y <- c(0, y)
  percentChange <- 100 * y/population

  ###for different colored bars
  col1 <- '#5fbf85'
  col2 <- '#cb615b'
  barColors <- c()
  for(i in percentChange){
    if(i > 0){
      barColors <- c(barColors, col1)
    } else {
      barColors <- c(barColors, col2)
    }
  }
  
  ### make solid barplot of population change
  barplot(percentChange, space=0, axes=FALSE,
          xlab=NA, ylab=NA, border=FALSE, col=barColors,
          main=NA, ylim=range(0, 4))
  
  grid(NA, NULL, col='white', lwd=gridWidth)
  
  ### draw axes
  axis(side=4, line=axisLine, lwd.ticks=0, labels=FALSE)
  axis(side=4, las=1, lwd=0, at=c(0,1,2,3,4), labels=c("0%", "", "2%", "", "4%"), lwd.ticks=1, cex.axis=axisSize, line=axisLine, tck=tick*3)
  
  ### draw axis label
  mtext(txt$popChange, side=4, cex=labSize, at=2, line=labLine)
  
  #########################################
  ### population over time line plot
  #########################################
  
  par(fig=c(0,1,0,1), yaxs='i', xaxs='i', new=TRUE, lty=1)
  
  ### plot population
  plot(years, population, type='s', xlab=NA, ylab=NA, axes=FALSE,
       main=NA, lwd=lineWidth,
       ylim=range(0, pMax))
  
  ### millions text at end of plot line
  mtext(txt$millions, cex=labSize, side=4, las=1, at=population[match(years[length(years)], years)], line=0.2, font=2)
  
  ### draw axes
  axis(side=1, at=c(min(years), max(years)), labels=FALSE, line=axisLine, lwd.ticks=0)
  axis(side=1, cex.axis=axisSize, lwd=0, lwd.ticks=1, line=axisLine, tck=tick)
  axis(side=2, at=c(0,pMax), labels=FALSE, line=axisLine, lwd.ticks=0)
  axis(side=2, cex.axis=axisSize, line=axisLine, lwd=0, lwd.ticks=1, tck=tick, las=1)
  
  ### axis label text
  mtext(txt$xlab, side=1, cex=labSize, line=labLine)
  mtext(txt$ylab, side=2, cex=labSize, line=labLine)
  
  ### draw main text and subtitle text
  mtext(txt$title, side=3, cex=labSize*1.5, line=labLine-0.5)
  mtext(txt$subtitle, side=3, cex=labSize*1.3, line=labLine - 1.8, font=3)

  # draw ablines up until the population line
  for(i in seq(1960,2040,by=10)){
    segments(i, 0, i, population[match(i, years)], col=rgb(0.6,0.6,0.6), lwd=gridWidth, lty=3)
  }
  
  # plot information at bottom
  title(sub=txt$attribution,line=4,family='Times')
  
}

popPlot(dataList, infoList, textList)