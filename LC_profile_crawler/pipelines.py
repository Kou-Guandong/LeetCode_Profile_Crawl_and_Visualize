# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import CsvItemExporter
from datetime import date


class ProfilePipeline(object):
    def __init__(self):
        self.file = open("solved-{}.csv".format(date.today().strftime("%Y-%m-%d")), 'wb+')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()


class QuestionPipeline(object):
    def __init__(self):
        print('question pipeline')
        self.file = open("question-{}.csv".format(date.today().strftime("%Y-%m-%d")), 'wb+')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        print('process item', spider)
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()