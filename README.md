# Engineering_4_Notebook
My engineering stuff!


## Dice Roller
For a while I foolishly kept trying to find libraries that read key presses because I thought I wanted it to work like an interrupt. It took too long, but I figured out the the user would be the one controlling each roll and wouldn't need it as fast as possible. Also I tried using "None" instead of checking if the length was zero, but I think input() doesn't result null values.


## Calculator
This one wasn't too bad for, but I forgot to cast the input as an integer for a bit. It was an easy fix. Other than that I didn't really encounter any problems besides typos. 

## Quadratic Solver
This one was fun. The main hiccup I had was forgetting to cast the input as integers. Every other problem was pretty much a typo. I did forget to make it a function and had to retroactively turn it into one, but that didn't take long. Just a simple, straight forward assignment.
## String Splitter
This one was fine, but there were a few lines where I made a thoughtless mistake. Nothing that couldn't be fixed after one round of bug fixing. The more major problem was that my repo got corrupted. I reinitialized it, and it would successfully pull from Github, but it wouldn't push to it. I ended up deleting the whole thing and recloning it, which worked out.
## Hangman
This one was great fun. I did have a bit of a headstart because I made hangman in Python last year for fun. However, this version was pretty bad and didn't work when I tried to open it for this project. One of the bad things was how, when finding the letters, I had a function to find a certain instance of a letter. For example, the function might look for the second instance of a letter. It required an extra loop each time to find all instances. This time I realized that I only ever want every instance. That fix cleaned things up a lot. The code from GeeksforGeeks that I used taught me about list comprehension, which is cool. I also removed redundancies, like unecessary variables, and made the code a little prettier. I might go back and break it up into a handful of functions to improve readability. I made it so funny symbols like "!" or a space were revealed automatically because it didn't seem fair otherwise. I also forced lowercase for both the word and the guess. I might go back and improve on that. I also considered having something more complicated for the stickman printer, but it really seemed to work well and I guess I didn't really see the point. I'm not sure how much longer it would have taken me if I didn't have an old project to base this one on. The hardest part for me a year ago was figuring out that I should store the positions guess right, not the letters. I really do think that made it easier. Probably faster than last year, but not as fast as this year.

## Bash Blink
This was the one where I had to make two LEDs blink 10 times with a simple bash script. Going into this I had never written a bash script, so just about everything was new to me. The most unfamiliar thing was the for loops. I saw some alternate versions of them, so I guess I was lucky to have chosen correctly. The final issue I had is that I made some changes in GitHub, like adding comments. When I tested it on the Pi it didn't work. It turns out I had just forgotten to put spaces in front of my comments. It was an easy fix. The other thing I don't get is why gpio 0 refers to pin #17, that doesn't make any sense to me.
