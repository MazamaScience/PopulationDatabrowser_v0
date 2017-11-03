library(shiny)

# Define UI for miles per gallon application
shinyUI(pageWithSidebar(
  
  # Application title
  headerPanel("Population Databrowser"),
  
  # Sidebar with controls to select the variable to plot against mpg
  # and to specify whether outliers should be included
  sidebarPanel(
    selectInput("countryCode", "Select Country:",
                list("United States" = "US", 
                     "Canada" = "CA", 
                     "Mexico" = "MX",
                     "North America" = "US,CA,MX")),
    
    checkboxInput("projection", "Show projections", FALSE)
  ),
  
  # Show the caption and plot of the requested variable against mpg
  mainPanel(
    h3(textOutput("caption")),
    
    plotOutput("populationPlot")
  )
))