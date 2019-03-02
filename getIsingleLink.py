page = '''<div id="top_bin"> <div id="top_content" class="width960">
   <div class="udacity float-left"> <a href="/">'''
# just an example to understand how the parse the list of html tags and get the link values .
startHref = page.find("<a href=")
endHref = page.find(">", startHref)
pullingLinks = page[startHref: endHref]
linkValue = pullingLinks[pullingLinks.find('"'):]

print(linkValue[1: -1])
