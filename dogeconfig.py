
#defaults...

keyfile = "config/.keyfile"
portfile = "config/.portfile"
hostfile = "config/.hostfile"

port = 5000
host = '127.0.0.1' # set to '0.0.0.0' to make it available to the outside world
secret_key = 'secret_key'
debug = True



try:
	f = open(keyfile)
	s = f.readline().strip()
	secret_key = s
except:
	print("could not read keyfile, using default")


try:
	f = open(portfile)
	s = f.readline().strip()
	i = int(s)
	port = i
	print("using port " + s)	
except:
	print("could not read port, using default: " + str(port))


try:
	f = open(hostfile)
	s = f.readline().strip()
	host = s
	debug = False
	print("running on " + s)
except:
	print("could not read hostfile, using default: " + host)
	print("debug mode: " + str(debug))

