# A first look at R and population data
#install.packages("reshape2")

library("reshape2")

setwd("~/PopulationDatabrowser/Development/WillLeahy")

dfInit <- read.table("../../StaticData/IDB_Dataset/IDBext001.txt", sep="|")

#give the columns appropriate names
names(dfInit) <- c("countryCode", "year", "population")

# "melt" the data frame into long-format data
molten <- melt(data=df, id.vars = c("countryCode", "year"), measured.vars="population")

# "cast" the data frame into wide-format data with "countryCode" columnnames and "year" rownames
table <- dcast(meltdf, year ~ countryCode)

# save table as a csv fle
write.csv(file="IDVtext001.csv", x=table)

#function which plots population data associated with infoList$counryCode as a function of year
populationTimeseriesPlot = function(datalist, infoList, textList){
  
}

futureMask <- table$year > 2014

plot(table$year, table$UK, type="l")
lines(table$year[futureMask], table$UK[futureMask], type="l", lw=4, col='red')
plot(table$year, table$CH, type="l", lwd=4, col="blue")



