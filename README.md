<h1>Python Exercise Tracker:</h1>
<h2>Using APIs to create a web app to accurately record exercise details into a google sheet.
(Keys and ID have been removed, will need generating for personal use).</h2> 

<i> A Work in Progress. </i>

<b>Aim:</b> to create a simple web app which can record bouts of exercises and personal bests onto a google sheet for future viewing. 

<b>How it Works:</b>
1. The user must edit lines; 8,9,10,11 appropriately for accurate calculations and generate API_KEY and APP_ID from the [Nutritionix API](https://trackapi.nutritionix.com/v2/natural/exercise).
2. Using the [Nutritionix API](https://trackapi.nutritionix.com/v2/natural/exercise) and its natural language processing glossary, the user is asked "what did you do today?", the user would then respond by typing something along the lines of "i ran 2km in 30mins".
3. The API can then calculate calories burned, organises the input and records the results to a .JSON.
4. This .JSON is then organised using a for loop: 

![image](https://user-images.githubusercontent.com/120504783/210156790-e8953220-3669-4d1b-a92a-3cf8329758f6.png)

 Where the keys in the dictionary will correspond to the column headings.
 
5. These column headings will be generated within the google_sheet we have created and then connected to using the [Sheety API](https://sheety.co/).
6. Dictionary Keys and values are then pasted into google sheet automatically.

![image](https://user-images.githubusercontent.com/120504783/210157217-3911aa45-bd34-4317-aefe-ec78fcda55a8.png)


![image](https://user-images.githubusercontent.com/120504783/210157164-2ec7fb17-6b8f-4042-a31a-9c42c36c0847.png)

<b>Errors:</b>
The duration column requires formatting as the .json reads correctly but the google sheet does not.

<b>Noteable limitations:</b> 

Currently the Nutritionix NLP glossary does not recognise certain exercises as anything other than 'Weightlifting' (e.g. Deadlift) and so this limits the precison of our data and does not allow the user to accurately record their exercises.

<b>Future development:</b>

If an improved glossary of physical exercises and their parameters (i.e. Kilograms, Lbs, Km, Miles) is implimented, a simple web app could be rolled out to various sports clubs and gyms where members could input thier personal bests and the google sheet could be used as a digital leaderboard.

<b>Personal thoughts: </b>

Add NLP to the list of course topics I wish to learn.


This Github Repository contains:
- .py files.

Game runs using python 3.10 interpreter.

