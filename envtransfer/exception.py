import urllib2


def function_exception(func):
    def new_func(*args):
        try:
            if func.__name__ == 'upload_file':
                print "Start upload file"
                func(*args)
                print "File successfully uploaded..."
            elif func.__name__ == 'download_file':
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
