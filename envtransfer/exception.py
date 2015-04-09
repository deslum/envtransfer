import urllib2



def excpt(func):
	def new_func(*args):
		try:
			if func.__name__ in 'uploadFile':
				print "Start upload file"
				func(*args)
				print "File successfully uploaded..."
			elif func.__name__ in 'downloadFile':
				print "Start download file"
				func(*args)
				print "File successfully downloaded..."
			else:
				func(*args)
			return new_func
		except urllib2.URLError:
			print "Error connection"
		except IOError:
			print "File error"
		except TypeError:
			print "Token not found. Please generate token 'envtransfer auth'"
	return new_func
