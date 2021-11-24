import sys
import json
import base64
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Authentication:
    def __init__(self, BASE_URL=""):
        self.HEADER = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.BASE_URL = BASE_URL

    def generateTokenHeader(self, username="", password=""):
        try:
            print("\n[Request] Generate an Authentication Token Header")
            url = self.BASE_URL + '/api/v1/login'
            print("URL  : " + url)

            body = json.dumps({
                "id": str(username),
                "password": str(password),
                "remember": False
            }).encode("utf-8")

            r = requests.post(url, data=body, headers=self.HEADER)
            if r.status_code == 200:
                r = r.json()
                if r["token"] and r["user"]:
                    print("\n[Successful] Generate Token for " + r["user"]["name"])
                    return {
                        'Authorization': "Bearer " + r["token"],
                        'Accept': 'application/json'
                    }
                else:
                    print("[Error] Can't Generate an Authentication Token")
                    sys.exit()
            else:
                print("[Error] " + str(r.status_code))
                print("        " + str(r.text))
                sys.exit()
        except:
            print("\n[Error] Function generateTokenHeader")
            sys.exit()

    def generateCredentialHeader(self, username="", password=""):
        try:
            print("\n[Request] Generate an Authentication Credential Header")

            TOKEN_AUTH = base64.b64encode((str(username) + ":" + str(password)).encode("ascii")).decode("utf-8")

            print("\n[Successful] Generate Authentication Credential for " + username)
            return {
                'Authorization': "Basic " + TOKEN_AUTH,
                'Accept': 'application/json'
            }
        except:
            print("\n[Error] Function generateCredentialHeader")
            sys.exit()
