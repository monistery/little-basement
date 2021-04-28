def input_userinfo(first, last, minzu='han', **userinfo):
	info = {}
	info['name'] = first + " " +  last
	info['minzu'] = minzu
	for key, value in userinfo.items():
		info[key] = value
	return info
