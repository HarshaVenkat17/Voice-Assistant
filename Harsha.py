# python3 -m pip install <package> 
import pyttsx3
import speech_recognition as sr
import webbrowser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import mimetypes
from email.mime.application import MIMEApplication
import os
import getpass
#import time as t
import time
import wikipedia
import datetime
import pandas as pd
import threading as thr
from multiprocessing import Process
from PIL import ImageGrab
import recognise
import re
import string
from pyowm import OWM
import json
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from plyer import notification
import schedule
engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices') 
engine.setProperty('voice',voices[0].id)
""" for speech rate:
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+50)
"""
#keep commands like pause and clear after google and other sites 
def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour=int(datetime.datetime.now().hour)
	if(hour>=0 and hour<12):
		speak("Good Morning!")
	elif(hour>=12 and hour<16):
		speak("Good Afternoon!")
	else:
		speak("Good Evening!")
	speak("How can I help you?")

def takeCommand():
	r=sr.Recognizer()
	r.energy_threshold=800#(a float no.)sounds below this are not considered. (Typical levels of speaking: 150-3500)
	#r.dynamic_energy_threshold=True   # to adjust automatically. This takes more time. So the adjust_for_ambient_noise is used
	#r.dynamic_energy_adjustment_damping = 0.15  # portion of energy retained
	#r.dynamic_energy_adjustment_ratio = 1.5   #minimum factor by which speech is louder than ambient noise
	#r.adjust_for_ambient_noise(source, duration = 1)   #method 2 for recognition 
	#r.adjust_for_ambient_noise(source: AudioSource, duration: float = 1) -> None #(also check)(duration atleast 0.5)
	with sr.Microphone() as source: 
		print("Listening...")	
		r.pause_threshold=2	#minimum length of silence (in seconds) that will register as the end of a phrase
		#r.operation_timeout = 1.0 # type: Union[float, None]#timeout (in seconds) for internal operations, such as API requests
		audio=r.listen(source)
	try:
		print("Recognizing...")
		query=r.recognize_google(audio,language="en-in")
		print("User said:%s \n"%query)
	except:
		print("I am sorry. Say that again please...")
		speak("I am sorry. Say that again please")
		return "None"
	return query

def job():
	global ct
	ct+=1
	hrs=ct//4
	mnt=ct%4
	if mnt!=0:
		if hrs==1:
			msg="Running for "+str(hrs)+" hour "+ str(15*mnt)+" minutes..."
		else:
			msg="Running for "+str(hrs)+" hours "+ str(15*mnt)+" minutes..."
		notification.notify(
            title="15 minutes reminder",
            message=msg,
            timeout=5
            )
	else:
		if hrs==1:
			msg="Running for 1 hour..."
		else:
			msg="Running for "+str(hrs)+" hours..."
		notification.notify(
            title="1 hour reminder",
            message=msg,
            timeout=5
            )
def call():
	global ct
	ct=0
	schedule.every(15).minutes.do(job)
	while True:
		schedule.run_pending()

