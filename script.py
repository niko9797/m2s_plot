#!/usr/bin/python3
import linecache, sys, os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def searchdata (line, program, num_cfg):
	#Gathers all the data from report files
	config=1
	res=()

	while (config<=num_cfg):
		#Each file is read and added to a array
		data = "./reports/report_" + str(program) + "-" + str(config)+ ".txt"
		desiredline = linecache.getline(data, int(line))
		desiredvalue = desiredline.split("=")[1]
		desiredvalue2 = desiredvalue.split("\\")[0]
		res = res + (float(desiredvalue2), )
		config=config+1
	return res

if __name__ == "__main__":
	#Get arguments and init variables
	line = int(sys.argv[1])
	count = 1
	data = ()

	#Get programs name and number of configs, needs sorted to have alphanumerical order
	program_names = sorted(os.listdir("./test/"))
	program_cfg = sorted(os.listdir("./cfg/"))

	#Read all of programs config result
	while (count<=len(program_names)):
		data = data +(searchdata(line, count, len(program_cfg)), )
		#print(data)
		count+=1
	
	#Plot bars
	color_list = ['black', 'green', 'red', 'blue', 'yellow', 'brown']
	gap = .8 / len(data)
	for i, row in enumerate(data):
		X = np.arange(len(row))
		plt.bar(X + i * gap, row,
			width = gap,
			color = color_list[i % len(color_list)],
			label = program_names[i])
	plt.yscale('log')

	#Get name of the config and ad it in y plot axis
	desiredline = linecache.getline("./reports/report_1-1.txt", line)
	
	desiredvalue = desiredline.split("=")[0]
	plt.ylabel(desiredvalue)
	ax = plt.subplot(111)
	box = ax.get_position()
	ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])

	# Put a legend below current axis
	ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=len(program_names))
	plt.show()
	print(data)
