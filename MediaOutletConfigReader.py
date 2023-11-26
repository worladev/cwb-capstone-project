import configparser
import logging


from MediaOutlet import MediaOutlet


# MediaOutletConfigReader class has self and filename as its parameters.
# this function is to read media data using a file and display the output in a list form
# the filename is the name of the configuration file
# an empty list is created to store the media objects
class MediaOutletConfigReader:
    def __init__(self, filename):
        self.media_list = []
        self.filename = filename
        self.logger = logging.getLogger(__name__)

        # Method to read media data using parameters from a config file this function uses the get method to retrieve the
    # name,url and location of the mediaOutlet and create a media object it then appends to the media list created in
    # the MediaOutletConfigReader class it then returns the media object in a list form
    def read(self):
        config = configparser.ConfigParser()
        config.read(self.filename)
        self.logger.info("Reading media data from config file.")

        for section in config.sections():
            name = config.get(section, 'name')
            url = config.get(section, 'url')
            location = config.get(section, 'location')
            self.logger.debug(f"Read media outlet: {name}, {url}, {location}")


            media = MediaOutlet(name, url, location)
            self.media_list.append(media)
        return self.media_list
