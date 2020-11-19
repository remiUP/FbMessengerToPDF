import tkinter as tk
from tkinter import filedialog
from fpdf import FPDF
from os.path import isfile
import json
import datetime
from random import randrange
import re

test_path = "E:\\Files\\Programming\\FbMessengerToPDF\\data\\messages\\inbox\\AliseGilot_A6kYU9nD4A"

# colors = {'name':[fillColor[],drawColor[],textColor[]], ...}


def promptFolder():
	root = tk.Tk()
	root.withdraw()
	file_path = filedialog.askdirectory()
	return file_path

def load_participants(path):
	participants = []
	with open(path + '\\message_1.json') as d:
		temp = json.load(d)['participants']
		for p in temp:
			participants.append(p['name'])
	return participants

def load_messages(path):
    data = []
    i=1
    while isfile(path + '\\message_'+str(i)+'.json'):
        with open(path + '\\message_'+str(i)+'.json') as d:
            data += json.load(d)['messages']
        i+=1
    cache = sorted(data, key=lambda message : message['timestamp_ms'])
    return cache

def decode(s):
    try:
        #res = unidecode(unicode(s,encoding='latin1'),decode='utf8')
        res = remove_emoji(s.encode('latin1',errors='ignore').decode('utf8'))
    except:
        res = ''
    return res

def remove_emoji(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

def setRandomColors(participants):
	colors = dict()
	for person in participants:
		colors[person]= [[randrange(200,255),randrange(200,255),randrange(200,255)],
						[randrange(0,100),randrange(0,100),randrange(0,100)],
						[0,0,0]]
	return colors

def printMsg(item,colors,pdf):
	if item['type']=='Generic':
		pdf.set_fill_color(colors[item['sender_name']][0][0], colors[item['sender_name']][0][1], colors[item['sender_name']][0][2])
		pdf.set_draw_color(colors[item['sender_name']][1][0], colors[item['sender_name']][1][1], colors[item['sender_name']][1][2])
		pdf.set_text_color(colors[item['sender_name']][2][0], colors[item['sender_name']][2][1], colors[item['sender_name']][2][2])
		pdf.multi_cell(0,10,txt=decode(item['content']),border=1 , fill=True)
		pdf.ln()

def makePDF(path):
	data = load_messages(test_path)
	pdf = FPDF(orientation="P",unit='mm',format='A4')
	#pdf.set_doc_option('core_fonts_encoding', 'utf-8')
	#pdf.set_doc_option('core_fonts_encoding', 'windows-1252')
	
	#pdf.set_auto_page_break(True)
	pdf.add_page()
	pdf.add_font('DejaVu', '', "C:\\Users\\remiUP\\AppData\\Local\\Microsoft\\Windows\\Fonts\\DejaVuSansCondensed.ttf", uni=True)
	#pdf.set_font('DejaVu','',12)
	pdf.set_font('Arial','',12)
	colors = setRandomColors(load_participants(path))
	for x,item in enumerate(data[:100]):
		try:
			printMsg(item,colors,pdf)
		except:
			print(decode(item['content']))
			print(x)
			break
	pdf.output("test.pdf")

if __name__ == "__main__":
	makePDF(test_path)
