#
# This is the server logic of a Shiny web application. You can run the 
# application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
# 
#    http://shiny.rstudio.com/
#

library(shiny)
require(RgoogleMaps)
require(leaflet)
library(DT)



# Define server logic required to draw a histogram
shinyServer(function(input, output) {
  
  
  point <- eventReactive(input$localizar, {
    getGeoCode(input$dir)
  })
  
  
  output$map <- renderLeaflet({
    
    # draw the map
    leaflet()%>%addTiles()%>%
      addMarkers(lng=point()[2],lat=point()[1],popup="Inmueble estimado")%>%
      setView(lat = point()[1], lng = point()[2], zoom = 18) 

    
  })



  
  
  
})



