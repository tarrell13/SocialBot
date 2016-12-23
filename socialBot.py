#!/usr/local/bin/python3

'''
Author:         Tarrell Fletcher
Date Created:   December 22,2016
Last Modified:  N/A

Synopsis: Program will send out a web bot to post status updates on all your favorite
          social media websites. FOR THIS WORK PROPERLY, USERS SHOULD LOG INTO SITES
          AND ALLOW BROWSER TO REMEMBER PASSWORD!

LOG:    (1) postMe() Function needs to be configured
        (2) Maybe a way to log users in if they are logged out
        (3) Find a way to store the status string

Usage:
-v:             Verbose Output
-s:             Posting Status
-h --help:      Show commands
--facebook:     Posting to FaceBook.com
--twitter:      Posting to Twitter.com
--all           Multiposting to all websites
--fetch:        Open all websites or specified websites
--upload:       Uploads Picture to sites [Provide path]

Example:    (1) ./socialBot.py  --facebook -s Today was a good day!
............(2) ./socialBot.py  --all -s Hello Everyone
............(3) ./socialBot.py  --all --fetch
............(4) ./socialBot.py  --twitter --upload ~/Pictures/sunnyday.png
'''

import sys
import webbrowser
import getopt

FACEBOOK = False
TWITTER = False
VERBOSE = False
UPLOAD = False
STATUS = False

commands = ["-v", "-h", "-s","--help", "--facebook", "--twitter", "--all", "--upload"]

'''CommandMe Function will define commands that are passed into the program'''
def commandMe():
    global FACEBOOK, TWITTER, VERBOSE, UPLOAD, STATUS

    try:
        getopt.getopt(sys.argv[1:], "h:v:s", ["help", "facebook", "twitter", "all", "upload"])
    except getopt.GetoptError as err:
        print(str(err))
        usage()

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == ["-h", "--help"]:
            usage()
        elif sys.argv[i] == '-v':
            VERBOSE = True
        elif sys.argv[i] == "--facebook":
            FACEBOOK = True
        elif sys.argv[i] == "--twitter":
            TWITTER = True
        elif sys.argv[i] == "--upload":
            UPLOAD = True
        elif sys.argv[i] == "--all":
            FACEBOOK = True
            TWITTER  = True
        elif sys.argv[i] == "-s":
            STATUS = True

        print(STATUS)

'''Usage Function will display program usage'''
def usage():
    print("Usage: ./socialBot <OPTIONS> -s <Status>")
    print("-v:          Verbose Output")
    print("-s:          Posting Status")
    print("-h - -help:  Show commands")
    print("--facebook:  Posting to FaceBook.com")
    print("--twitter:   Posting to Twitter.com")
    print("--all:       Post to all websites")
    print("--fetch:     Open all websites or specified websites")
    print("--upload:    Uploads Picture to sites [Provide path]")
    print("")
    print("Example:....(1)./socialBot.py --facebook -s Today was a good day!")
    print("............(2)./socialBot.py --all -s Hello Everyone")
    print("............(3)./socialBot.py --all --fetch")
    print("............(4)./socialBot.py --twitter - -upload ~ / Pictures / sunnyday.png")
    sys.exit()

'''Fetch will open all sites in browser simultaneously'''
def fetch():
    for i in range(1, len(sys.argv)):
        if sys.argv[i] == "--facebook" and FACEBOOK:
            webbrowser.open("https://www.facebook.com")
        elif sys.argv[i] == "--twitter" and TWITTER:
            webbrowser.open("https://www.twitter.com")
        elif sys.argv[i] == "--all":
            webbrowser.open("https://www.facebook.com")
            webbrowser.open("https://www.twitter.com")

'''postMe will send bot out to post status'''
def postMe(arg):

    if FACEBOOK:

    if TWITTER:
    sys.exit()




commandMe()