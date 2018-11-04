############################################
#
#   Client rest api to write markupdate data
#
############################################
import requests, logging, json
import pandas as pd


###############################################
#   Set logging 
###############################################
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# create a file handler
handler = logging.FileHandler('mu_ra_cli.log')
handler.setLevel(logging.INFO)
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(handler)

logger.info('Logging started')

###############################################
#   Read parms: HOST:PORT 
###############################################
f=open('mu_ra_cli.json', encoding = 'UTF-8')
parms_lines =  [json.loads(line) for line in f.read().splitlines()]
for parms in parms_lines:
	Host = parms["Host"]
	XLSFile = parms["XLSFile"]
	XLSSheet = parms["XLSSheet"]

###############################################
#   Read XLSFile 
###############################################



try:
	logger.info('XLSFile data reading..')
	market_data = pd.read_excel(XLSFile, XLSSheet)
	logger.info(market_data)
except:
	logger.error('An error occurred')
	raise


