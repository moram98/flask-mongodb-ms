class DevConfig():
    DEBUG = True

config = {
    'development': DevConfig,
    'MONGO_URI': 'url-from-mongo-atlas'
}