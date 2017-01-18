import os

from os.path import basename
from collections import Counter
import subprocess

complexityDic = {}
repository = "./"


def linesInFile(filePath):
    i = 0
    with open(filePath) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def calculateComplexity(folder):
	for root, dirs,files in os.walk(folder, topdown=True):
    		for name in files:
			if ".java" in name:
				fullPath = os.path.join(root, name)				
				lines = linesInFile(fullPath)
				complexityDic[name] = lines	

def calculateChurn():
	dataResult = ""	
	output = os.popen("git log --all --pretty=format: --name-only | grep .java | sed 's/.*\///'  | sort | uniq -c | sort -rg").read().split()
	count = 0

	while (count < len(output)-2):
	   fileName=output[count+1]
	   frequency=output[count]
	   if fileName in complexityDic:
	   	dataResult = dataResult + "[%s,%s,'%s']," % (frequency,complexityDic[fileName],fileName)	
	   count = count + 2
	dataResult = dataResult[0:len(dataResult)-1]
	return dataResult

def gererate(dataResult):
	file = open('template.html')
	
	contents = file.read()
	replaced_contents = contents.replace('##placeholder##', dataResult)

	fileResult = open("result.html", "w")
	fileResult.write(replaced_contents)

	file.close()
	fileResult.close()


calculateComplexity(repository)
result = calculateChurn()
gererate(result)
