# Scrapy settings for Lower_branches project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'Lower_branches'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['Lower_branches.spiders']
NEWSPIDER_MODULE = 'Lower_branches.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

CONCURRENT_REQUESTS = 1
DOWNLOAD_DELAY = 0.4

ITEM_PIPELINES = ['Lower_branches.pipelines.LowerBranchesPipeline']
