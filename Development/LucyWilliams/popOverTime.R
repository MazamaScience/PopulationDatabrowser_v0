# population over time plots

df <- read.table("/Users/lucy/Desktop/IDBext001.txt", sep="|")

# give the columns useful names
names(df) <- c("countryCode", "year", "population")

# "melt" the data frame so that it's ready to be cast
moltendf <- melt(data=df, id.vars = c("countryCode", "year"), measured.vars="population")

# cast the data frame to a table using the formula rows ~ columns
table <- dcast(moltendf, year ~ countryCode)

# takes a recast table of population data as a function of year and countryCode
popOverTime <- function(table, country) {
  color <- rainbow(length(country))
  par(mar=c(5.1,4.1,4.1,2.8))
  
  # find max ylim (kinda ugly right now)
  ylim <- findMax(table,country)
  
  # plot first country
  countryIndex <- which(names(table)==country[1])
  # plot year on x-axis and country's population on y-axis
  plot(table$year, table[[countryIndex]], type="l", lwd=3,
       ylab="", xlab="", las=1, col=color[1],
       ylim=c(0,ylim),
       main="Mid-Year Population, 1950-2050")
  box()
  mtext(paste(" ", country[1]), las=1, side=4, at=table[[countryIndex]][101])
  
  
  # plot all other countries
  for (index in seq(2,length(country),1)) {
    countryIndex <- which(names(table)==country[index])
    points(table$year, table[[countryIndex]], type="l", lwd=3, col=color[index])
    # label at height of 2050 population, outside RHS margin
    mtext(paste(" ", country[index]), las=1, side=4, at=table[[countryIndex]][101])
  }
  
}

overTimeWithPyramids <- function(table,country) {
  
  # plot over time
  popOverTime(table,country)
  ymax <- findMax(table,country)
  
  par(new=TRUE, fig=c(1960))
  
  
  
}

findMax <- function(table, country) {
  ylim <- 0
  fipsList <- names(table)
  for (index in seq(1,length(country),1)) {
    countryIndex <- which(fipsList==country[index])
    populations <- table[[countryIndex]]
    maxPop <- max(populations)
    ylim <- max(maxPop,ylim)
  }
  return(ylim)
}