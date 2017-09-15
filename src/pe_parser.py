#!/usr/bin/python
import pefile
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('logs/generic.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class PEFeatureExtractor():
	def __init__(self , filepath):
		self.filepath = filepath
	
	def extractor(self):
		logger.info('Features for PE file {} being extracted'.format(self.filepath))
		with open(self.filepath , 'rb') as f:
			data = f.read()
			self.pe_success , self.pe_error = self.try_with_pe_open(data)
			
	def try_with_pe_open(self,file_data ):
		logger.info('Trying to see if PE is able to open {}'.format(self.filepath))
		try:
			pe = pefile.PE(data=self.file_data, fast_load=False)
			if (pe.PE_TYPE is None or pe.OPTIONAL_HEADER is None or len(pe.OPTIONAL_HEADER.DATA_DIRECTORY) < 7):
				logger.error('Error: on file: %s' % self.filepath)
                       	 	error_str =  '(Exception):, %s' % (str(e))
                        	return None, error_str
        		return pe, None
		except Exception as e:
			logger.error('Eroor: on file: %s' % self.filepath)
			error_str =  '(Exception):, %s' % (str(e))
            		return None, error_str
	def check_for_pe_success(self):
		if self.pe_success:
			logger.info('PE Feature extraction success on file {}'.format(self.filepath))
			return 1
		else:
			logger.info('PE Feature extraction failed on file {}'.format(self.filepath))
			return 0
	def extract_features(self):
		pass
def main():
	peExtractor = PEFeatureExtractor('/home/ransom/exe_example')
	peExtractor.extractor()
	peStatus = peExtractor.check_for_pe_success()
	if peStatus:
		peExtractor.extract_features()

if __name__ == '__main__':
	main()
