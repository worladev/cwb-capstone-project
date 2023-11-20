import configparser


# mediaOutlet class has an initializer and there parameters as name, url and location.the name shows the name of
# the media, url contains the web address of the media and the location shows where the news media can be found.
class MediaOutlet:
    def __init__(self, name, url, location):
        self.name = name
        self.url = url
        self.location = location

 #create a method to print media outlet.
 # this function prints out the name, url and location of the mediaOutlet
def printMediaOutlet(self):
   print(f"Name: {self.name}, URL: {self.url}, Location: {self.location}")
