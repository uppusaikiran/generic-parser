__author__     = 'Saikiran Uppu'
__copyright__  = 'Copyright ,2017'
__licence__    = ''
__version__    = '1.0.0'
__maintainer__ = 'Saikiran Uppu'
__email__      = 'iamsaikiran.official@gmail.com'
__status__     = 'Development'

import sys
import logging
import time
import json
import os
import magic

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('logs/generic.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

class GenericParser:

        def __init__(self, file_path):
                self.file_path = file_path
                self.mime_with_macro_office = {".doc": "application/msword",
                        ".dot": "application/msword",
                        ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                        ".dotx": "application/vnd.openxmlformats-officedocument.wordprocessingml.template",
                        ".docm": "application/vnd.ms-word.document.macroEnabled.12",
                        ".dotm": "application/vnd.ms-word.template.macroEnabled.12",
                        ".xls": "application/vnd.ms-excel",
                        ".xlt": "application/vnd.ms-excel",
                        ".xla": "application/vnd.ms-excel",
                        ".xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        ".xltx": "application/vnd.openxmlformats-officedocument.spreadsheetml.template",
                        ".xlsm": "application/vnd.ms-excel.sheet.macroEnabled.12",
                        ".xltm": "application/vnd.ms-excel.template.macroEnabled.12",
                        ".xlam": "application/vnd.ms-excel.addin.macroEnabled.12",
                        ".xlsb": "application/vnd.ms-excel.sheet.binary.macroEnabled.12",
                        ".ppt": "application/vnd.ms-powerpoint",
                        ".pot": "application/vnd.ms-powerpoint",
                        ".pps": "application/vnd.ms-powerpoint",
                        ".ppa": "application/vnd.ms-powerpoint",
                        ".pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
                        ".potx": "application/vnd.openxmlformats-officedocument.presentationml.template",
                        ".ppsx": "application/vnd.openxmlformats-officedocument.presentationml.slideshow",
                        ".ppam": "application/vnd.ms-powerpoint.addin.macroEnabled.12",
                        ".pptm": "application/vnd.ms-powerpoint.presentation.macroEnabled.12",
                        ".potm": "application/vnd.ms-powerpoint.template.macroEnabled.12",
                        ".ppsm": "application / vnd.ms - powerpoint.slideshow.macroEnabled.12"
                                                                           }
                self.mime_with_macro_pdf = {
                        ".pdf": ["application/pdf", "application/x-pdf", "application/acrobat", "application/vnd.pdf", "text/pdf", "text/x-pdf"]
                }
		self.mime_executable = {
			".exe" : ["application/octet-stream", "application/x-msdownload", "application/exe", "application/x-exe", "application/dos-exe", "vms/exe", "application/x-winexe", "application/msdos-windows", "application/x-msdos-program"]
		}
                self.mime_compressed = {}
                self.mime_packed = {}
                self.mime_no_macro = {}

        def check_mime(self):
                logger.info('GenericParser on file {} starts at {}'.format(self.file_path, time.time()))
                #magic_info = magic.from_file(file_path)
                #magic_buffer = magic.from_buffer(open(file_path).read(1024))
                magic_mime = magic.from_file(self.file_path, mime=True)
                print magic_mime
                if magic_mime in self.mime_with_macro_office.values():
                        logger.info('Office File {} mime {}'.format(self.file_path, magic_mime))
                        logger.info('Sending File to office_extractor')
                elif magic_mime in self.mime_with_macro_pdf.values()[0]:
                        logger.info('Pdf File {} mime {}'.format(self.file_path, magic_mime))
                elif magic_mime in self.mime_compressed:
                        logger.info('Compressed File {} mime {}'.format(self.file_path, magic_mime))
                elif magic_mime in self.mime_packed:
                        logger.info('Packed File {} mime {}'.format(self.file_path, magic_mime))
		elif magic_mime in self.mime_executable['.exe'][0]:
                        logger.info('Executable File {} mime {}'.format(self.file_path, magic_mime))
			logger.info('Sending File {} to Exe Extractor'.format(self.file_path))
                elif magic_mime in self.mime_no_macro:
                        logger.info('NonMacro File {} mime {}'.format(self.file_path, magic_mime))
                else:
                        print 'No macro'




def parser():
        parser = GenericParser(file_path)
        parser.check_mime()


def main():
        print 'This is intended for module purpose only'
        logger.info('Checking logs working')
        parser()


if __name__ == '__main__':
        main()

