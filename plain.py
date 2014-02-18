"""XML: PLAIN Writer Style

The plain style writes the document as is. That is, the data in the
text node is printed without any processing. This style will not
rewrite an xml document in the exact same way it was parsed.

It should be noted that a processing instruction gets written as:

    <?target*

where `*` is a whitespace if the content has no newline. Otherwise
`*` is the newline character. Also, since the attributes do not
collect any of the spaces or newline characters, the plain style
cannot rewrite a file in the same way it was parsed. That is, if the
file was parsed from

    <parent att1="val1"
            att2="val2">
        <child/>
    </parent>

then this style will print

    <parent att1="val1" att2="val2">
        <child/>
    </parent>

"""

from lexor import init, load_aux

INFO = init(
    version=(0, 0, 1, 'final', 0),
    lang='xml',
    type='writer',
    description='Writes XML files with no text node processing.',
    url='http://jmlopez-rod.github.io/lexor-lang/xml-writer-plain',
    author='Manuel Lopez',
    author_email='jmlopez.rod@gmail.com',
    license='BSD License',
    path=__file__
)
MOD = load_aux(INFO)['nw']
MAPPING = {
    '#comment': MOD.CommentNW,
    '#doctype': MOD.DoctypeNW,
    '#cdata-section': MOD.CDataNW,
    '__default__': MOD.DefaultNW,
}
