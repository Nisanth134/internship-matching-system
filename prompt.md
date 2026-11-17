Tanooj:
The Prompt I used is: 
"I wrote a Python function that calculates a match score by comparing a student's skills (list of strings) to an internship's required skills (list of strings). 
What edge cases and invalid inputs should I validate against?
The AI suggested validating against:
1. Incorrect data types (passing strings or integers instead of lists).
2. Empty lists (student has no skills, or internship requires no skills).
3. Case sensitivity and whitespace (e.g., "Python" vs " python ").
4. Missing dictionary keys when processing the broader database.
*How I applied this:* 
I added TypeError checks for list validation, implemented a division-by-zero safeguard for empty internship skills, and used .strip().lower() to handle case and whitespace discrepancies.

Koushik ram:
prompts used:
"I am building a Flask app for an internship matcher. Generate a Bootstrap 5 HTML form that takes a student's name and a comma-separated list of skills. Also, provide the Flask route snippet to parse that comma-separated string into a Python list and pass it to my template."

*AI Response Summary:*
The AI provided the HTML using Bootstrap's grid and card classes. For the backend, it recommended using .split(',') and a list comprehension with .strip() to clean up the user input before passing it to the matching algorithm.

*How I applied this:*
I implemented the list comprehension in app.py to sanitize the data before sending it to Person 1's logic, and used the Bootstrap code in templates/index.html to render the results dynamically using Jinja2 syntax.

Nisanth: 

*Prompt used:*
"I am deploying a Flask application to Render. What command do I need to use for the 'Start Command' to run the app in production, and what library do I need to add to my project to support it?"

*AI Response Summary:*
The AI explained that Flask's built-in server is not secure or stable for production. It recommended installing gunicorn and setting the Render Start Command to gunicorn app:app (since the Flask instance is named app inside app.py).

*How I applied this:*
I added gunicorn to a new requirements.txt file so Render knows to install it, and I used gunicorn app:app during the Render deployment configuration phase.
