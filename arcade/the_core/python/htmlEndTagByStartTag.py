from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)
        return tag

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)
        

def htmlEndTagByStartTag(startTag):
    m = MyHTMLParser()
    r = m.handle_starttag(startTag, None)
    a = r.split(' ')
    res =  a[0]
    if res[len(a[0])-1:] == '>':
        res = res[0] + '/' + res[1:]
    else:
        res = res[0] + '/' + res[1:] + '>' 
    return res
    
