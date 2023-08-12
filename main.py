from saxonche import PySaxonProcessor

xpath = '''array {
  let $dividers := //divider
  return
    for-each-pair($dividers, tail($dividers), function($d1, $d2) {
      array { root($d1)//*[. >> $d1 and . << $d2] }
    })
}'''

with PySaxonProcessor(license=False) as saxon:
    xpath_processor = saxon.new_xpath_processor()

    xpath_processor.set_context(file_name='sample1.xml')

    xdm_result = xpath_processor.evaluate(xpath)

    print(xdm_result)

import lxml.etree as ET

from elementpath import select
from elementpath.xpath3 import XPath3Parser

root = ET.parse('sample1.xml')

xpath = '''let $dividers := //divider
  return
    for-each-pair($dividers, tail($dividers), function($d1, $d2) {
      array { root($d1)//*[. >> $d1 and . << $d2] }
    })
'''
result = select(root, xpath, parser=XPath3Parser)

result_list = [array.items() for array in result]

print(result_list)

