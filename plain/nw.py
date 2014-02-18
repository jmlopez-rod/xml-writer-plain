"""XML: PLAIN NodeWriter

Collection of NodeWriter objects to write an xml file as is, i.e.
there is no processing on the text nodes.

"""

from lexor.core.writer import NodeWriter
import lexor.core.elements as core


class DefaultNW(NodeWriter):
    """Default way of writing XML elements in the plain style. """

    def start(self, node):
        if isinstance(node, core.ProcessingInstruction):
            self.write('<%s' % node.name)
            if '\n' in node.data:
                self.write('\n')
            else:
                self.write(' ')
            return
        att = ' '.join(['%s="%s"' % (k, v) for k, v in node.items()])
        self.write('<%s' % node.name)
        if att != '':
            self.write(' %s' % att)
        if isinstance(node, core.RawText) or node.child:
            self.write('>')
        else:
            self.write('/>')

    def end(self, node):
        if node.child:
            self.write('</%s>' % node.name)
        elif isinstance(node, core.ProcessingInstruction):
            self.write('?>')
        elif isinstance(node, core.RawText):
            self.write('</%s>' % node.name)


class CommentNW(NodeWriter):
    """Writes `<!-- ... -->`. """

    def start(self, node):
        self.write('<!--')

    def end(self, node):
        self.write('-->')


class DoctypeNW(NodeWriter):
    """Writes `<!DOCTYPE ...>`. """

    def start(self, node):
        self.write('<!DOCTYPE ')

    def end(self, node):
        self.write('>')


class CDataNW(NodeWriter):
    """Writes `<![CDATA[ ... ]]>`. """

    def start(self, node):
        self.write('<![CDATA[')

    def end(self, node):
        self.write(']]>')

