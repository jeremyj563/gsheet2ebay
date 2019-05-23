#By Jeremy Johnson

from __future__ import print_function
import httplib2
import os
import sys
import datetime

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from optparse import OptionParser

sys.path.insert(0, '%s/../' % os.path.dirname(__file__))

from common import dump

import ebaysdk
from ebaysdk.utils import getNodeText
from ebaysdk.exception import ConnectionError
from ebaysdk.trading import Connection as Trading

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'

def get_user_input():
	os.system('clear')
	print ("""
						GSheet2eBay""")
	ans=True
	while ans:
		print ("""
		1.  Game Guides			16. Wii				31. Xbox One
		2.  Game Manuals		17. Wii U			32. Misc Electronics
		3.  Accessories			18. Game Boy			33. Computer Video Games
		4.  TurboGrafx-16		19. Game Boy Color		34. Computer Software
		5.  3DO				20. Game Boy Advance		35. DVDs & Movies
		6.  Sega CD			21. Nintendo DS			36. Consoles
		7.  Sega 32X			22. Nintendo 3DS		37. Soundtracks
		8.  Sega Genesis		23. PlayStation			38. Other
		9.  Sega Saturn			24. PlayStation 2		0.  Quit
		10. Dreamcast			25. PlayStation 3
		11. Game Gear			26. PlayStation 4
		12. Nintendo			27. PlayStation Portable
		13. Super Nintendo		28. PlayStation Vita
		14. Nintendo 64			29. Xbox
		15. GameCube			30. Xbox 360
		""")
		ans=raw_input("Please make worksheet selection: ")
		if ans=="1":
			strWorkSheet = "Game Guides"
			break
		elif ans=="2":
			strWorkSheet = "Game Manuals"
			break
		elif ans=="3":
			strWorkSheet = "Accessories"
			break
		elif ans=="4":
			strWorkSheet = "TurboGrafx-16"
			break
		elif ans=="5":
			strWorkSheet = "3DO"
			break
		elif ans=="6":
			strWorkSheet = "Sega CD"
			break
		elif ans=="7":
			strWorkSheet = "Sega 32X"
			break
		elif ans=="8":
			strWorkSheet = "Sega Genesis"
			break
		elif ans=="9":
			strWorkSheet = "Sega Saturn"
			break
		elif ans=="10":
			strWorkSheet = "Dreamcast"
			break
		elif ans=="11":
			strWorkSheet = "Game Gear"
			break
		elif ans=="12":
			strWorkSheet = "Nintendo"
			break
		elif ans=="13":
			strWorkSheet = "Super Nintendo"
			break
		elif ans=="14":
			strWorkSheet = "Nintendo 64"
			break
		elif ans=="15":
			strWorkSheet = "GameCube"
			break
		elif ans=="16":
			strWorkSheet = "Wii"
			break
		elif ans=="17":
			strWorkSheet = "Wii U"
			break
		elif ans=="18":
			strWorkSheet = "Game Boy"
			break
		elif ans=="19":
			strWorkSheet = "Game Boy Color"
			break
		elif ans=="20":
			strWorkSheet = "Game Boy Advance"
			break
		elif ans=="21":
			strWorkSheet = "Nintendo DS"
			break
		elif ans=="22":
			strWorkSheet = "Nintendo 3DS"
			break
		elif ans=="23":
			strWorkSheet = "PlayStation"
			break
		elif ans=="24":
			strWorkSheet = "PlayStation 2"
			break
		elif ans=="25":
			strWorkSheet = "PlayStation 3"
			break
		elif ans=="26":
			strWorkSheet = "PlayStation 4"
			break
		elif ans=="27":
			strWorkSheet = "PlayStation Portable"
			break
		elif ans=="28":
			strWorkSheet = "PlayStation Vita"
			break
		elif ans=="29":
			strWorkSheet = "Xbox"
			break
		elif ans=="30":
			strWorkSheet = "Xbox 360"
			break
		elif ans=="31":
			strWorkSheet = "Xbox One"
			break
		elif ans=="32":
			strWorkSheet = "Misc Electronics"
			break
		elif ans=="33":
			strWorkSheet = "Computer Video Games"
			break
		elif ans=="34":
			strWorkSheet = "Computer Software"
			break
		elif ans=="35":
			strWorkSheet = "DVDs & Movies"
			break
		elif ans=="36":
			strWorkSheet = "Consoles"
			break
		elif ans=="37":
			strWorkSheet = "Soundtracks"
			break
		elif ans=="38":
			strWorkSheet = "Other"
			break
		elif ans=="0":
			print("\n")
			quit()
		else:
			os.system('clear')
			print("\nInvalid entry\n")
			raw_input("Press Enter to continue...")
			get_user_input()

	intRangeStart = input("Range Start: ")
	intRangeEnd = input("Range End: ")
	strRange = (str(intRangeStart) + ":" + str(intRangeEnd))
	return ans

