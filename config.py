def can_build(plat):
	return plat=="android" or plat=="iphone"

def configure(env):
	if (env['platform'] == 'android'):
		env.android_add_dependency("compile 'com.google.android.gms:play-services-ads:17.1.+'")
		env.android_add_java_dir("android")
		env.android_add_to_manifest("android/AndroidManifestChunk.xml")
		env.disable_module()
	if env['platform'] == "iphone":
		env.Append(FRAMEWORKPATH=['modules/godotadmob/ios/lib'])
		env.Append(LINKFLAGS=['-ObjC', '-framework','AdSupport', '-framework','CoreTelephony', '-framework','EventKit', '-framework','EventKitUI', '-framework','MessageUI', '-framework','StoreKit', '-framework','SafariServices', '-framework','CoreBluetooth', '-framework','AssetsLibrary', '-framework','CoreData', '-framework','CoreLocation', '-framework','CoreText', '-framework','ImageIO', '-framework', 'GLKit', '-framework','CoreVideo', '-framework', 'CFNetwork', '-framework', 'MobileCoreServices', '-framework', 'GoogleMobileAds'])
