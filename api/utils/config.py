import configparser

config = configparser.RawConfigParser()
config.read('/Users/mertakcay/Cryptocurrency/api/config.ini')
details_dict = dict(config.items('DEV'))
print(details_dict)
