#!/usr/bin/python

from src import generic , custom_logger
import time 
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('logs/generic.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def main():
	logger.info('Starting Main Process at {}'.format(time.time()))
	gen_obj = generic.GenericParser('/home/ransom/9a66eef3511daf5cc2954d7ae0fc93e6920f4d0ce565b6df7438899598711e99')
	gen_obj.check_mime()

if __name__ == '__main__':
	main()
