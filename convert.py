#!/usr/local/bin/python3
#Name:convert.py
#Version 1.1
#usage "convert EXPORT_FOLDERNAME"
#EXPORT_FOLDERNAME is the folder name where Mac Photos will export the photos to.
import os
import time
import re
import sys
import locale
import datetime
import shutil

#Counters
removed_folder=0
if (len(sys.argv) <= 1 ):
 print ("USAGE : ./convert EXPORTFOLDERNAME")
 exit()

source_folder = sys.argv[1]
# Open Log File
log_filename=os.getcwd()+"/convert_fl.log"
log=open(log_filename,'w')
all_folder_names=os.listdir(source_folder)
#log.write("list files and folder found = %s\n" %all_folder_names)
exclude_name = ()
real_folder=[]
excluded_folders=[".DS_Store" , "converted"]


def rename_folder(folder):
	*location , datestr = folder.split(',')
	log.write("ren_fol: converting %s," %datestr )
	time_str = time.strptime(datestr.strip(), "%d %B %Y")
	new_time_str= time.strftime("%Y-%m-%d",time_str)
	src=source_folder+folder
	dst=source_folder+new_time_str
	log.write("Renaming folder \t |%s| => |%s|\n" %(src,dst) )
	shutil.move(src,dst)
	#print (src+" -> "+dst)



def move_to_exsisting(folder):
	*location , datestr = folder.split(',')
	log.write("mv_to_ex: converting %s" %datestr )
	time_str = time.strptime(datestr.strip(), "%d %B %Y")
	new_time_str= time.strftime("%Y-%m-%d",time_str)
	src=source_folder+folder
	dst=source_folder+new_time_str
	allfiles=os.listdir(src)
	log.write("Source:%s\n" %src)
	log.write("list %s \n" %allfiles)
	for every_file in allfiles:
		src1=src+"/"+every_file
#		log.write("Source: %s \n", %src1)
		dst1=source_folder+new_time_str+"/"+every_file
#		log.write("Destination: %s \n",%dst1)
		log.write("moving file |%s| => |%s|\n" %(src1,dst1) )
		shutil.move(src1,dst1)
		#print (src1+" to "+"->"+dst1 )




#Start the real job  

#If the folder name already found in YYYY-MM-DD format add the folder to exclude_folder
for folder in list( all_folder_names):
	try:
		isinstance(time.strptime(folder,'%Y-%m-%d'),time.struct_time)
		excluded_folders.append(folder)

	except ValueError:
	  print("%s will be proceed\n" %folder)
	  #log.write("%s will be proceed\n" %folder)



#Check one by one folder for long name , if found rename "long folder name to YYYY-MM-DD " format 
for folder in list(all_folder_names):
	if folder not in excluded_folders:
		log.write("Starting %s "%folder)
		if "," in folder:
			*location , datestr = folder.split(',')
			if datestr in real_folder:
				move_to_exsisting(folder)
				#exsistig_date(folder)
			else:
				real_folder.append(datestr)
				rename_folder(folder)
			#print ( datestr )
		else:
			#print (folder+"is in not correct")
			if folder in real_folder:
				move_to_exsisting(folder)
		
			else:
				rename_folder(folder)
				real_folder.append(folder)
	else:
		excluded_folders.append(folder)

log.close()


#print (real_folder)
#print ("Below are excluded")
#print(excluded_folders)
#print("Removed Folders = "+removed_folder)
