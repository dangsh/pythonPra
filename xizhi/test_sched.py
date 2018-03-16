import time , os , sched
schedule = sched.scheduler(time.time , time.sleep)

def perform_command(cmd , inc):
	os.system(cmd)

def timming_exe(cmd , inc = 60):
	schedule.enter(inc , 0 , perform_command , (cmd , inc))
	schedule.run()

print("show time after 10s")
timming_exe("echo %time%" , 10)