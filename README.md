## Pitcher Predictor

This is a simple Flask web app made using [MLB-StatsAPI](https://pypi.org/project/MLB-StatsAPI/) and hosted on Vercel.

You can access the tool at [pitcher.bob-brown.com](https://pitcher.bob-brown.com).

### Primary Purpose
* Allows users to see the predicted starting pitcher for any MLB game at any point in the season. 

### How It Works
* This information is gathered based on the previous starting pitchers for the team of your choosing and the number of games between the current date and your selected game. 

### Notes:
* Currently, the frontend has little-to-no styling. This should change in the near future. 
* As you might guess, injuries and roster changes are not recognized in the algorithm and may cause inaccurate results. 
* Not much error handling has been built into the site, so choosing past game dates or messing with the parameters will cause errors. 