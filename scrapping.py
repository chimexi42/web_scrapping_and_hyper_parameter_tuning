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

print(soup.b.prettify())

from bs4 import CData
cdata = CData("A CDATA block")
comment.replace_with(cdata)
print(soup.b.prettify())


soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.find('head'))

print(soup.body.b)

print(soup.find('body').find('b'))
print(soup.a)

print(soup.find_all('a'))

head_tag = soup.head
print(head_tag)

title_tag = head_tag.contents[0]
print(title_tag)

print(title_tag.contents)

print(len(soup.contents))
print(soup.contents[0].name)

text = title_tag.contents[0]
print(text)

for child in title_tag.children:
    print(child)


print(head_tag.contents[0])

print()
for child in head_tag.descendants:
    print(child)

print(len(list(soup.children)))
print(len(list(soup.descendants)))


print(title_tag.string)
print(title_tag.contents)
print(soup.html.body.a['href'])
print(soup.html.string)

for string in soup.strings:
    print(repr(string))

for string in soup.stripped_strings:
    print(repr(string))

title_tag = soup.title
print(title_tag)
print(title_tag.parent)

print(title_tag.string.parent)
html_tag = soup.html

print(type(html_tag.parent))

print(soup.parent)

link = soup.a
print(link)

for parent in link.parents:
    print(parent.name)


sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></a>", 'html.parser')
print(sibling_soup.prettify())

print(sibling_soup.b.next_sibling)

print(sibling_soup.c.previous_sibling)

print(sibling_soup.b.previous_sibling)

print(sibling_soup.c.next_sibling)

print(sibling_soup.b.string)

print(sibling_soup.b.string.next_sibling)


link = soup.a
print(link)

print(link.next_sibling)

print(link.next_sibling.next_sibling)


for sibling in soup.a.next_sibling:
    print(repr(sibling))

for sibling in soup.find(id= "link3").previous_sibling:
    print(repr(sibling))


print()
last_tag = soup.find('a', id= "link3")

print(last_tag)
print(last_tag.previous_sibling)
print(last_tag.next_sibling)
print()

print(soup)

print(last_tag.next_element)

for element in last_tag.next_elements:
    print(repr(element))

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.find_all('a'))
print(soup.find_all('ab'))
print("Using Regex")
print()


import re
for tag in soup.find_all(re.compile("^b")):
    print(tag)
    print(tag.name)



for tag in soup.find_all(re.compile("t")):
    print(tag.name)


print(soup.find_all(['a', 'b']))

for tag in soup.find_all(True):
    print(tag.text)
    print(tag.name)


def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

print(soup.find_all(has_class_but_no_id))

def not_lacie(href):
    return href and not re.compile("lacie").search(href)

soup.find_all(href = not_lacie)

print("Soup find_all")
print()
print(soup.find_all("title"))

print(soup.find_all("p",class_ ="title"))
print(soup.find_all("a"))
print()
print(soup.find_all(id="link2"))
print()

print(soup.find_all(string = re.compile("sisters")))

splitted = list(soup.find_all(string = re.compile("sisters")))
print(type(splitted))

print(soup.find_all("title"))


print(soup.find_all(id="link2"))
print(soup.find_all(href = re.compile('elsie')))

print(soup.find_all(id = True))

print(soup.find_all(class_=True))


print(soup.find_all(href = re.compile('elsie'), id = 'link1'))

data_soup = BeautifulSoup('<div data-foo="value">foo!</div>', 'html.parser')
print(data_soup.find_all(attrs={"data-foo": "value"}))

print()
print(soup.find_all(attrs={'class': 'sister'}))

name_soup = BeautifulSoup('<input name="email"/>', 'html.parser')
print(name_soup.find_all(name ='email'))
print(name_soup.find_all(attrs ={'name': 'email'}))

print(soup.find_all("a", class_ = 'sister'))

print(soup.find_all(class_ = re.compile('itl')))

def has_six_characters(css_class):
    return css_class is not None and len(css_class) ==6

print()
print(soup.find_all("a", class_ = has_six_characters))
print(soup.find_all("p", class_ = has_six_characters))
print(soup.find_all("b"))
print()

css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser')
print(css_soup.find_all("p", class_ = "body"))
print(css_soup.find_all("p", class_ = "strikeout"))
print(css_soup.find_all("p", class_ = "body strikeout"))

print()
print(css_soup.select("p.strikeout.body"))

print()
print(soup.find_all("a", attrs={'class': 'sister'}))



# selecting with srings
string1 = soup.find_all(string = "Elsie")
print(string1[0].upper())

print(soup.find_all(string = ['Tillie', 'Elsie', 'Lacie']))

print(soup.find_all(string = re.compile('Dormouse')))
print(soup.find_all(text = re.compile('Dormouse')))




# combining tags and strings

print(soup.find_all("a", string = re.compile('Elsie')))
print(soup.find_all("a", string = 'Elsie'))
print()



