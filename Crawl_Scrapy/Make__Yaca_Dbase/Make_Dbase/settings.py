# Scrapy settings for Make_Dbase project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'Make_Dbase'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['Make_Dbase.spiders']
NEWSPIDER_MODULE = 'Make_Dbase.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

CONCURRENT_REQUESTS = 1
DOWNLOAD_DELAY = 0.4

ITEM_PIPELINES = ['Make_Dbasel.pipelines.MakeDbasePipeline']

