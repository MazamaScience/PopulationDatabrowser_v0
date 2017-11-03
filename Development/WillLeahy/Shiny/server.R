library(shiny)
library(datasets)
library(RColorBrewer)

# Read in CSV of country code populations
df = read.csv("MidYearPop.csv")

# Define server logic required to plot populations
shinyServer(function(input, output) {
  
  # Compute the text in a reactive expression
  plotText <- reactive({
    labels <- list("main"=paste("Total Midyear Population: ", input$countryCode),
                   "x"="Year", "y"="Population")
    return(labels)
  })
  
  # Get the country code from the UI. Reads the countryCode from input
  # and strips the string into a list of country Codes.
  countryCode <- reactive({
    return(strsplit(input$countryCode, ",")[[1]])
  })
  
  # Create a mask to show/hide projected populations
  projMask <- reactive({
    if (!input$projection){
      projMask <- df$year < 2014
    } else if (input$projection){
      projMask <- df$year > 0
    }
    return(projMask)
  })
  
  # Find the cumulative population each time the user changes a field.
  popMax <- reactive({
    popMax <- 0
    for(code in countryCode()){
      popMax <- popMax + max(df[,code][projMask()])
    }
    return(popMax)
  })

  # Generate a plot of the requested variable against mpg and only 
  # include outliers if requested
  output$populationPlot <- renderPlot({
    
    # Create a vector of colors from the RColorBrewer package
    colors <- brewer.pal(length(countryCode), "Blues")
    
    # Call reactive functions to define plot parameters
    labels <- plotText()
    mask <- projMask()
    codes <- countryCode()
    yrange <- range(0, popMax())
    
    # These values are needed to create a polygon that mimics a 
    # stair plot
    x <- df$year[mask]
    y <- df[,codes[1]][mask]
    y2 <- rep(y, each=2)
    y2 <- y2[-length(y2)]
    x2 <- rep(x, each=2)[-1]
    finalX <- c(min(x2), x2, max(x2))
    finalY <- c(0,y2,0)
    
    # make blank plot for polygons
    plot(x, y, type='n',
         main=labels$main, 
         axes=FALSE, ylab=NA, xlab=NA,
         ylim=yrange,
         frame.plot=TRUE)
    
    # draw new axes
    Axis(side=1, labels=TRUE)
    Axis(side=2, labels=TRUE)
    Axis(side=3, labels=FALSE)
    Axis(side=4, labels=FALSE)
    
    # write axis labels
    mtext(labels$x, side = 1, line = 2, cex = 1.2)
    mtext(labels$y, side = 2, line = 2, cex = 1.2)
    
    # draw the first polygon
    polygon(finalX,finalY, col=colors[1], border=NA)
    
    # check if there are multiple countries to plot
    if(length(codes) > 1) {
      
      # plot the remaining countryCodes
      for (i in 2:length(codes)){   
        
        # These values are needed to create a polygon that mimics a 
        # stair plot
        y <- df[,codes[i]][mask]
        y2 <- rep(y, each=2)
        y2 <- y2[-length(y2)]
        y3 <- c(0,y2,0)
        
        polygon(c(finalX,rev(finalX)), c(finalY,rev(finalY + y3)), col=colors[i], border=NA)
        
        # update finalY so the next polygon starts at the top
        finalY = finalY + y3
        
      }
    }
    
    # create legend
    legend('topleft',codes, pch = 20, col=colors)
    
  })
})

