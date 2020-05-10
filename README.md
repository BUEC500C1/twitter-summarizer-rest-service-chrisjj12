# Program Description

This program implements the use of ffmpeg, threading, and processing. It receives a list of four twitter handles because that is the number of cpu's on my computer. It pulls and downloads tweets of both the text and the picture and then puts it into an image that well then be collected and turned into a video. This program uses threading and processing to thread through all the tweets from all twitter handles and then processes each video by having each of the four cpu's compiling the video for each of the four twitter handles. The text of the tweet is presented on an image and if there is a picture that was part of the tweet, it will pop up next in the video. The video is .avi format. When the program has finished, all image files will be deleted so that only the video will show. This is for organization and making the directly as clean as possible.

## Flask App

This program will have the user type up in a valid twitter user handle and hit enter. This will created the video and download it to the computer. But this locally hosted.

## AWS

AWS is implemented into this program so that we can run a flask app on a computer in an amazon data center that is always running. We use an ec2 instance so that anyone can access our api at any time. If you just run Python on your computer for a flask app, it’s locally hosted and if you close your laptop or turn it off then the api can’t be accessed. Also, all the security settings we used for the EC2 instance does help security, we only allowed http and ssh traffic to enter and leave the computer, and no other network protocol which makes it a little safer.
