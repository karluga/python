import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Janis</name>
  <phone type="intl">
    +371 1122
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
