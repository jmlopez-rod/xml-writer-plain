"""XML: PLAIN writer NW test

Testing suite to write XML in the PLAIN style.

"""

import lexor
from lexor.command.test import compare_with

DOCUMENT = """<!DOCTYPE xml>
<?python print 'Hello xml!'
?><parent 
att="val">
<child1>child 1 
content</child1>     <child2> child 2 
content with entity &amp; </child2>
<child3>
    &lt;  
&amp; <!-- Multiline comment goes
here and there... 
done... --></child3>
 <child4>
  child
 4 &lt; 
  content
<apples>    <bananas>  </bananas>
</apples><![CDATA[a < b]]> </child4>
&lt;
text
&amp;
<a> <b/> </a>
</parent>
"""

EXPECTED = """<!DOCTYPE xml>
<?python
print 'Hello xml!'
?><parent att="val">
<child1>child 1 
content</child1>     <child2> child 2 
content with entity &amp; </child2>
<child3>
    &lt;  
&amp; <!-- Multiline comment goes
here and there... 
done... --></child3>
 <child4>
  child
 4 &lt; 
  content
<apples>    <bananas>  </bananas>
</apples><![CDATA[a < b]]> </child4>
&lt;
text
&amp;
<a> <b/> </a>
</parent>
"""


def test_plain():
    """xml.writer.plain.nw """
    doc, _ = lexor.parse(DOCUMENT, 'xml')
    doc.style = 'plain'
    compare_with(str(doc), EXPECTED)
