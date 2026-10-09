## text_based_rpg README & AAR

## Quickstart
```bash```
git clone https://github.com/jessescodes/text_based_rpg.git
cd text_based_rpg
python3 main.py

## Background & Preface: The After Action Review

First let me preface what this is, and what this public repo is supposed to
be. I made this Github account to track my progress as I learn to write code,
and document "my journey" if you will.

What these README's will contain will be what we called in RANGER Battalion an
After Action Review. After finishing any mission in Batt we would always go over
what it was we set out to do (what was the mission). What did we actually do?
What went well, and ultimately what can we do to be more effective in the future.
I believe this pattern and behavior is among the most effective ways to not only
improve, but ensure you're not making mistakes you don't recognize. This will be
the only repo I explain this, but if someone does read it I figure I should give
you a heads up.

What is an AAR?
1. What was the intent of the mission/ project?
2. What happened during the course of the mission/ project?
3. What were the sticking points? What could be improved? How can we leverage
that to be more efficient in the future?
4. What went well? What could we reproduce to be more successful in the future.

## WHAT WAS THE GOAL 

The goal with this exercise was: I read in a few different places that a text based
RPG was a great way to learn basic programming. So I followed that advice. 

When I started the project I honestly had no idea it would be this long! I just
kinda thought it would be funny to have some satirical WoW elements, and I didn't
want it to be over immediately. Of course I needed to figure out how make the 
player class dynamic and mutable. Get stronger continuously as the game progresses.
And have some form of gearing systems in place. I also wanted to have multiple
"Zones" if you will. So the player can experience Ellewyn forrest, STV, BRD etc.

Honestly starting this project I didn't realize what that would amount to. I just
kinda started writing all of that into a notebook, and started writing classes.
Above was really the kind of "gist" of what my idea of what the game would
become.

Also I want to ensure this is articulated. I did stop. I didn't "balance" the 
game as deeply as I wanted to. I also didn't get all the way to serialization.
This was a deliberate choice. I'm sure you see the save.json along with some
bugs inside the code. This was my thinking as I was finishing:

Ultimately I really wanted this code to be a proper "reflection" of my abilities
as a "developer". However, I wanted this to reflect where
I am at day 30-35 of learning to code. The more I stayed in the terminal fixing 
this, and perfecting it it would become closer to "production grade" code, but 
it also got further from the "where I am now". Not only does that defeat the 
point. Its extremely counter productive to the use of this, and these exercises.

The entire point of all of this are the mistakes. Failure is the most important
part, so if I spent another 2 weeks scrubbing this to perfection, I would 
essentially "lose" the sharpening stone, and the path marker I wanted this project
to be. 

## HOW DID THE Project GO?

So first and foremost this went way better and way worse than I expected. No one
tells you how long codebases can get from just a small idea. When I started writing
this I thought "yeah this will be like 300-500 lines" Kinda long for a first "big"
project, but you know what. I'm feeling pretty brave.

Well I honestly had absolutely no idea the sheer scope this 300 liner would become.
Now I understand though. Really the "business" logic is pretty simple, but I dint'
realize how typing intensive all the separate subclasses would be. Or just a text
based RPG would essentially be long textually because "I'm telling a story with
text. DUH". Yea I was pretty ignorant to what this was. Looking back I think before
I even started, I still viewed code as something "Magical". After I came to realize
its not. Honestly whatever you want to get it, you'll probably need to put at least
2-10 times more effort in.

I think the first "uh oh" moment was when I was building the player subclass.
All the attributes I started adding to it to track the states, then the inventory
system and equip methods. I really started to realize "ok there are a lot of 
states I need to follow", and it was initially really overwhelming! 

The Monster and Boss subclasses were initially really easy to write because their
mutable attributes weren't very large, and as I was writing them I had a general
Idea of how I wanted to combat "engine" and honestly I feel bad calling it that
but how my functions would interact with the classes to mutate their health.

Speaking of the combat functions those were what I decided to do almost last, 
because it was so simple. We'll get to that later.

So as I was writing I had a general idea that I wanted "zone nodes" and that I 
would connect them to one another, and later on that will end up being what I spent
a lot of time agonizing over trying to figure out. But essentially as I started
I just drew a bubble chart with all the connections, and then from there I wrote
the node classes. I ended up making quite a few parent classes so I could take
advantage of inheritance, and not have to write a ton of redundant code. Honestly
looking back I don't know how effectively I implemented that? I think I probably
could have been much more effective with inheritance, and been able to write
less code. However, I didn't quite know how. I still don't I don't think so that
is definitely something I'll need to look into moving forward!

So at this point I'm about 2 days into the project and I have all of my classes
pre-built and ready to go. That's the hard part over right?

Absolutely not, now is where I realized how little I know about coding and how
absolutely imposing connecting things in main.py really is. However, I know that
there is an efficient way. So before I do anything else I write up some quick
functions for the combat system. Ultimately I know I want the player to be able
to heal with potions, and choose between each attack what they'll do (turn based).
Ultimately i decided a while loop inside the zones combat occurs would be the 
most effective "clean" way to handle this.

