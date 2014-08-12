# def savePic(url):
#     hs = hashlib.sha224(url).hexdigest()
#     file_extension = url.split(".")[-1]
#     uri = ""
#     dest = uri+hs+"."+file_extension
#     print dest
#     try:
#         urllib.urlretrieve(url,dest)
#     except:
#         print "save failed"
#
#
# savePic(image)




# g_data = soup.find_all("div" , {"class" : "img-wrapper"})


# Use something like this to download all the images from SomeCard
# for link in links:
#   if "http" in link.get("href"):
#     # print link



#
#
# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#
# print bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC
