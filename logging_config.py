import logging
import sys
#def configure_logging():
 # Configure logging to display messages on the console
  # logging.basicConfig(filename='web_scraper.log',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
   #console = logging.StreamHandler()
   #console.setLevel(logging.INFO)
   #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
   #console.setFormatter(formatter)
   #logging.getLogger('').addHandler(console)

# Class to log all activities and happenings when running the program
# It uses the Python logging with logging level of INFO to log messages
# It uses StreamHandler to display logs on the standard output streams , this can be the console or terminal
class LoggingConfig:
   def __init__(self):
     logging.basicConfig(
       level=logging.INFO,
       format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
       handlers=[logging.FileHandler('web_scrapers.log'), logging.StreamHandler(sys.stdout)]
     )



