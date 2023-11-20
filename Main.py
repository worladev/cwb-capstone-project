from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello CWB Members</h1>'


if __name__ == '__main__':
    app.run(debug=True)

Daakyehen
from MediaOutlet import printMediaOutlet
from MediaOutletConfigReader import MediaOutletConfigReader

# Create an instance of MediaOutletConfigReader
# Call the read method to parse the file and get a list of media objects
# Print the names, URLs, and locations of the media items
filename = 'config.ini'
reader = MediaOutletConfigReader(filename)
media_list = reader.read()
for media in media_list:
    printMediaOutlet(media)

