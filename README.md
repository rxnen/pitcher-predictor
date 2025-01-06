# Pitcher Predictor

This is a simple Flask web app made using [MLB-StatsAPI](https://pypi.org/project/MLB-StatsAPI/) and hosted on Vercel.

You can access the tool at [pitcher.ronenjain.com](https://pitcher.ronenjain.com).

## Primary Purpose
* Allows users to see the predicted starting pitcher for any MLB game at any point in the season. 
* If you are going to see a baseball game in a week, this app will estimate the starting pitcher based on previous games.

## How It Works
* This information is gathered based on the previous starting pitchers for the team of your choosing and the number of games between the current date and your selected game. 

## Notes:
* Injuries and roster changes are not recognized in the algorithm and may cause inaccurate results. 
* Not much error handling has been built into the site, so choosing past game dates or messing with the parameters will cause errors. 

## Author

Created by **Ronen Jain**.  
For more information, visit [ronenjain.com](https://ronenjain.com).