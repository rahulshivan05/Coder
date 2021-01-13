import uiautomator,os,sys,datetime,time
from uiautomator import Device

def app_install():

	list1 = ['whatsapp messenger','facebook','uber','teewe','BookMyShow','skype','flipkart','flipboard',
		'gaana','9gag','Dailyhunt','ndtv','cricbuzz','mx player','firefox','opera','subway surf','asphalt8','deer hunt','realracing3','clashofclans']

	os.system('adb shell am start -n com.android.vending/com.google.android.finsky.activities.MainActivity')
	time.sleep(5)
	if device(text="ACCEPT", resourceId="com.android.vending:id/positive_button").exists :
		device(text="ACCEPT", resourceId="com.android.vending:id/positive_button").click()
		time.sleep(3)
	if device(className="android.widget.ImageView", resourceId="com.android.vending:id/search_box_idle_text").exists :
		device(className="android.widget.ImageView", resourceId="com.android.vending:id/search_box_idle_text").click()
		time.sleep(2)
		for index in range(len(list1)):
			device(className="android.widget.EditText", resourceId="com.android.vending:id/search_box_text_input").set_text(list1[index])
			time.sleep(5)
			device(className="android.widget.RelativeLayout",index=0).click()
			print ("app opened")
			time.sleep(3)
			pass
			#while True:
			if device(className="android.widget.RelativeLayout", resourceId="com.android.vending:id/play_card",index=0).exists :
				device(className="android.widget.RelativeLayout", resourceId="com.android.vending:id/play_card",index=0).click()
			#	break
			#	pass
			time.sleep(5)
			if device(className="android.widget.Button", resourceId="com.android.vending:id/buy_button",text="INSTALL").exists:
				device(className="android.widget.Button", resourceId="com.android.vending:id/buy_button",text="INSTALL").click()
				time.sleep(2)
				if device(className="android.widget.TextView", resourceId="com.android.vending:id/account",text="needs access to").exists :
					device(className="android.widget.Button", resourceId="com.android.vending:id/continue_button",text="ACCEPT").click()
					time.sleep(40)
					device(className="android.widget.TextView",resourceId='com.android.vending:id/search_button').click()
					time.sleep(1)
					pass
			else:
				if device(className="android.widget.Button", resourceId="com.android.vending:id/update_button",text="UPDATE").exists:
					device(className="android.widget.Button", resourceId="com.android.vending:id/update_button",text="UPDATE").click()
					time.sleep(2)
					if device(className="android.widget.TextView", resourceId="com.android.vending:id/account",text="needs access to").exists :
						device(className="android.widget.Button", resourceId="com.android.vending:id/continue_button",text="ACCEPT").click()
						time.sleep(40)
						device(className="android.widget.TextView",resourceId='com.android.vending:id/search_button').click()
						time.sleep(1)
						pass
				else:
					time.sleep(3)
					device(className="android.widget.TextView",resourceId='com.android.vending:id/search_button').click()
					time.sleep(5)
					pass

		time.sleep(300)				
		os.system('adb shell pm clear com.android.vending')

if __name__=='__main__':
	print ('Getting Device Info')
	os.system('adb devices > deviceinfo')
	devinf = open('deviceinfo','rb')
	devlines = devinf.readlines()
	devinf.close()
	for i in range(len(devlines)):
		if 'device' not in devlines[i]: continue
		dev = devlines[i].split('\t')[0]
		print (dev)
	device=Device(dev)

	app_install()