import os,glob,dirSplit as ds

def writeHeader(file_contents):
	file_contents.write('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"'+'\n')
	file_contents.write('"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">'+'\n'+'<html xmlns="http://www.w3.org/1999/xhtml">'+'\n'+'<head>'+'\n')
	file_contents.write('<title>Course Jump Page</title>'+'\n'+'</head>'+'\n'+'<body>'+'\n')
	file_contents.write('<ul>'+'\n')

def writeFooter(file_contents):
	file_contents.write('</ul>'+'\n'+'</body>'+'\n'+'</html>')
	
def getPaths(file_contents,root,student_name):
	for folder in glob.glob('*/*/*/'):
		lst = ('<li><a href="'+root+'/'+student_name+'/index.html">'+student_name+'</a></li>'+'\n')
		#file_contents.write(lst)
		return file_contents.write(lst)

# def writeClass(file_contents, course_name):
# 	if course_name == "GD160":
# 		return file_contents.write('<h1>'+course_name+'</h1>')
# 	if course_name == "IMD240":
# 		return file_contents.write('<h1>'+course_name+'</h1>')
