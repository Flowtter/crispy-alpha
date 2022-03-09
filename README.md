# Crispy
Crispy is a python program to make VALORANT montages.

# Example
[youtube link](https://www.youtube.com/watch?v=9DxsrQEqagw)

# Disclaimer
- This project is only about 10% complete.
- We plan to synchronize the music drops with the clips.
- Some clips crash the program.
- Templates have to be added manually.
- **It only works on linux**, due to some errors, the project currently only works on linux.

## why is it so slow
This is a test version, some numpy functions are not used correctly and not everything is multithreaded yet. Moreover, most of the rendering is done on the CPU.\
Curently, 30 mins of gameplay takes 10-15 mins to make a montake, we're targeting 5.


# How to use it
- clone the project
- Create a directory `resources/videos` and `resources/audio`.
- add your clips in the directory `resources/videos` and, eventually, a music in `resources/audio`.
- run `pip3 install -r requirements.txt`
- run `python3 src/main.py`

# What we want to add
- **support for windows**
- beat drop music
- better syunchronizations on kills
- AI to detect if it's a nice kill (flick for example)
- AI to detect kills without templates

## When will it be added 
Probably in June and August, when we will have time to work a lot on the project.
Currently we are refactoring a lot of things.
Pull requests are totally open and welcome.

# Contributors
[Gyroskan](https://github.com/gyroskan) - Directory management
