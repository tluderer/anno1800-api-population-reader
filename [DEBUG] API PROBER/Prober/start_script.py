import subprocess, sys, os

class Prober:
	def __init__(self):
		self.src_path = "C:/code/anno1800_modding/src"
		self.log_file_path = self.src_path+'/debug.log'
		self.debug("Init")
		

	def debug(self, obj):
		try:
			with open(self.src_path+'/debugger.py', 'r') as py_file:
				exec(py_file.read(), {'DATA': obj, 'LOG_FILE': self.log_file_path})
		except Exception as e:
			print('ERROR:' + str(e))
			with open(log_file_path, 'a') as log_file:
				log_file.write(str(e)+'\n')

	def pressNine(self):
		self.debug(dirs())
	
	def pressEight(self):
		self.debug(locals())	
	
	def pressSeven(self):
		self.debug(globals())
		#Values ?
			
prober = Prober();

