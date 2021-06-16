import json

def get_config(config_path = "./config.jSON"):
	c = open(config_path,"r")
	return json.load(c)

d1={'anme':'foot',"cpu_num": -1}
json.dump(d1,open(r'./config.jSON','w'))

c=get_config()
c