def is_this_the_only_string_with_a_tag(s):
    return ( s== s.parent.string)

print(soup.find_all(string = is_this_the_only_string_with_a_tag))

# limit clause

xml_soup = BeautifulSoup('<p class="odogwu nwoke"></p>', 'xml')
print(xml_soup.p['class'])
print(xml_soup.p['class'])


print(soup.find_all("a", limit=2))

print(soup.find_all('title'))
print(soup.find_all('title')[0].text)
print()
print(soup.html.title)
print(soup.html.title.text)

print()
print(soup.html.find_all("title", recursive=False))

print(soup.find_all('a'))
print(soup('a'))

print()
print(soup.find_all('title', limit=1))
print(type(soup.find_all('title', limit=1)))
print(soup.find('title'))
print(type(soup.find('title')))

print()

print(soup.find_all('title', limit=1))
print(soup.find('title'))
print(soup.find("nons"))

print()

print(soup.head.title)
print(soup.find('head').find('title'))
print(soup.find('head').find_all('title'))


# find parent and find parents

a_string = soup.find(string = 'Lacie')
print(a_string)

print(a_string.findParents('a'))
print(a_string.find_parents('a'))

print()
print(a_string.find_parent('p'))
print()

print(a_string.find_parents('p', class_ = "title"))

print()
first_link = soup.a
print(first_link)

print(first_link.find_next_siblings('a'))
print()


first_story_paragraph = soup.find('p', 'story')
print(first_story_paragraph.find_next_sibling('p')['class'])
print(first_story_paragraph.find_next_sibling('p'))

print()

last_link = soup.find('a', id ='link3')
print(last_link)
print(last_link.find_previous_siblings('a'))
print()

first_story_paragraph = soup.find('p', 'story')
print(first_story_paragraph)
print(first_story_paragraph.find_previous_sibling('p'))

print()

first_link = soup.a
print(first_link)

print(first_link.find_all_previous('p'))
print(first_link.find_all_previous('title'))

# CSS SELECTORS
print(soup.select('title'))

print(soup.select("p:nth-of-type(2)"))

# print(soup.find_all("p"))

print()
print(soup.select("body a"))

print()
print(soup.select("head title"))
print(soup.select("head > title"))
print(soup.select("body > p > b"))

print(soup.select('p > a'))

print(soup.select('p > a:nth-of-type(2)'))
print(soup.select('p > a:nth-of-type(2)')[0].text)

print()
print(soup.select('p > #link1'))
print(soup.select('p > .sister')[0:2])


print(soup.select("#link1 ~ .sister"))


print()
print(soup.select("[class~=sister]"))
print()

print(soup.select("#link1"))
print(soup.select("a#link1"))
print(soup.select("#link1, #link2"))

print()
print(soup.select("a[href]"))

print()
print(soup.select('a[href="http://example.com/elsie"]'))

print(soup.select('a[href$="tillie"]'))
print(soup.select('a[href*=".com/el"]'))

xml = """<tag xmlns:ns1="http://namespace1/" xmlns:ns2="http://namespace2/">
 <ns1:child>I'm in namespace 1</ns1:child>
 <ns2:child>I'm in namespace 2</ns2:child>
</tag> """

soup = BeautifulSoup(xml, 'xml')
print(soup.select('child'))
print(soup.select('ns1|child'))

print()

# Changing tag names and attributes
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b
tag.name = "blockquote"
tag['class'] = 'verybold'
tag['id'] = 1

del tag['class']
del tag['id']
print(tag)


markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup, 'html.parser')

tag = soup.a
tag.string = "New Link text"
tag['href'] = "http://chimexi.com"
print(tag)

soup = BeautifulSoup("<a>Foo</a>", 'html.parser')
soup.a.append("Bar")
print(soup)
print(soup.a.contents)

soup = BeautifulSoup("<a>Soup</a>", 'html.parser')
soup.a.extend(["'s", " ", "on"])
print(soup)
print(soup.a.contents)

soup = BeautifulSoup("<b></b>", 'html.parser')
tag = soup.b
tag.append("Hello world")
new_string = " there"
tag.append(new_string)
print(tag)
print(tag.contents)

from bs4 import Comment
new_comment = Comment("Nice to see you")
tag.append(new_comment)
print(tag)
print(tag.contents)

print()
soup = BeautifulSoup("<b></b>", 'html.parser')
original_tag = soup.b

new_tag = soup.new_tag("a", href = "http://www.chimexi.com")
original_tag.append(new_tag)
new_tag.string = "Link text"

print(original_tag)
print(original_tag.a['href'])

print()
# INSERT

markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup, 'html.parser')
tag = soup.a
tag.insert(1, "but did not endorse")
print(tag)
print(tag.contents)

soup = BeautifulSoup("<b>leave</b>", 'html.parser')
tag = soup.new_tag('i')
tag.string = "Don't"
soup.b.string.insert_before(tag)
print(soup.b)