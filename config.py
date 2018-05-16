# about captcha image
IMAGE_HEIGHT = 36
IMAGE_WIDTH = 120
CHAR_SETS = 'ABCDEFHKUPSLN3MWYZ2468RG597TV'
CLASSES_NUM = len(CHAR_SETS)
CHARS_NUM = 5
# for train
RECORD_DIR = './data'
TRAIN_FILE = 'train.tfrecords'
VALID_FILE = 'valid.tfrecords'
