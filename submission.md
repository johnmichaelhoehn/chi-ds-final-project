### Project Problem and Hypothesis

One of the reasons frogs serve as an important part in the ecosystem is their ability to act as a leading indictor for the health of an ecosystem. Because of this reason, scientists are able to use information on the types and number of frogs in a given location to understand if interventions are needed or if ongoing interventions are working. With a limited number of scientists available to monitor, a large portion of monitoring efforts are taken on by amateurs.

For amateurs starting to monitor for frogs, it can be difficult to know what frogs to listen for as well as knowing what frogs you are actually hearing when you are monitoring. However, using publically available data on past frog monitoring sessions as well as other relevant information (date, location, and weather information), I believe that we can create an application that will identify the different frogs that a new monitor is likely to be hearing at a given time and location with 95% confidence.

This problem will require using decision trees to predict a categorical outcome – the types of frogs that one is likely to be hearing given their location. This will provide value by making it easier for new monitors to get involved and by making the information that they gather surrounding the frogs they are hearing more accurate.


### Datasets

The initial dataset that I will use include 18,000 observations from the Illinois and Indiana area dating back to 1999. The features of this dataset are:
•	ObsSeq
•	CountyState
•	RouteID
•	RunDate
•	MonitorID
•	Run
•	Location
•	Species
•	Call_Index
•	Seen
•	TimeObs
•	MonitorName
•	Precipitation
•	Below_Freezing
•	Latitude
•	Longitude
•	CoordFrom
•	Temp
•	Wind_Code
•	Sky_Code
•	Cloud_Cover


### Domain knowledge

I am a current frog monitor. In this way, I understand the process with which the data is collected, the goals of the data collection, and the types of observations that are available.  The current research is relatively broad – either focused academically on the current state of frogs in a given ecosystem or towards the amateur in a broad bucket of possible frogs in their area.  There is no contextual tools to help frog monitors that I have found.

### Project Concerns

The main concern that I have is that the data I will use is all crowd sourced and provided by amateurs. This provides risk of incorrect data that can lead to poor results.

### Outcomes

I expect the output to be an application that provides the types of frogs one may be hearing given their current location, weather, and time of year with the likelihood of it being each certain frog. The target audience is amateur frog monitors.

My model does not need to be overly complicated, but rather a simple decision tree to lead to the frog type one is likely to hear. I hope to be able to integrate information about that given frog to the application which may be more complicated.

In order to be a success, we will see the frog that one is likely to be hearing accurate 95% percent of the time (e.g. the frog one is actually hearing is on the list). A bust would be that the list is worse than 50% accurate.
