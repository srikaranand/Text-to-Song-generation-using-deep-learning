from gtts import gTTS 
from pydub import AudioSegment
from selenium import webdriver
from time import sleep
import os 
import glob


AudioSegment.converter = "C:\\Program Files\\ffmpeg-20191202-968c4cb-win64-static\\bin\\ffmpeg.exe"
AudioSegment.ffmpeg = "C:\\Program Files\\ffmpeg-20191202-968c4cb-win64-static\\bin\\ffmpeg.exe"
AudioSegment.ffprobe ="C:\\Program Files\\ffmpeg-20191202-968c4cb-win64-static\bin\\ffprobe.exe"


buffer = []
file = open("lyrics.txt","r")
lyrics=file.read()
file.close()
lyrics=lyrics.split("\n")
for line in lyrics:
    buffer.append(line)
multiline_string = "\n".join(buffer)
  
myobj = gTTS(text=multiline_string, lang='en', slow=False) 
  
myobj.save("output_.mp3") 

def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')
print(get_download_path())

sleep(1)

driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

print(glob.glob(get_download_path()+"\*.mid"))
fn=glob.glob(get_download_path()+"\*.mid")
fn=fn[0]

value = fn

driver.get("https://www.onlineconverter.com/midi-to-mp3")
input_element = driver.find_element_by_id("file")
input_element.send_keys(value)

button_element = driver.find_element_by_id("convert-button")
button_element.click()


sleep(20)


url = driver.find_element_by_id("convert-message")
element = url.find_element_by_css_selector("a").get_attribute("href")
print(element)


driver.get(element)

sleep(5)

print(glob.glob(get_download_path()+"\*.mp3"))
fn=glob.glob(get_download_path()+"\*.mp3")
fn=fn[0] #output of the first music file generated
print(fn)

#os.system("start output_.mp3") 
#os.system("start "+fn) 


print('ch1')
sound1 = AudioSegment.from_file("output_.mp3")
print('ch2')

sound2 = AudioSegment.from_file(fn)
print('ch3')
combined = sound1.overlay(sound2)
print('ch4')
combined.export("FinalMusic.mp3", format='mp3')

os.system("start FinalMusic.mp3") 
