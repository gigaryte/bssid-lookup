# -*- coding: utf-8 -*-
#!/usr/bin/python3

# Mostly taken from paper by François-Xavier Aguessy and Côme Demoustier
# http://fxaguessy.fr/rapport-pfe-interception-ssl-analyse-donnees-localisation-smartphones/

import sys
import code
import requests
import BSSIDApple_pb2
import struct
#import simplekml

def padBSSID(bssid):
    result = ''
    for e in bssid.split(':'):
        if len(e) == 1:
            e='0%s'%e
        result += e+':'
    return result.strip(':')

def decodeWifiList(wifi_list):
    apdict = {}
    for wifi in wifi_list.wifi:
        if wifi.HasField('location'):
            lat = wifi.location.lat*pow(10,-8)
            lon = wifi.location.lon*pow(10,-8)
            unk1 = wifi.location.unk1
            unk2 = wifi.location.unk2
            unk3 = wifi.location.unk3
            unk4 = wifi.location.unk4
            unk5 = wifi.location.unk5
            unk6 = wifi.location.unk6
            unk7 = wifi.location.unk7
            unk8 = wifi.location.unk8
            unk9 = wifi.location.unk9
            unk10 = wifi.location.unk10
            unk11 = wifi.location.unk11
            mac=padBSSID(wifi.bssid)
            apdict[mac] = (lat,lon, unk1, unk2, unk3, unk4, unk5, unk6, unk7,
                           unk8, unk9, unk10, unk11)
    return apdict

def QueryBSSIDs(query, more_results=True):

    location_message = BSSIDApple_pb2.WiFiLocation()
    
    if type(query) == str:
        bssid_list = [query]
    elif type(query) == list:
        bssid_list = query
    else:
        raise TypeError('Provide 1 BSSID as string or multiple BSSIDs as list of strings')
    for bssid in bssid_list:
        wifi_msg = location_message.wifi.add()
        wifi_msg.bssid = bssid
    location_message.unk1 = 0
    if more_results:
        location_message.single = 0 # last byte in request == 0 means return ~400 results, 1 means only return results for BSSIDs queried
    else:
        location_message.single = 1
    str_message = location_message.SerializeToString()
    str_message_len = len(str_message)
    headers = {'Content-Type':'application/x-www-form-urlencoded', 'Accept':'*/*', "Accept-Charset": "utf-8","Accept-Encoding": "gzip, deflate",\
            "Accept-Language":"en-us", 'User-Agent':'locationd/1753.17 CFNetwork/711.1.12 Darwin/14.0.0'}
    data = "\x00\x01\x00\x05"+"en_US"+"\x00\x13"+"com.apple.locationd"+"\x00\x0a"+"8.1.12B411"+"\x00\x00\x00\x01\x00\x00\x00" + chr(str_message_len) + str_message.decode();
    r = requests.post('https://gs-loc.apple.com/clls/wloc',headers=headers,data=data,verify=False) # CN of cert on this hostname is sometimes *.ls.apple.com / ls.apple.com, so have to disable SSL verify
    print(r.content[0:10])
    response_message = BSSIDApple_pb2.WiFiLocation()
    response_message.ParseFromString(r.content[10:])
    return decodeWifiList(response_message)