def gsheet_get_cred():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def gsheet_select():
	credentials = gsheet_get_cred()
	http = credentials.authorize(httplib2.Http())
	discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
		'version=v4')
	service = discovery.build('sheets', 'v4', http=http,
		discoveryServiceUrl=discoveryUrl)

	spreadsheetId = '1f_kwLOso1zv490coHRyX_TtwgzwHJDWWpbVFfjF3YaE'
	rangeName = 'Game Guides!313:313'
	result = service.spreadsheets().values().get(
		spreadsheetId=spreadsheetId, range=rangeName).execute()
	values = result.get('values', [])

	if not values:
		print('No data found.')
	else:
		global myitem
		for row in values:
		        myitem = {
				"Item": {
					"Title": row[0],
					"Description": "<![CDATA[<table cellspacing=\"28\" cellpadding=\"0\" width=\"100%%\"><tbody><tr><td valign=\"top\"><hr size=\"6\"><br><div align=\"left\"><font size=\"4\"><b>I T E M&nbsp;&nbsp;&nbsp; D E S C R I P T I O N:</b></font><br></div><font size=\"3\"><br>%s<br><br><b>All of my items are stored in a clean and smoke free home.</b><br><br><br><hr><br><br><i><b>NOW OFFERING COMBINED SHIPPING!</b></i><br><br><i>Add items to your cart to see the HUGE savings! Shipping charges will be calculated automatically based on weight.</i><br><br><br><hr size=\"6\"></font></td></tr></tbody></table>]]>" % (row[5]),
					"PrimaryCategory": {"CategoryID": "156595"},
					"StartPrice": row[2],
					"CategoryMappingAllowed": "true",
					"Country": "US",
					"ConditionID": "3000",
					"Currency": "USD",
					"DispatchTimeMax": "3",
					"ListingDuration": "Days_30",
					"ListingType": "FixedPriceItem",
					"PaymentMethods": "PayPal",
					"PayPalEmailAddress": "dummy.bin@hotmail.com",
					"PictureDetails": {"PictureURL": "https://raw.githubusercontent.com/jeremyj563/ebay-images/master/%s" % (row[1])},
					"PostalCode": "52806",
					"Quantity": "1",
					"ReturnPolicy": {
						"ReturnsAcceptedOption": "ReturnsAccepted",
						"RefundOption": "MoneyBack",
						"ReturnsWithinOption": "Days_30",
						"Description": "If you are not satisfied, return the book for refund.",
						"ShippingCostPaidByOption": "Buyer"
					},
					"SellerProfiles": {
						"SellerPaymentProfile": {
							"PaymentProfileName": "PayPal:Immediate pay",
						},
						"SellerReturnProfile": {
							"ReturnProfileName": "30 Day Return Policy",
						},
						"SellerShippingProfile": {
							"ShippingProfileName": "USPS First Class, Priority, Priority Express Flat Rate Envelope",
						}
					},
					"ShippingDetails": {
						"ShippingType": "Calculated",
						"ShippingServiceOptions": {
							"ShippingServicePriority": "1",
							"ShippingService": "USPSMedia"
						},
						"CalculatedShippingRate": {
							"OriginatingPostalCode": "52806",
							"PackagingHandlingCosts": "0.0",
							"ShippingPackage": "PackageThickEnvelope",
							"WeightMajor": "1",
							"WeightMinor": "0"
						}
					},
					"Site": "US"
				}
			}


def ebay_init_options():
    usage = "usage: %prog [options]"
    parser = OptionParser(usage=usage)

    parser.add_option("-d", "--debug",
                      action="store_true", dest="debug", default=False,
                      help="Enabled debugging [default: %default]")
    parser.add_option("-y", "--yaml",
                      dest="yaml", default='ebay.yaml',
                      help="Specifies the name of the YAML defaults file. [default: %default]")
    parser.add_option("-a", "--appid",
                      dest="appid", default=None,
                      help="Specifies the eBay application id to use.")
    parser.add_option("-p", "--devid",
                      dest="devid", default=None,
                      help="Specifies the eBay developer id to use.")
    parser.add_option("-c", "--certid",
                      dest="certid", default=None,
                      help="Specifies the eBay cert id to use.")

    (opts, args) = parser.parse_args()
    return opts, args


def ebay_add_item(opts):
    """http://www.utilities-online.info/xmltojson/#.UXli2it4avc
    """

    try:
        api = Trading(debug=opts.debug, config_file=opts.yaml, appid=opts.appid,
                      certid=opts.certid, devid=opts.devid, warnings=False)
        
        api.execute('AddFixedPriceItem', myitem)
        dump(api)

    except ConnectionError as e:
        print(e)
        print(e.response.dict())
        
if __name__ == '__main__':
	get_user_input()
	#gsheet_select()
	#(opts, args) = ebay_init_options()
	#ebay_add_item(opts)
