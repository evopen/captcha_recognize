# about captcha image
IMAGE_HEIGHT = 36
IMAGE_WIDTH = 120
CHAR_SETS = '123456789ABCDEFGHIJKLMNPQRSTUVWXYZ'
CLASSES_NUM = len(CHAR_SETS)
CHARS_NUM = 5
# for train
RECORD_DIR = './data'
TRAIN_FILE = 'train.tfrecords'
VALID_FILE = 'valid.tfrecords'
