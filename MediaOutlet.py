import configparser


# This Class defines a Media source with the following attributes:
# name : the name of the media
# url : the website of the media outlet
# location : the location of the media outlet

class MediaOutlet:
    def __init__(self, name, url, location):
        self.name = name
        self.url = url
        self.location = location


# This creates a method to print media outlet.
# This function prints out the name, url and location of the mediaOutlet
    def printMediaOutlet(self):
        print(f"Name: {self.name}, URL: {self.url}, Location: {self.location}")
