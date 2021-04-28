def bd_profile(first, last, **user_info):
	profile = {}
	profile['name'] = first.title() + last
	for key, value in user_info.items():
		profile[key] = value
	return profile
	
user_profile = bd_profile('bai', 'jicheng', 
						   location='jiangsu',
						   field='jisuanji')
print(user_profile)
	
