from bs4 import BeautifulSoup
# from bs4.builder import builder_registry
# builder_registry.lookup('html').DEFAULT_CDATA_LIST_ATTRIBUTES

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>


<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.title.text)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.p['class'])

print(soup.a)
print(soup.find_all('a'))

print(soup.find(id ="link3"))
print()
for link in soup.find_all("a"):
    print(link.get('href'))


soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b
print()
print(tag)

print(tag.name)
tag.name = "blockquote"
print(tag)


tag = BeautifulSoup('<b id="boldest">bold</b>', 'html.parser').b
print(tag['id'])

print(tag.attrs)

tag['id'] = "verybold"
tag['another-attribute'] = 1
print(tag)

del tag['id']
del tag['another-attribute']
print(tag)


css_soup = BeautifulSoup('<p class="body"></p>', 'html.parser')
print(css_soup.find('p')['class'])

css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser')
print(css_soup.p['class'])

id_soup = BeautifulSoup('<p id="my id"></p>', 'html.parser')
print(id_soup.p['id'])

rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>', 'html.parser')
print(rel_soup.a['rel'])

rel_soup.a['rel'] = ['index', 'contents']
print(rel_soup.p)


no_list_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser', multi_valued_attributes=None)
print(no_list_soup.p['class'])

print(id_soup.p.get_attribute_list('id'))

xml_soup = BeautifulSoup('<p class="odogwu nwoke"></p>', 'xml')
print(xml_soup.p['class'])

class_is_multi= { '*' : 'class'}
xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml', multi_valued_attributes=class_is_multi)
print(xml_soup.p['class'])


soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b
print(tag.string)

unicode_string = str(tag.string)
print(unicode_string)
print(type(unicode_string))

print(type(tag.string))

tag.string.replace_with("No longer bold")
print(tag)
print(tag['class'])

doc = BeautifulSoup("<document><content/>INSERT FOOTER HERE</document", "xml")
footer = BeautifulSoup("<footer>Here's the footer</footer>", "xml")
doc.find(text = "INSERT FOOTER HERE").replace_with(footer)

print(doc)

markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup, "html.parser")
comment = soup.find('b').string
comment = soup.find('b').string
print(comment)





















