I think I could have handled the "combat" more modularly. However, right now I 
honestly believe it was a good choice to put it there. As it was easy to include
those loops in Monster and Boss parent classes. And this is one place where I 
feel I was really effective in my use of inheritance.

This is where the hard part started, but honestly the greatest learning also 
happened. How to connect everything, and how to make this all function inside a
main loop.

After a lot of thinking, reading docs, browsing random github repos etc I had an
idea. I can use hashmaps to make key value pairs, and link the user input to the 
key, and our value will be what the program does. 

That's how I got to what I actually did, and believe me it was a pain while i wrote
it. Like in my world building function I initially didn't have all of the node
classes init at the very top, so my program would crash on startup, until I moved
them all up to the top.

Anyway, this one took quite a bit of trial and error, but we got to the point
that the program actually ran! Though I learned about dependency through all of
this! Quite a few of my methods required self, and player! But it didn't know
what the player was!

Once again. Another nightmare of digging until I figured out the lambda idea
to make give the class method the player object into the function being called
inside of the hash. However that got really repetitive (we'll go into that more
in the lessons learned section).

## LESSONS LEARNED
In true Batt fashion we'll start with lessons learned, and what I can do better
during my next execution. Then We'll finish with what I believe went well, and 
patterns I feel I can leverage in other projects (at least until I learn more 
effective methods to implement).

One of the biggest lessons learned is what coding really is. Coding doesn't make
just one task easier. It makes doing 1 thing repeatedly easier, however, in doing
so you'll need to put that much effort into the code itself. So learning expectations
on a project was a big thing I learned. It's probably going to be longer than
that simple outline in your head you imagined.

Another lesson was what a program really is. It's just data. Especially in Python.
like this whole project was nothing but dictionaries. My entity classes were dictionaries
I was mutating. My zones were dicts I had to traverse efficiently. Same with 
shops, potions. Literally the whole thing is just a data structure.

A really big lesson I learned doing this next time i really need to spend more
time focusing on the structure of my dictionaries, or data structures in general.
Literally ALL OF THE CONNECTING CODE WAS TRAVERSING AND CALLING THAT DATA. I wish
I would have spent more time being "smarter" about how I built those dicts so
it would be easier and more intuitive to traverse and call those values.

Another really big takeaway from this was dependency injection (Yea I had to 
google that one). But making a function to "inject" the needed variables into 
class method calls would have saved me a huge headache with the ALL OF THE 
LAMBDAS inside my mapping system. Also I realize that those lambdas are a "weak
link" in my code. Like if something changes in the future, if the methods are 
altered, if we need other parameters etc my entire system is built on lambdas
rather than just functions. Intuitively that feels like a weak link in my system, 
and would probably be the first thing that breaks in the future.

Given my background, things like that really drive me nuts. If I can see something
has a weakness my "instinct" is to make it as strong as everything around it.
Though i discuss why I didn't earlier. The goal isn't to make this perfect. It's
to document exactly this, and remember what hung me up my first month of coding.

## WHAT WENT WELL
I'm going to be honest, after finishing I'm not exactly satisfied with my 
performance. I'm glad the system runs, and honestly when the system ran the first
time it was a big "LETS GO" kind of moment. However, the last day, debugging and 
all of that makes it really easy for these to feel like failures.

However, what did go well? Well it runs and doesn't crash! That's a plus. My 
class objects mutate the way I intend them to. Leveling up changes stats, and the
player gets to grow progressively stronger as they defeat monsters. I can travel
to all the zones. So essentially I was able to "accomplish the mission", and 
ultimately perfectionist tenancies aside. That is mission accomplished.

Another thing I believe I did well was the separation of responsibilities. That
is what we called it in the military. I did well not mixing my module logic, and
looking at it while debugging it was easy to go to the modules that were failing,
and I didn't need to "hunt" for logic because my project was separated by modules
which i separated by their responsibilities.

I also feel my use of key: value pairs to connect user input and program functions
was really well done and thought out. It's probably the part of the project I'm 
most proud of. Because its simple, and keep it simple stupid is something I've 
spent years trying to implement on a deep level.

Last I personally liked my main() file. It was short like 30 lines, and being able
to compress 2000+ lines into 30 lines of actual running logic was something I 
felt was well done.

## FINAL THOUGHTS
Ultimately for a one month project I felt this was incredibly efficient. I did
a lot of learning on traversing data structures especially. 

You might notice a save.json in the repo. I had planned on making a way to save
the game and load the game. However I'll be honest I had no idea how to do that. 
As such I felt it wouldn't give a very accurate example of where I am now, and I
will probably incorporate that into my next project once I learn how.

Also I learned that I really do love this. It's problem solving. Optimization.
And deep levels of Organization. I also realize that even after "finishing" a
project like this there's a lot to polish.

All of these things speak deeply to me given my background. I love having something
that while you can "accomplish" your goal there's always optimizations that can
be implemented. You can always get better, run faster, make it cleaner etc. 
That realization made coding even more enticing to me. It gives me something to 
learn. Ways to fail, and ultimately its through all these failures that I'm 
going to improve even more.

THANKS FOR READING- Jessescodes.
