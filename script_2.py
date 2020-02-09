from jinja2 import Environment, FileSystemLoader
import yaml

config = yaml.load(open('./vlan.yaml'))

env = Environment(loader=FileSystemLoader('.'))

template = env.get_template('vlan.j2')

print(template.render(config))
