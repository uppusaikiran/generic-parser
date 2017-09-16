#!/usr/bin/python

from src import generic , custom_logger
import time 
import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('logs/generic.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def main():
	logger.info('Starting Main Process at {}'.format(time.time()))
	gen_obj = generic.GenericParser(sys.argv[1])
	gen_obj.check_mime()

if __name__ == '__main__':
	main()
