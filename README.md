![R.A.F~Home~](/shots/R_A_F~Home~.png)

# R.A.F_Remote_Access_Framework_
Python Remote Access Tool [ Not Trojan ].

# Overview

R.A.F [Remote Access Framework] is a multi-client reverse-shell written in python. It is not multi-threaded yet however, modifications are in the works.
I greatly encourage any contributions. 


## Update

* **Version: 1.1.2**
* **Lots of bug fixes**
* **Numerous new features**


## Screenshots
<img src= '/shots/R_A_F~Connecting~.png' width= 400>     <img src= '/shots/R_A_F~Home~.png' width= 400>


## Getting started
1. `git clone `
2. `cd R.A.F_Remote-Access-Framework_`
3. `python3 R_A_F.py`

***

# Requirements

R.A.F is written in python 3.6 therefore you'll have to run with pytnon3

## External Modules

* **psutil**  
* **termcolor**

## Usage

To run R.A.F you'll need both the Tower.py and the R_A_F.py .

* **R_A_F.py** - This will run on public host and wait for connections from clients [port forwarding is required if server is behind firewall(NAT)]
* **Tower.py** - This connects to the remote server and receives commands.
***

## Server

Simply run **R_A_F.py** using python 3.6 or any pyhton3 version.

`python3 R_A_F.py` [see screenshots above]

To view all connected clients;

`'hostname'@R.A.F:~ > clients`


To interact with a client;

`'hostname'@R.A.F:~ > interact 0`

<img src= '/shots/R_A_F~Client-interaction~.png' width= 600>

once inside client, use `help` to view command list, Enter any command in the list.

<img src= '/shots/R_A_F~Client-command-list~.png' width= 600>

## Client

You can run **Tower.py** using either python2 or python3

`python Tower.py` or `python3 Tower.py`

But first of all, change the Host and Port variables in **Tower.py** to yours. [Automation of this coming soon]

To compile to exe, for now use; `pyinstaller --onefile --windowed Tower.py` in terminal/command prompt. Also I recommend using U.A.C,

`pyinstaller --onefile --windowed --uac-admin Tower.py`


ALTERNATIVELY [ recommended ]:

You can use a beautiful and easy to use gui tool developed by @brentvollebregt called [auto-py-to-exe](https://github.com/brentvollebregt/auto-py-to-exe.git)
 

## Known Error

* **download** - The download feature has a small bug, files do download but the loop breaks somewhere there and destabilizes the whole program
any help would really be appreciated.

<img src= '/shots/R_A_F~File-upload~.png' width= 650>

***

## TO DO

* **Persistence**
* **Multithreading**
* **Auto Tower.exe compilation** 


# Disclamer
R.A.F was built as a utility to manage multiple machines at ones from any where in the world not for malicious purposes,
R.A.F should only be used in the lawful, remote administration of authorized systems. Accessing a computer network without authorization or permission is illegal. 

***
Please if any errors are spotted be sure to contact me, also i wrote this script with sublime text so if you try editing it and see alot of unalligned '#|', 
!! BLAME SUBLIME !! or you could just use it instead.
