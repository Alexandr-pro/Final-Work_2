#-------------------------------------------------------------------------------
# File             : Notes.py
# Description      : Working with notes
# Author           : Alexander Kozhan
# Version          : 01
# Date             : 27.06.2023
# Last update      : 29.06.2023
#-------------------------------------------------------------------------------

import json
import datetime
import os


#                  ======
#                  System
#                  ======

#-------------------------------------------------------------------------------
# Name        : ClearScreen
# Description : Clear screen
#-------------------------------------------------------------------------------
def ClearScreen():
  os.system('cls')
#-------------------------------------------------------------------------------


#                  ==
#                  IO
#                  ==

#-------------------------------------------------------------------------------
# Name        : FileWrite7
# Description : Writing 7 notes to file
# Parameters  :
#               fname - file name
#-------------------------------------------------------------------------------
def FileWrite7(fname):
  data = []  
  data.append({'id': 1, 'head': 'note 1', 'body': 'body 1', 'dt': '2023-10-10 05:45:23.267781'})
  data.append({'id': 2, 'head': 'note 2', 'body': 'body 2', 'dt': '2023-10-10 05:45:23.267781'})
  data.append({'id': 3, 'head': 'note 3', 'body': 'body 3', 'dt': '2023-10-10 05:45:23.267781'})
  data.append({'id': 4, 'head': 'note 4', 'body': 'body 4', 'dt': '2023-10-10 05:45:23.267781'})
  data.append({'id': 5, 'head': 'note 5', 'body': 'body 5', 'dt': '2023-10-10 05:45:23.267781'})
  data.append({'id': 6, 'head': 'note 6', 'body': 'body 6', 'dt': '2023-10-10 05:45:23.267781'})
  data.append({'id': 7, 'head': 'note 7', 'body': 'body 7', 'dt': '2023-10-10 05:45:23.267781'})
  with open(fname, 'w') as outfile:
    json.dump(data, outfile)  
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
# Name        : FileWrite
# Description : Writing all notes to file
# Parameters  :
#               data - json data
#               fname - file name
#-------------------------------------------------------------------------------
def FileWrite(data, fname):  
  with open(fname, 'w') as outfile:
    json.dump(data, outfile)  
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
# Name        : FileRead
# Description : Reading all notes from file & return json object
# Parameters  :
#               fname - file name
#-------------------------------------------------------------------------------
def FileRead(fname):
  with open(fname, 'r') as infile:
    data = json.load(infile)
  return data
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
# Name        : FilterNotes
# Description : Filter the notes by date & return new notes
# Parameters  :
#               data - json data
#               date - date for filter
#-------------------------------------------------------------------------------
def FilterNotes(data, date):
  fdata = []
  for d in data:
    ndate = datetime.datetime.strptime(d['dt'], '%Y-%m-%d %H:%M:%S.%f')
    if ndate.date() == date:
      fdata.append(d)
  return fdata
#-------------------------------------------------------------------------------

             
#-------------------------------------------------------------------------------
# Name        : PrintNotes
# Description : Print all the notes
# Parameters  :
#               data - json data
#-------------------------------------------------------------------------------
def PrintNotes(data):
  for d in data:
    print(d['id'], ' ', d['head'], d['body'], ' ', d['dt'])
#-------------------------------------------------------------------------------


#                  =====
#                  Notes
#                  =====

#-------------------------------------------------------------------------------
# Name        : AddNote
# Description : Add new note
# Parameters  :
#               data - json data
#-------------------------------------------------------------------------------
def AddNote(data):
  id = len(data) + 1
  head = input('Input head: ')
  body = input('Input body: ')
  dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
  d = {'id': id, 'head': head, 'body': body, 'dt': dt}
  data.append(d) 
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
# Name        : EditNote
# Description : Edit note
# Parameters  :
#               data - json data
#               id - note's id
#-------------------------------------------------------------------------------
def EditNote(data, id):
  for d in data:
    if d['id'] == id:
      head = input('Input new head: ')
      body = input('Input new body: ')      
      d['head'] = head
      d['body'] = body
      d['dt'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
#-------------------------------------------------------------------------------
          

#-------------------------------------------------------------------------------
# Name        : DeleteNote
# Description : Delete note
# Parameters  :
#               data - json data
#               id - note's id
#-------------------------------------------------------------------------------
def DeleteNote(data, id):
  for d in data:
    if d['id'] == id:
      data.remove(d)
      break  
#-------------------------------------------------------------------------------
             

#                  ====
#                  Main
#                  ====

#-------------------------------------------------------------------------------
# Name        : main
# Description : Entrance point
#-------------------------------------------------------------------------------
def main():  
  fname = 'data.json'
  #-----------------------------------------------------------------------------
  #FileWrite7(fname)                              # once only
  #-----------------------------------------------------------------------------
  data = FileRead(fname)
  ClearScreen()
  while True:
    print('****************************************')
    print('1 - Add new note')
    print('2 - Edit note')
    print('3 - Delete note')
    print('4 - Print all notes')
    print('5 - Print notes for date')
    print('6 - Print note for id')
    print('7 - Read notes from file')
    print('8 - Save notes to file')
    print('q - Exit')
    print('****************************************')    
    c = input('Enter your choice: ')
    if c == '1':      
      AddNote(data)
    elif c == '2':
      id = int(input('Input edited note id: '))
      EditNote(data, id)
    elif c == '3':
      id = int(input('Input id: '))
      DeleteNote(data, id)
    elif c == '4':
      PrintNotes(data)
    elif c == '5':
      s = input('Input date in format YYYY-MM-DD: ')
      date = datetime.datetime.strptime(s, '%Y-%m-%d').date()
      fdata = FilterNotes(data, date)
      PrintNotes(fdata)
    elif c == '6':
      id = int(input('Input note id: '))
      data1 = [d for d in data if d['id'] == id]
      PrintNotes(data1)
    elif c == '7':
      data = FileRead(fname)
    elif c == '8':
      FileWrite(data, fname)
    elif c == 'q':
      break
  return
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Program
main()
#-------------------------------------------------------------------------------
