from engine import *

def inputIn(count, exp):
	inputStr = createInput(exp)

	Iin = []
	
	lines = inputStr.split("\n")
	for line in lines:
		userInput = line.strip()
		Iin.append(formatLine(userInput))

	return Iin

def formatLine(line):

	Iin = []
	userInput = line.strip()
	# print(line)
	quit = ['quit','q']
	if userInput == "" or userInput == "EPSILON":
		return ""
	elif (userInput.lower() in quit):
		exit()
	elif userInput.lower() == 'status':
		status = m.PrintModel()
		#print(status)
		SaveStatusToFile(status)
		return GetInput()
	else:
		pairs = userInput.split(',')
		count = 0
		for pair in pairs:
			toks = pair.split(':')
			if len(toks) == 1:
				Iin = Iin +[[toks[0],1.0]]
			else:
				Iin = Iin+[[toks[0],float(toks[1])]]
			count += 1
	print(Iin)
	return Iin

def createInput(exp):
	res = ""
	
	if exp == 2:
		for i in range(40):
			res += "\ncs1+:1.0"
			res += "\nucs+:1.0"
			res += "\ncs1-:1.0"
			res += "\nucs-:1.0"
			res += "\nEPSILON"
	return res


if __name__ == "__main__":
	print(inputIn(0, 2))