#
# This is the user-interface definition of a Shiny web application. You can
# run the application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
# 
#    http://shiny.rstudio.com/
#

library(shiny)
require(shinyjs)

require(RgoogleMaps)
require(leaflet)



shinyUI(fluidPage(
  # Application title
  titlePanel("Maps"),
  sidebarPanel(

  textInput(inputId="dir",label="Direccion (Ej: Calle Mayor, 15, Madrid)",value = " ")
  ),
  actionButton("localizar", "Localizar"),
  
    # Show a plot of the generated distribution
    mainPanel(
      #tableOutput("table"),
      leafletOutput("map")
    ))
      
    )
  



