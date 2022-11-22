from environs import Env

env = Env()
env.read_env()

class Config(object):
    MODEL_FOLDER = env.str("MODEL_FOLDER", default="app/assets/model/")
    IMAGE_FOLDER = env.str("IMAGE_FOLDER", default="app/assets/images/")
    