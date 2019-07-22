from bs4 import BeautifulSoup
#         meta.decompose()


def processHTML(htmlpath):
	f = open(htmlpath, "r",  encoding="utf8")
	contents = [line.rstrip('\n') for line in f]
	f.close()
	# contents.insert(10, '<link rel="stylesheet" type="text/css" href="/assets/style.css">')
	# contents.insert(11, '<script async type="text/javascript" src="/assets/webgazer.js"></script>')
	inject = open('inject.html', 'r', encoding="utf8")
	contents_inject= inject.readlines()
	contents.insert(20, "".join(contents_inject))
	f= open(htmlpath, "w",  encoding="utf8")
	contents= "".join(contents)
	f.write(contents)
	f.close()

# def processHTML(htmlpath):
# 	f = open(htmlpath, "r",  encoding="utf8")
# 	contents = [line.rstrip('\n') for line in f]
# 	f.close()
# 	# contents.insert(10, '<link rel="stylesheet" type="text/css" href="/assets/style.css">')
# 	# contents.insert(11, '<script async type="text/javascript" src="/assets/webgazer.js"></script>')
# 	inject = open('inject.html', 'r', encoding="utf8")
# 	contents_inject= inject.readlines()
# 	contents.insert(20, "".join(contents_inject))
# 	f= open('test.html', "w",  encoding="utf8")
# 	contents= "".join(contents)
# 	f.write(contents)
# 	f.close()