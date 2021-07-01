# import notify2
# notify2.init('News Notify')
# n = notify2.Notification('hi','hello')
# n.show()
# n.set_timeout(14000)
import os

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

notify("Title", "Heres an alert")