def VA():
	checkList1=["kill yourself","quit","exit","see you soon"]
	checkList2=["search","wikipedia"," for ","open"]
	checkList3=["search","google"," on "," for "]
	checkList4=["capture","take photo","video","webcam","camera"]
	checkList5=["send files"," share ","bluetooth"]
	checkList6=[".in",".com",".co",".org",".net",".us",".int",".edu",".gov",]
	checkList7=["hibernate","shutdown"]
	checkList8=["hibernate in","shutdown in"]
	checkList9=["hibernate at","shutdown at","hibernate after","shutdown after"]
	checkList10=["how ","which","when","who ","why"]
	checkList11=["search","play","watch","open"]
	checkList12=["netflix","amazon prime","amazon","flipkart"]
	checkList13=["drive","google doc","slide","sheet","hangout","photo","duo","meet"]
	while True:
		try:
			query=takeCommand().lower()
		except:
			query=input("Enter query: ")
		if "how are you" in query:
			speak("I am feeling good. Thanks!")
		elif "what is your name" in query:
			speak("My name is Harsha and I am a voice assistant.")

		elif "who" in query:
			if "i" in query or "we" in query:
				for i in cList:
					speak("You are"+i)
			elif "you" in query:
				speak("I am Harsha, speed 1.8 GigaHz, memory 8 Giga byte.")
		elif "work for" in query:
			username = getpass.getuser()
			speak("I work for %s."%username)
		elif "paint" in query:
			os.system('cmd /c "start ms-paint:"')
			os.system('cmd /c "pause"')
		elif "skype" in query:
			url="https://web.skype.com/"
			chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
			webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path),1)
			webbrowser.get('chrome').open_new_tab(url)
			os.system('cmd /c "pause"')
		elif("outlook" in query):
			url="https://outlook.live.com/mail/0/inbox1"
			chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
			webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path),1)
			webbrowser.get('chrome').open_new_tab(url)
			os.system('cmd /c "pause"')
		elif (("one drive" in query) or ("onedrive" in query)):
			url="https://onedrive.live.com/"
			chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
			webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path),1)
			webbrowser.get('chrome').open_new_tab(url)
			os.system('cmd /c "pause"')
		elif (("microsoft" in query or "ms" in query) and "online" in query):
			try:
				if "word" in query:
					sStr="https://office.live.com/start/Word.aspx"
				elif "excel" in query:
					sStr="https://office.live.com/start/Excel.aspx"
				elif (("powerpoint" in query) or ("presentation" in query)):
					sStr="https://office.live.com/start/Powerpoint.aspx" 
			except Exception as e:
				speak("Sorry, cannot open!")
				print(e)
			chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
			webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path),1)
			webbrowser.get('chrome').open_new_tab(sStr)
			os.system('cmd /c "pause"')
		elif "wikipedia" in query:
			speak("Searching wikipedia...")
			for c in checkList2:
				if c in query:
					query=query.replace(c,"")
			print(query.lstrip())
			results=wikipedia.summary(query,sentences=1)
			speak("According to wikipedia")
			print(results)
			speak(results)
		elif ("youtube" in query and any(c in query for c in checkList11)):
			yList=query.split(" ")
			yInd=yList.index("youtube")
			if "in youtube" in query:
				query=query.replace("in youtube","")
			else:
				query=query.replace("youtube","")
			for c in yList:
				if c in checkList11:
					if c=="search" and yList[yList.index(c)+1]=="for":
						c="search for"
					query=query[0:query.index(c)]+query[query.index(c)+len(c)+1:]
					break
			webbrowser.open_new_tab('http://www.youtube.com/search?btnG=1&q=%s' % query)
			os.system('cmd /c "pause"')
		elif "youtube" in query:
			url="youtube.com"
			chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
			webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path),1)
			webbrowser.get('chrome').open_new_tab(url)
			os.system('cmd /c "pause"')
		elif ("google" in query and any(c in query for c in checkList13)):
			if "slide" in query:
				url="https://docs.google.com/presentation/"
			elif "hangout" in query:
				url="https://hangouts.google.com/"
			elif "sheet" in query:
				url="https://docs.google.com/spreadsheets/"
			elif "doc" in query:
				url="https://docs.google.com/document/"
			elif "photo" in query:
				url="https://photos.google.com";
			elif "duo" in query:
				url="https://duo.google.com/"
			elif "drive" in query:
				url="https://drive.google.com/drive/u/0/my-drive"
			elif "meet" in query:
				url="https://meet.google.com/"
			else:
				url="https://www.youtube.com/"
			chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
			webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path),1)
			webbrowser.get('chrome').open_new_tab(url)
			os.system('cmd /c "pause"')
		elif "open google" in query:
			os.system('cmd /c start "title" /MAX "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"')
			os.system('cmd /c "pause"')
		
		elif "google with url" in query:
			chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
			try:
				speak("url please")
				url=takeCommand()
				url=url.lower()
				url= url.replace("dot",".")
				url=url.replace(" ","")
				url=url.replace("slash","/")
				if all(c not in url for c in checkList6):
					url=url+".com"
				if "https://" not in url:
					url="https://"+url
				print("searching with url %s" %url)	
				webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path),1)
				webbrowser.get('chrome').open_new_tab(url)
				os.system('cmd /c "pause"')
			except Exception as e:
				speak("Sorry, cannot find results")
				print(e)
		elif "search google" in query:
			try:
				speak(" What should I search for?")
				sTerm=takeCommand().lower()
				webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % sTerm)
				os.system('cmd /c "pause"')
			except Exception as e:
				print(e)
				speak("Sorry, cannot find results")   

		elif ("google" in query or "search" in query):#"search for" before "what is"
			query=query.replace("search for ","")
			query=query.replace("search ","")
			query=query.replace("google for","")
			query=query.replace("in google","")
			webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % query)
			os.system('cmd /c "pause"')
		elif "whatsapp" in query:
			try:
				url="https://web.whatsapp.com"
				chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
				webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path),1)
				webbrowser.get('chrome').open_new_tab(url)
				os.system('cmd /c "pause"')
			except Exception as e:
				speak("Sorry, cannot open WhatsApp")
				print(e)   
		#paint is to be identified before ms since query may contain "ms"-paint
		elif ("order food" in query or "zomato" in query or "swiggy" in query):
			if "zomato" in query:
				url="https://www.zomato.com"
			else:
				url="https://www.swiggy.com/restaurants"
			try:
				chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" 
				webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path),1)
				webbrowser.get('chrome').open_new_tab(url)
				os.system('cmd /c "pause"')
			except Exception as e:
				speak("Sorry, cannot order food") 
				print("Sorry, cannot order food due to "+e)
		elif (("show" in query or "movie" in query) and ("book" in query or "ticket" in query)):
			url="https://in.bookmyshow.com/"
			try:
				chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" 
				webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path),1)
				webbrowser.get('chrome').open_new_tab(url)
				os.system('cmd /c "pause"')
			except Exception as e:
				speak("Sorry, cannot book tickets") 
				print("Sorry, cannot book tickets due to "+e)
		elif any(c in query for c in checkList12):
			if "amazon prime" in query:
				url="https://www.primevideo.com/"
			elif "netflix" in query:
				url="https://www.netflix.com/"
			elif "amazon" in query:
				url="https://www.amazon.in"
			elif ("flipkart" in query):
				url="https://www.flipkart.com/"
			try:
				chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" 
				webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path),1)
				webbrowser.get('chrome').open_new_tab(url)
				os.system('cmd /c "pause"')
			except Exception as e:
				speak("Sorry, cannot open "+ c) 
				print("Sorry, Cannot open "+ c +" due to "+e)
		elif "book" in query:
			if ("cab" in query or "car" in query or "taxi" in query):
				url="https://www.goibibo.com/cars/"
			elif ("bus" in query):
				url="https://www.redbus.in/bus-tickets/"
			elif "train" in query:
				url="https://www.irctc.co.in/nget/train-search"
			elif ("plane" in query):
				url="https://www.goibibo.com/flights/"
			try:
				chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" 
				webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path),1)
				webbrowser.get('chrome').open_new_tab(url)
				os.system('cmd /c "pause"')
			except Exception as e:
				speak("Sorry for inconvinience. Cannot find your website")
				url="https://www.makemytrip.com/"
				chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" 
				webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path),1)
				webbrowser.get('chrome').open_new_tab(url)
				os.system('cmd /c "pause"')
		######3check location and navigation
		elif "locat" in query:
			query=query.replace(" in ","")
			query=query.replace("google ","")
			query=query.replace("maps","")
			query=query.replace("map","")
			try:
				qList=query.split(" ")
				if "locate" in query:
					sTerm="+".join(qList[qList.index("locate")+1:])
				elif "location" in query:
					sTerm="+".join(qList[qList.index("location")+2:])
				url="https://www.google.com/maps?q="+sTerm
				chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" 
				webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path),1)
				webbrowser.get('chrome').open_new_tab(url)
			except Exception as e:
				print("Cannot open Google maps due to "+e)
				os.system('cmd /c "start bingmaps:"')
			os.system('cmd /c "pause"')
		elif "navigate" in query or "directions" in query:
			query=query.replace(" in ","")
			query=query.replace("google ","")
			query=query.replace("maps","")
			query=query.replace("map","")
			try:
				qList=query.split(" ")
				if "navigate" in query:
					sTerm="+".join(qList[qList.index("navigate")+1:])
				elif "directions" in query:
					sTerm="+".join(qList[qList.index("directions")+1:])
				if "from" in query:
					fAddr="+".join(qList[qList.index("from")+1:qList.index("to")])
				else:
					fAddr="My+Location"
				if "to" in query:
					tAddr="+".join(qList[qList.index("to")+1:])
				url="https://www.google.com/maps?saddr=%s&daddr=%s"%(fAddr,tAddr)
				chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" 
				webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path),1)
				webbrowser.get('chrome').open_new_tab(url)
			except Exception as e:
				print("Cannot open Google maps due to "+e)
				os.system('cmd /c "start bingmaps:"')
			os.system('cmd /c "pause"')
		elif " map" in query:
			os.system('cmd /c "start bingmaps:"')
			os.system('cmd /c "pause"')
		elif "time" in query:
			strTime=datetime.datetime.now().strftime("%r")
			speak("Time is %s"%strTime)
		elif " date " in query:
			strDate=datetime.datetime.now().strftime("%A %e %B %Y")
			speak("Today is %s"%strDate)
		elif "movie" in query:
			os.system('cmd /c start "title" "PATH FOR MOVIES FOLDER"')
			os.system('cmd /c "pause"')
		elif "open songs" in query:
			os.system('cmd /c start "title" "PATH FOR SONGS FOLDER"')
			os.system('cmd /c "pause"')
		elif "open vlc" in query:
			os.system('cmd /c "C:\Program Files\VideoLAN\VLC\\vlc.exe"')
			os.system('cmd /c "pause"')
		elif "music" in query:
			os.system('cmd /c "start mswindowsmusic:"')	
			os.system('cmd /c "pause"')
		elif "alarm" in query:
			os.system('cmd /c "start ms-clock:"')	
			os.system('cmd /c "pause"')
		elif "stopwatch" in query:
			os.system('cmd /c "start ms-clock:"')	
			os.system('cmd /c "pause"')
		elif "timer" in query:
			os.system('cmd /c "start ms-clock:"')	
			os.system('cmd /c "pause"')
		elif "wifi" in query:
			os.system('cmd /c "start ms-availablenetworks:"')	
			os.system('cmd /c "pause"')
		elif "network" in query:
			os.system('cmd /c "start ms-availablenetworks:"')	
			os.system('cmd /c "pause"')
		elif "calendar" in query:
			os.system('cmd /c "start outlookcal:"')	
			os.system('cmd /c "pause"')
		elif "photo" in query or "pictures" in query:
			os.system('cmd /c "start ms-photos:"')
			os.system('cmd /c "pause"')
		elif any(c in query for c in checkList4):
			os.system('cmd /c "start microsoft.windows.camera:"')	
			os.system('cmd /c "pause"')
		elif any(c in query for c in checkList1):
			break
		elif "pause" in query:
			os.system('cmd /c "pause"')
		elif "cortana" in query:
			os.system('cmd /c "start ms-cortana:"')	
			os.system('cmd /c "pause"')
		elif "calculat" in query:
			os.system('cmd /c "start calculator"') #can remove all cmd,cmd/k,cmd /c k,c,....
			os.system('cmd /c "pause"')		
		elif "edge" in query:
			os.system('cmd /c "start microsoft-edge:"')
			os.system('cmd /c "pause"')
		elif "sports" in query:
			try:
				url="https://timesofindia.indiatimes.com/sports"
				chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
				webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path),1)
				webbrowser.get('chrome').open_new_tab(url)
				os.system('cmd /c "pause"')
			except Exception as e:
				print(e)
				speak("Sorry, cannot find anything. Try searching the news.")
				os.system('cmd /c "start bingnews:"')
				os.system('cmd /c "pause"')
		elif "news" in query:
			os.system('cmd /c "start bingnews:"')
			news_url="https://news.google.com/news/rss"
			Client=urlopen(news_url)
			xml_page=Client.read()
			Client.close()
			soup_page=soup(xml_page,"xml")
			news_list=soup_page.findAll("item")
			# Print news title, url and publish date
			for news in news_list[:10]:
				c="".join(x for x in news.title.text if x in string.printable)
				print (c)
				print(news.pubDate.text)
				speak(c)
				print("Link: "+news.link.text)
				print("-"*60)
			os.system('cmd /c "pause"')
		elif "voice" in query:
			os.system('cmd /c "start ms-callrecording:"')
			os.system('cmd /c "pause"')
		elif "settings" in query:
			os.system('cmd /c "start ms-settings:"')
			os.system('cmd /c "pause"')
		elif ("weather" in query or "temperature" in query) :
			try:
				if " in " in query:
					query=query.replace(query,query[query.index(" in ")+4:])
				else:
					with urlopen("https://geolocation-db.com/json") as url:
						data = json.loads(url.read().decode())
						query=data['city']
				command="what is the current weather in "+query
				reg_ex = re.search('current weather in (.*)', command)
				if reg_ex:
					city = reg_ex.group(1)
					owm = OWM(API_key='ab0d5e80e8dafb2cb81fa9e82431c1fa')
					obs = owm.weather_at_place(city)
					w = obs.get_weather()
					k = w.get_status()
					x = w.get_temperature(unit='celsius')
					print('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (city, k, x['temp_max'], x['temp_min']))
					speak('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (city, k, x['temp_max'], x['temp_min']))
			except:
				os.system('cmd /c "start bingweather:"')
				os.system('cmd /c "pause"')
		elif "shareit" in query:
			os.system('cmd /c "C:\Program Files (x86)\SHAREit Technologies\SHAREit\SHAREit.exe"')
			os.system('cmd /c "pause"')
		elif any(c in query for c in checkList5):
			os.system('cmd /c "fsquirt"')
			os.system('cmd /c "pause"')
		elif "bluetooth" in query:
			os.system('cmd /c "start ms-settings-bluetooth:"')
			os.system('cmd /c "pause"')
		elif "open screenshots" in query:
			os.system('cmd /c start "title" "PATH FOR SCREENSHOTS"')
			os.system('cmd /c "pause"')
		elif "file" in query:
			os.system('cmd /c "explorer"')
			os.system('cmd /c "pause"')
		elif "wordpad" in query:
			os.system('cmd /c "write"')
			os.system('cmd /c "pause"')
		elif "notepad" in query:
			os.system('cmd /c "notepad"')
			os.system('cmd /c "pause"')
		elif "powerpoint" in query:
			os.system('cmd /c "start powerpnt"')
			os.system('cmd /c "pause"')
		elif "zoom" in query:
			os.system('cmd /c "magnify"')
			os.system('cmd /c "pause"')
		elif "magnify" in query:
			os.system('cmd /c "magnify"')
			os.system('cmd /c "pause"')
		elif "clear" in query:
			os.system('cmd /c "cls"')
		elif "sleep" in query:
                #go to edit power plan, click on "change advanced power settings" and change "Turn off hard disk after" "On battery and Plugged in" to "never"
                        os.system('cmd /c "cmd /c rundll32.exe powrprof.dll,SetSuspendState 0,1,0"')   
		elif "stop shutdown" in query:
			os.system('cmd /c "shutdown /a" ')
		elif "stop scheduled" in query:
                        if "shutdown" in query:
                                os.system('cmd /c SCHTASKS /Delete /TN "auto shutdown my computer"')
                        if "hiberna" in query:
                                os.system('cmd /c SCHTASKS /Delete /TN "auto hibernate my computer"')
		elif any(c in query for c in checkList7): 
                        try:
                                hr=0
                                mi=0
                                se=0
                                qhInd=0
                                qmInd=0
                                qsInd=0
                                query=query.replace("to","2")
                                if any(c in query for c in checkList9):		
                                        qMod=query.split(" ")
                                        if "pm" in query:
                                                query=query.replace("pm","")   
                                                if "hours" in query:
                                                        qhInd=qMod.index("hours")
                                                elif "hour" in query:
                                                        qhInd=qMod.index("hour")											   
                                                if qhInd!=0:
                                                        hr=int(qMod[qhInd-1])
                                                        if hr<12:
                                                                hr=hr+12										   
                                        else:
                                                query=query.replace("am","")
                                                if "hours" in query:
                                                        qhInd=qMod.index("hours")
                                                elif "hour" in query:
                                                        qhInd=qMod.index("hour")											   
                                                if qhInd!=0:
                                                        hr=int(qMod[qhInd-1])
                                        if "minutes" in query:
                                                qmInd=qMod.index("minutes")
                                        elif "minute" in query:
                                                qmInd=qMod.index("minute")
                                        if qmInd!=0:
                                                mi=int(qMod[qmInd-1])
                                        if hr<10:
                                                hr="0"+str(hr)
                                        if mi<10:
                                                mi="0"+str(mi)
                                        cmdStr=str(hr)+":"+str(mi)
                                        if "hibernate at" in query:
                                                os.system('cmd /c schtasks /create /sc once /tn "auto shutdown my computer" /tr "shutdown -h" /st %s' %cmdStr)
                                        elif "shutdown at" in query:
                                                os.system('cmd /c schtasks /create /sc once /tn "auto shutdown my computer" /tr "shutdown -s" /st %s' %cmdStr)
                                        elif "hibernate after" in query:
                                                hr=int(datetime.datetime.now().strftime("%H"))+hr
                                                mi=int(datetime.datetime.now().strftime("%M"))+mi
                                                os.system('cmd /c schtasks /create /sc once /tn "auto hibernate my computer" /tr "shutdown -h" /st %s' %cmdStr)
                                        elif "shutdown after" in query:
                                                hr=int(datetime.datetime.now().strftime("%H"))+hr
                                                mi=int(datetime.datetime.now().strftime("%M"))+mi
                                                os.system('cmd /c schtasks /create /sc once /tn "auto shutdown my computer" /tr "shutdown -s" /st %s' %cmdStr)
                                        elif any(c in query for c in checkList8):    
                                                speak("Could you please tell the number of seconds?")
                                                ts=takeCommand()
                                                ts=ts.replace("seconds","")
                                                ts=ts.replace("second","")
                                                if "hibernate" in query:
                                                        t=thr.Timer(int(ts),lambda:os.system('cmd /c shutdown -h'))
                                                if "shutdown" in query:
                                                        t=thr.Timer(int(ts),lambda:os.system('cmd /c shutdown -s'))
                                                t.start()
                                else:
                                        if "hibernate" in query:
                                             os.system('cmd /c shutdown -h')
                                        elif "shutdown" in query:
                                             os.system('cmd /c shutdown -s')
                        except Exception as e:
                             print(e)
                             speak("Sorry! Cannot hibernate")
		elif "log" in query:
			query=query.replace(" ","")
			if "logout" in query:
				os.system('cmd /c "shutdown /l" ')
			elif "logoff" in query:
				os.system('cmd /c "shutdown /l" ')
		elif "restart" in query:
			os.system('cmd /c "shutdown /r" ')
		elif "screenshot" in query:
			snapshot = ImageGrab.grab()
			strTime=datetime.datetime.now().strftime("%d%m%y%H%M%S")
			SSTime="SSTimed"+strTime+".jpg"
			SSPath = "PATH FOR SCREENSHOTS"+SSTime
			snapshot.save(SSPath)
		elif "note" in query:
			if "take" in query or "write" in query:
				content=""
				speak("Do you want to speak content")
				ask=takeCommand().lower()
				if "s" in ask:
					content=takeCommand()
				else:
					speak("Enter content")
					content=input("Enter content:")
				f = open('note.txt','a')
				f.write(content+'\n')
				f.close()			
			elif "open" in query or "read" in query:
				f = open('note.txt','r')
				s=f.read()
				print(s)
				f.close()
		elif("screen" in query and "record" in query):
			os.system('cmd /c "C:\\Program Files (x86)\\Bandicam\\bdcam.exe"')
			os.system('cmd /c "pause"')
		elif "code blocks" in query:
			os.system('cmd /c  "C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe"')
			os.system('cmd /c "pause"')
		elif "android studio" in query:
			os.system('cmd /c "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"')
			os.system('cmd /c "pause"')
		elif "visual studio" in query:
			os.system('cmd /c start "title" "C:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Community\\Common7\\IDE\\devenv.exe"')
			os.system('cmd /c "pause"')
		elif "latex" in query:
			os.system('cmd /c start "title" "C:\\Users\\HarshaVenkat\\AppData\\Local\\Programs\\MiKTeX 2.9\\miktex\\bin\\x64\\miktex-texworks.exe"')
			os.system('cmd /c "pause"')			
		elif ("kill" in query or "close" in query):#after "kill yourself" to close voice assistant
			query=query.replace("kill","")
			query=query.replace("task","")
			query=query.replace("dot",".")
			query=query.replace("close","")
			try:
				if query!="":
					if ".exe" not in query:
						query=query+".exe"
				else:
					query=takeCommand()
					if ".exe" not in query:
						query=query+".exe"
				os.system('cmd /c taskkill>NUL /F /IM'+query)
			except Exception as e:
				print(e)
				speak("Please tell the name of process to be killed")
				query=takeCommand()
				os.system('cmd /c tasklist')
				query=query.replace("dot",".")
				if query!="":
					if ".exe" not in query:
						query=query+".exe"
				else:
					query=takeCommand()
					if ".exe" not in query:
						query=query+".exe"
				os.system('cmd /c taskkill>NUL /F /IM ',+query)
			speak("closed"+query.replace(".exe",""))
		elif "open email" in query:
			try:
				url="https://mail.google.com/mail/u/0/#inbox?compose=new"
			except Exception as e:
				print(e)
				speak("Sorry, cannot open mail")
			chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
			webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path),1)
			webbrowser.get('chrome').open_new_tab(url)
			os.system('cmd /c "pause"')
		elif "email" in query:#import csv of google contacts from "https://contacts.google.com/frequent"
			qList=query.split(" ")
			rcp=""
			eInd=qList.index("email")
			eInd=eInd+2
			to_email=[]
			if qList[eInd]!="":
				rcp=qList[eInd]
				for i in range(eInd+1,len(qList)):
					rcp=rcp+qList[i]
				to_email.append(rcp)
			elif qList[eInd+1]!="to":
				rcp=qList[eInd]
				for i in range(eInd+1,len(qList)):
					rcp=rcp+qList[i]
					to_email.append(rcp)
			else:
				break
			while 1:
				speak("Are there any receipents")
				choice=takeCommand()
				choice=choice.lower()
				if 's' in choice:
					speak("Who is the receipent")
					rcp=takeCommand()
					rcp=rcp.lower()
					to_email.append(rcp)
					#if the voice assistant recognises incorrectly
					"""speak("Do you want to enter the receipent")
					ask=takeCommand()
					ask=ask.lower()
					if "s" in ask:
						rcp=input("Enter receipent:")
					to_email.append(rcp)"""
				else:
					break
	#to_email has list of receipents to be verified. While checking, if not present, ask for id
			to=""
			print(to_email)
			try:
				df = pd.read_csv('"C:\\Users\\HarshaVenkat\\Desktop\\Extras\\Harsha\\"+contacts.csv')
				eCol= df['E-mail 1 - Value']
				for rcp in to_email:
					flag=0
					for c in range(0,len(eCol)-1):
						if not pd.isnull(eCol[c]):
							if rcp in eCol[c]:
								to_email[to_email.index(rcp)]=eCol[c]
								flag=1
					if flag==0:
						speak("Enter mail id of receipent"+rcp)
						to=input("Enter mail id of receipent %s:" %rcp)
						to_email[to_email.index(rcp)]=to
				print(to_email)
				speak("Enter content")
				content=input("Enter content: ")#Can change to speak("Enter content") and then call takeCommand() 
				msg = MIMEMultipart()
				speak("Please tell subject")
				msg['Subject'] = takeCommand()
				s = smtplib.SMTP_SSL('smtp.gmail.com',465)
				email_user="abc@gmail.com"#mail id of user
				pass_user="abc@123"#password of user
				s.login(email_user, pass_user)
				msg['From'] = email_user
				msg['To']=", ".join(to_email)
				txt = MIMEText(content)
				msg.attach(txt)
				speak("Do you want to attach any files")
				choice=takeCommand().lower()
				if "s" in choice:
					attachment=[]
					nf=int(input("Enter number of files:"))
					for i in range(0,nf):
						attachment.append(input("Enter file path or drag and drop file:").replace('"',''))
					for f in attachment:
						with open(f, 'rb') as a_file:
							basename = os.path.basename(f)
							part = MIMEApplication(a_file.read(), Name=basename)

						part['Content-Disposition'] = 'attachment; filename="%s"' % basename
						msg.attach(part)
				s.send_message(msg)
				s.quit()
				speak("Email has been sent")
			except Exception as e:
				print("E-mail cannot be sent due to error: %s" %e)
		elif "mail" in query:
			try:
				url="gmail.com"
			except Exception as e:
				print(e)
				speak("Sorry, cannot open mail")
			chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
			webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path),1)
			webbrowser.get('chrome').open_new_tab(url)
			os.system('cmd /c "pause"')
		elif "what is" in query:
			query=query.replace("what is ","")
			webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % query)
			os.system('cmd /c "pause"')
		elif "tell" in query:
			rList=["tell me about", "tell about","tell me"]
			if any(c in query for c in rList):
				query=query.split(c)[1]
			webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % query)
			os.system('cmd /c "pause"')
		elif any(c in query for c in checkList10):
			webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % query)
			os.system('cmd /c "pause"')
		elif "open" in query:
			c=query.replace("open","")
			speak("Sorry! I don't have your query in my database. Do you want me to search in google")
			query=takeCommand().lower()
			if "s" in query:
				webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % c)
				os.system('cmd /c "pause"')
	speak("Thanks for visiting.")
if __name__ == '__main__':
	try:
		cList=recognise.shoot()
	except:
		speak("Sorry, error while recognising.")
		print("Sorry, error while recognising.")
		exit()
		#cList=recognise.shoot()
	for i in cList:
		if "(2)" in i:
			cList[cList.index(i)]=i.replace("(2)","")
	if len(cList)==0:
		speak("Sorry, Access Denied")
		exit()
	for i in cList:
		speak("Hi"+i)
	speak("Good to see you again. How can I help you?")
	#wishMe()
	p1 = Process(target = VA)
	p1.start()
	p2 = Process(target = call)
	p2.start()
	p1.join()
	p2.join()
