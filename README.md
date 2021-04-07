# Autophone

## Overview

This project aims to "automate" navigation through phone menus. Hate calling your ISP, bank, or any company line? 

Having to navigate the numerous phone menus, waiting, etc. just to talk to someone. 

Well, this project will call the company, navigate the phone menu based on an action you choose, and then call you back when someone's on the other end!

It's a work in progress, but the Shell version works right now.

## Setup 

Download the zip and extract it OR git clone this repo.

Navigate to the `autophone/shell-module` directory,

In the terminal, type: `python3 shell-module.py` 

Type an action like `businessHours` or `accountInfo` or `callRogers`. 

The app will call Rogers, or pre-made IVR, and start navigating the menus. A recording of the call is saved on Twilio. The call back feature is a WIP, but the menu navigation works!

