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

def ListWifiDepuisApple(wifi_list):
	apdict = {}
	#kml = simplekml.Kml()
	for wifi in wifi_list.wifi:
		#print "Wifi BSSID : ", wifi.bssid 
		if wifi.HasField('location'):
			lat=wifi.location.latitude*pow(10,-8)
			lon=wifi.location.longitude*pow(10,-8)
			#kml.newpoint(name=wifi.bssid, coords=[(lon,lat)])
			mac=padBSSID(wifi.bssid)
			apdict[mac] = (lat,lon)
		if wifi_list.HasField('valeur_inconnue1'):
			print('Inconnu1 : ', '%X' % wifi_list.valeur_inconnue1)
		if wifi_list.HasField('valeur_inconnue2'):
			print('Inconnu2 : ', '%X' % wifi_list.valeur_inconnue1)
		if wifi_list.HasField('APIName'):
			print('APIName : ', wifi_list.APIName)
	#kml.save("test.kml")
	return apdict

def ProcessMobileResponse(cell_list):
	operators = {1:'Telstra',2:'Optus',3:'Vodafone',6:'Three'}
	celldict = {}
	celldesc = {}
	#kml = simplekml.Kml()
	for cell in cell_list.cell:
		if cell.HasField('location') and cell.CID != -1: # exclude "LAC" type results (usually 20 in each response)
			lat=cell.location.latitude*pow(10,-8)
			lon=cell.location.longitude*pow(10,-8)
			cellid = '%s:%s:%s:%s' % (cell.MCC,cell.MNC,cell.LAC,cell.CID)
			#kml.newpoint(name=cellid, coords=[(lon,lat)])
			try:
#				cellname = '%s LAC:%s CID:%s [%s %s %s] [%s %s]' % (operators[cell.MNC],cell.LAC,cell.CID,\
#					cell.location.data3,cell.location.data4,cell.location.data12,\
#					cell.data6,cell.data7)
				cellname = '%s LAC:%s CID:%s' % (operators[cell.MNC],cell.LAC,cell.CID)
			except:
				cellname = 'MNC:%s LAC:%s CID:%s' % (cell.MNC,cell.LAC,cell.CID)
			try:
				if cell.HasField('channel'):
					cellname += ' Channel:%s' % cell.channel
			except ValueError:
				pass
			celldict[cellid] = (lat,lon)
			celldesc[cellid] = cellname
		else:
			pass
			#print 'Weird cell: %s' % cell
	#kml.save("test.kml")
	#f=file('result.txt','w')
	#for (cid,desc) in celldesc.items():
		#print cid, desc
		#f.write('%s %s\n'%(cid,desc))
	#f.close()
	#print 'Wrote result.txt'
	return (celldict,celldesc)

def QueryBSSID(query, more_results=True):
	liste_wifi = BSSIDApple_pb2.BlockBSSIDApple()
	if type(query) == str:
		bssid_list = [query]
	elif type(query) == list:
		bssid_list = query
	else:
		raise TypeError('Provide 1 BSSID as string or multiple BSSIDs as list of strings')
	for bssid in bssid_list:
		wifi = liste_wifi.wifi.add()
		wifi.bssid = bssid
	liste_wifi.valeur_inconnue1 = 0
	if more_results:
		liste_wifi.valeur_inconnue2 = 0 # last byte in request == 0 means return ~400 results, 1 means only return results for BSSIDs queried
	else:
		liste_wifi.valeur_inconnue2 = 1
	chaine_liste_wifi = liste_wifi.SerializeToString()
	longueur_chaine_liste_wifi = len(chaine_liste_wifi)
	headers = {'Content-Type':'application/x-www-form-urlencoded', 'Accept':'*/*', "Accept-Charset": "utf-8","Accept-Encoding": "gzip, deflate",\
			"Accept-Language":"en-us", 'User-Agent':'locationd/1753.17 CFNetwork/711.1.12 Darwin/14.0.0'}
	data = "\x00\x01\x00\x05"+"en_US"+"\x00\x13"+"com.apple.locationd"+"\x00\x0a"+"8.1.12B411"+"\x00\x00\x00\x01\x00\x00\x00" + chr(longueur_chaine_liste_wifi) + chaine_liste_wifi.decode();
	r = requests.post('https://gs-loc.apple.com/clls/wloc',headers=headers,data=data,verify=False) # CN of cert on this hostname is sometimes *.ls.apple.com / ls.apple.com, so have to disable SSL verify
	liste_wifi = BSSIDApple_pb2.BlockBSSIDApple() 
	liste_wifi.ParseFromString(r.content[10:])
	return ListWifiDepuisApple(liste_wifi)
