#import the required modules
import os, glob, time, dirSplit as ds, writeInfo as wi

path = os.getcwd()
path += '/SU2011/'
print(path)

def genIndex():
	#file_name = open(path+'index.html', 'w')
	file_name = open('index.html', 'w')
	wi.writeHeader(file_name)
	
	for folder in glob.glob('*/*/*/'):
		full_path = ds.split(folder)
		root = full_path[0]+"/"+full_path[1]
		course_name = full_path[1]
		student_name = full_path[2]
		lst = []
		lst = folder
		#wi.writeClass(file_name, course_name)
		wi.getPaths(file_name,root,student_name)
		
	print(('Complete'+'\n'))
	wi.writeFooter(file_name)
	file_name.close()
