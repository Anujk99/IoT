import RPi.GPIO as GPIO
from bottle import route, run, template
import os

# assuming LED1 is connected to 8 and LED2 to 10
def check_status():
    led1 = GPIO.input(8)
    led2 = GPIO.input(10)
    status = {}
    if led1:
        status['led1'] = "ON"
    else:
        status['led1'] = "OFF"
    if led2:
        status['led2'] = "ON"
    else:
        status['led2'] = "OFF"
    return status
        

    
index_html = '''<h4>This is the current status of LED connected to raspberrypi GPIO</h4>.
 <table style="width:15%">
  <tr>
    <th>LED</th>
    <th>STATUS</th>
  </tr>
  <tr>
    <td>LED 1:  </td>
    <td>{{ led1}}</td>
  </tr>
  <tr>
    <td>LED 2:  </td>
    <td> {{led2}}</td>
  </tr>
</table> 
'''

@route('/')
def index():
    status = check_status()
    return template(index_html, led1=status['led1'], led2=status['led2'])

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    run(host='0.0.0.0', port=port, debug=True)







