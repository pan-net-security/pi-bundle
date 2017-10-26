import requests
import os

CA_BUNDLE_FILE="/etc/ssl/certs/ca-certificates.crt"

try:
    ca_file = os.stat(CA_BUNDLE_FILE)
    if ca_file:
        ca_bundle_path = CA_BUNDLE_FILE
    else:
        ca_bundle_path = False
except os.error:
    ca_bundle_path = False

def header_add_token(token,headers={}):
    HEADERS = {'Accept': 'application/json',
               'Connection': 'keep-alive',
               'Accept-Language': 'en-us',
               'Accept-Encoding': 'gzip, deflate',
               }

    if token:
        HEADERS['PI-Authorization']=token

    return headers.update(HEADERS)

def api_get(url, token=None, headers={}, params={}):
    r = requests.get(url, headers=header_add_token(token,headers), params=params, verify=ca_bundle_path)
    r.raise_for_status()
    return r

def api_post(url, token=None, headers={}, body=""):
    return requests.post(url, headers=header_add_token(token,headers), data=body, verify=ca_bundle_path)

def api_delete(url, token=None, headers={}, body=""):
    return requests.delete(url, headers=header_add_token(token,headers), data=body, verify=ca_bundle_path)
