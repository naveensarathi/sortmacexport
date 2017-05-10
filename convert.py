#!/usr/local/bin/python3
#Name:convert.py
#Version 1.x
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


source_folder = sys.argv[1]
# Open Log File
log_filename=os.getcwd()+"/convert_fl.log"
log=open(log_filename,'w')
all_folder_names=os.listdir(source_folder)
log.write("list files and folder found = %s\n" %all_folder_names)
exclude_name = (".DS_Store" , "converted")
real_folder=[]
excluded_folders=[]


def rename_folder(folder):
	*location , datestr = folder.split(',')
	time_str = time.strptime(datestr.strip(), "%d %B %Y")
	new_time_str= time.strftime("%Y-%m-%d",time_str)
	src=source_folder+folder
	dst=source_folder+new_time_str
	log.write("FolderRename |%s| => |%s|\n" %(src,dst) )
	shutil.move(src,dst)
	#print (src+" -> "+dst)



def move_to_exsisting(folder):
	*location , datestr = folder.split(',')
	time_str = time.strptime(datestr.strip(), "%d %B %Y")
	new_time_str= time.strftime("%Y-%m-%d",time_str)
	src=source_folder+folder
	dst=source_folder+new_time_str
	allfiles=os.listdir(src)
	for every_file in allfiles:
		src1=src+"/"+every_file
		dst1=source_folder+new_time_str+"/"
		log.write("FilesRename |%s| => |%s|\n" %(src1,dst1) )
		shutil.move(src1,dst1)
		#print (src1+" to "+"->"+dst1 )







for folder in list(all_folder_names):
	if folder not in exclude_name:
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
