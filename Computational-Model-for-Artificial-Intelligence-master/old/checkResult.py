import csv



def outputToCSV(extractFile, stateI, stateF, csvFilename):
	# Extract information from output file
	with open(extractFile, 'r') as myfile:
		data = myfile.read().replace('\n', '')
		data = data.strip()

	finalList = []
	strSplit = data.split("------------------------- Trial #")

	for line in strSplit:
		if line.find("State " + str(stateI) + " -> State " + str(stateF)) != -1:
			lastStrLoc = line.find("State " + str(stateI) + " -> State " + str(stateF))
			strToFind = line[:int(lastStrLoc)]
			tempEnd = strToFind[strToFind.rfind("<")+1:]
			outputSymbol = tempEnd[:tempEnd.index(">")]
			finalList.append(str(line[0:line.find(" ")] + ":" + str(outputSymbol)))
	print(finalList)

	# Info to CSV
	with open(csvFilename, 'wb') as myfile:
		out = csv.writer(open(csvFilename,"w"), delimiter=',',quoting=csv.QUOTE_ALL)
		out.writerow(finalList)
		

if __name__ == "__main__":
	extractFile = "delayedOutput.txt"
	stateI = 0
	stateF = 8
	csvFilename = "testCSV.csv"
	
	getOutputResults(extractFile, stateI, stateF, csvFilename)