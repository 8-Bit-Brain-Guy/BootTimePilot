# Show Windows 10 boot time and time to shutdown.
# These times can be loacated manually via ... -> ... -> ...
# This scrpt uses exported Event xml files to grab the appropriate informations: 
# For startup times: ID100 -> MainPathBootTime and BootPostBootTime in milli seconds. The sum of both values can be read from BootTime
# For shutdown times: ID200 -> ShutdownTime in milli seconds.

import xml.etree.ElementTree as ET
import os

# clear command window first
os.system('cls')

start_tree = ET.parse('events_ID100.xml')
shutdown_tree = ET.parse('events_ID200.xml')

start_root = start_tree.getroot()
shutdown_root = shutdown_tree.getroot()

swVersion = '0.1'
print('This is BootTime Version: ' + swVersion + '\n')

# find all occurrences of MainPathBootTime and BootPostBootTime and grab the times
# access the times: 
# elements_MainPathBootTime[0].text

# get all MainPathBootTime elements
elements_MainPathBootTime = start_root.findall(".//*[@Name='MainPathBootTime']")
elements_BootPostBootTime = start_root.findall(".//*[@Name='BootPostBootTime']")
elements_BootTime = start_root.findall(".//*[@Name='BootTime']")
elements_ShutdownTime = shutdown_root.findall(".//*[@Name='ShutdownTime']")

print('Number of elements found:')
print('Number of MainPathBootTimes found: ' + str(len(elements_MainPathBootTime) ))
print('Number of BootPostBootTime found: ' + str(len(elements_BootPostBootTime) ))
print('Number of BootTime found: ' + str(len(elements_BootTime) ))
print('Number of ShutdownTime found: ' + str(len(elements_ShutdownTime) ))
print('\nBootTime is the sum of MainPathBootTime and BootPostBootTime')

print('\nLatest Times in ms:')
print('MainPathBootTime : ' + str(elements_MainPathBootTime[-1].text) )
print('BootPostBootTime : ' + str(elements_BootPostBootTime[-1].text) )
print('BootTime         : ' + str(elements_BootTime[-1].text) )
print('ShutdownTime     : ' + str(elements_ShutdownTime[-1].text) )


# Calculate and show average times:
liste_MainPathBootTime = []
liste_BootPostBootTime = []
liste_BootTime = []
liste_ShutdownTime = []

for i in range(0, len(elements_MainPathBootTime) ) :    
    liste_MainPathBootTime.append( int( elements_MainPathBootTime[i].text) )
    liste_BootPostBootTime.append( int( elements_BootPostBootTime[i].text) )
    liste_BootTime.append( int( elements_BootTime[i].text) )
    
for i in range(0, len(elements_ShutdownTime) ) :        
    liste_ShutdownTime.append( int( elements_ShutdownTime[i].text) )
    

print('\nAverage of Times in ms:')
print('MainPathBootTime average : ' + str( sum(liste_MainPathBootTime) / len(liste_MainPathBootTime) ) )
print('BootPostBootTime average : ' + str( sum(liste_BootPostBootTime) / len(liste_BootPostBootTime) ) )
print('BootTime average         : ' + str( sum(liste_BootTime) / len(liste_BootTime) ) )
print('ShutdownTime average     : ' + str( sum(liste_ShutdownTime) / len(liste_ShutdownTime) ) )


    
# print(type(liste_MainPathBootTime[0]))
# print( liste_MainPathBootTime[0] )
# print( sum(liste_MainPathBootTime) / len(liste_MainPathBootTime) )




# make lists with MainPathBootTimes and BootPostBootTimes



# print times to screen


# save times to textfile or maybe some more user-friendly readable format like an html file













# Environment.SetParameter('SetElementsPath', "./EIF/Segment[Name='DataRAMFree']/Length")

#elements = root.findall(xpath)
#       
#        for item in elements:
#            if element != None and ET.iselement(element) :
#                parent = item.find('..')            
#                if parent == None:
#                    parent = root.find(xpath + '/..')
#                if parent != None:                
#                    parent.remove(item)    
#                    parent.append(element)
#            else:
#                item.text = str(value)
#