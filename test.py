import base64
import hashlib
import urllib.parse
import zlib
import itertools
import random
import string


def randstr(n=4, fixed=True, charset=None):
    if not n:
        return b''

    if not fixed:
        n = random.randint(1, n)

    if not charset:
        charset = string.ascii_letters + string.digits

    return ''.join(random.choice(charset) for x in range(n)).encode('utf-8')

PREPEND = randstr(16, charset=string.printable)
print("PREPEND : " + str(PREPEND))

APPEND = randstr(16, charset=string.printable)
print("APPEND: " + str(APPEND))

class Raise:


    def cp(self, url, password):
        password = password.encode('utf-8')
        passwordhash = hashlib.md5(password).hexdigest().lower()
        print("password hash: " + passwordhash+ '\n')

        self.shared_key = passwordhash[:8].encode('utf-8')
        print("shared key: " + str(self.shared_key)+ '\n')

        self.header = passwordhash[8:20].encode('utf-8')
        print("header: " + str(self.header)+ '\n')

        self.trailer = passwordhash[20:32].encode('utf-8')
        print("trailer: " + str(self.trailer)+ '\n')

        url_parse = urllib.parse.urlparse(url)
        print("url parse: " + str(url_parse)+ '\n')





    def senf(self, original_payload):
        if isinstance(original_payload, str):
            original_payload = original_payload.encode('utf-8')
            print("original_payload: " + str(original_payload) + '\n')

        def sxor(s1, s2):
            return bytearray(
                a ^ b
                for a, b in zip(s1, itertools.cycle(s2))
            )

        xorred_payload = sxor(
            zlib.compress(original_payload),
            self.shared_key
        )
        print("xor payload: " + str(xorred_payload) + '\n')

        obfuscated_payload = base64.b64encode(xorred_payload).rstrip(b'=')
        print("obfuscated payload: " + str(obfuscated_payload)+ '\n')

        wrapped_payload = PREPEND + self.header + obfuscated_payload + self.trailer + APPEND
        print("wrapped payload: " + str(wrapped_payload)+ '\n')


    def night(self, response):

        def sxor(s1, s2):
            return bytearray(
                a ^ b
                for a, b in zip(s1, itertools.cycle(s2))
            )

        result = zlib.decompress(
            sxor(
                base64.b64decode(response),
                self.shared_key
            )
        )
        print("result: " + result)
