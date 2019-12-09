from jinja2 import Environment, FileSystemLoader
import yaml

config = yaml.load(open('./config2.yaml'))

ip_lan = raw_input ("vvedi lan ip:")
ip_wlan = raw_input ("vvedi wlna ip:")
#config["interfaces"]["interface_30"]["ip"] = str(ip_lan)

env = Environment(loader=FileSystemLoader('.'))

template = env.get_template('config2.j2')

print(template.render(config))
