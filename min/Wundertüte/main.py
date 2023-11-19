_A='output.txt'
from tkinter import*
import re
userinputs=[]
class UserInput:
	def ask_all():UserInput.ask('Amount of lucky bags');UserInput.ask('Amount of dice games');UserInput.ask('Amount of card games');UserInput.ask('Amount of skill games');return userinputs
	def ask(what):
		userinput=input(f"[96m{what}:[0m")
		if userinput.isdigit():userinputs.append(int(userinput))
		else:print("\x1b[91mYou didn't enter a valid number. Please enter a number.\x1b[0m");UserInput.ask(what)
class TextControl:
	@staticmethod
	def create_framework(lucky_bags):
		with open(_A,'a')as file:
			f=open(_A,'r+');f.truncate(0)
			for i in range(0,lucky_bags):zeile=f"Luckybag {i+1}:\n";file.write(zeile)
	@staticmethod
	def add_data(line,text,id=None):
		file_path=_A
		if id is None:raise ValueError('Invalid ID')
		with open(file_path,'r')as file:lines=file.readlines()
		text=f"[{id};{text}]";lines[line-1]=lines[line-1].rstrip('\n')+' '+text+'\n'
		with open(file_path,'w')as file:file.writelines(lines)
	@staticmethod
	def remove_data(id):
		file_path=_A
		if id is None:raise ValueError
		with open(file_path,'r')as file:lines=file.readlines()
		for(i,line)in enumerate(lines):pattern=re.compile(f"\\[{id};.*?\\]");lines[i]=re.sub(pattern,'',line)
		with open(file_path,'w')as file:file.writelines(lines)
	@staticmethod
	def get_line_data(line):
		file_path=_A
		with open(file_path,'r')as file:lines=file.readlines()
		if 1<=line<=len(lines):data_in_brackets=re.findall('\\[\\d+;(.*?)\\]',lines[line-1]);return data_in_brackets
		else:return
	@staticmethod
	def get_id_for_data_in_line(line,data):
		file_path=_A
		with open(file_path,'r')as file:lines=file.readlines()
		if 1<=line<=len(lines):
			pattern=re.compile(f"\\[(\\d+);{re.escape(data)}\\]");match=re.search(pattern,lines[line-1])
			if match:return int(match.group(1))
			else:return
		else:return
	@staticmethod
	def replace_data(id,new_text):
		file_path=_A
		with open(file_path,'r')as file:lines=file.readlines()
		for(line_num,line)in enumerate(lines,start=1):
			pattern=re.compile(f"\\[{id};.*?\\]");match=re.search(pattern,line)
			if match:
				lines[line_num-1]=re.sub(pattern,f"[{id};{new_text}]",line)
				with open(file_path,'w')as file:file.writelines(lines)
				return
class Result:
	@staticmethod
	def showresult():
		root=Tk();root.title('Your result is here! - Distributor (Wundertüte)');root.geometry('600x400');root.iconbitmap('img\\icon.ico');root.attributes('-topmost',True);message=open(_A,'r').read()
		def on_closing():root.quit()
		root.protocol('WM_DELETE_WINDOW',on_closing);text_box=Text(root,height=30,width=100);text_box.pack(expand=True);text_box.insert('end',message);text_box.config(state='disabled');root.mainloop()
print('All work is copyrighted by GNU GENERAL PUBLIC LICENSE. View the License (in main directory) for more information.')
inputs=UserInput.ask_all()
dice_games_left=inputs[1]
card_games_left=inputs[2]
skill_games_left=inputs[3]
line=0
id=0
missed=[]
print('\x1b[93mStarted. Please wait...')
print('Press CTRL+C to cancel\x1b[0m')
TextControl.create_framework(inputs[0])
for dice_game in range(1,dice_games_left+1):
	if line==inputs[0]:line=1
	else:line+=1
	TextControl.add_data(line,'Dice Game',id);id+=1
for card_game in range(1,card_games_left+1):
	if line==inputs[0]:line=1
	else:line+=1
	TextControl.add_data(line,'Card Game',id);id+=1
for skill_game in range(1,skill_games_left+1):
	if line==inputs[0]:line=1
	else:line+=1
	TextControl.add_data(line,'Skill Game',id);id+=1
if line!=inputs[0]:
	for i in range(line+1,inputs[0]+1):TextControl.add_data(i,'missed',id);missed.append(id);id+=1
for missed in missed:TextControl.remove_data(missed)
print('\x1b[92mYour result is here! View output.txt\x1b[0m')
Result.showresult()