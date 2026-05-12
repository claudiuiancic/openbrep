---
id: wiki.generated.gdl
type: wiki
category: other
commands: ["GDL"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

#### GDL XML EXTENSION

This extension allows reading, writing and editing XML files. It implements a subset of the Document Object Model (DOM) interface. XML is a text file that uses tags to structure data into a hierarchical system, similar to HTML. An XML document can be modeled by a hierarchical tree structure whose nodes contain the data of the document. The following node types are known by the extension:

- • Element: what is between a start-tag and an end-tag in the document, or for an empty-element it can be an empty-element tag. Elements have a name, may have attributes, and usually but not necessarily have content. It means that element type nodes can have child nodes. Attributes are held in an attribute list where each attribute has a different name and a text value.
- • Text: a character sequence. It cannot have child nodes.
- • Comment: text between the comment delimiters: <!-- the comment itself --> . In the text of the comment each '-' character must be followed by a character different from '-'. It also means that the following is illegal: <!-- comment ---> . Comment type nodes cannot have child nodes.
- • CDATASection: text between the CDATA section delimiters: <![CDATA[ the text itself ]]> . In a CDATA section characters that have special meaning in an XML document need not (and must not) be escaped. The only markup recognized is the closing "]]>". CData section nodes cannot have child nodes.
- • Entity-reference: reference to a predefined entity. Such a node can have a read-only subtree and this subtree gives the value of the referenced entity. During the parsing of the document it can be chosen that entity references are translated into text nodes.


On the top level it is obligatory to have exactly one element type node (the root), and there can be several comment type nodes, as well. The document type node of the DOM interface is not available through the extension’s interface.

name value Element name of the tag "" (empty string) Text "#text" the text content of the node Comment "#comment" the text content of the node CDATASection "#cdata-section" the text content of the node Entity-reference name of the referenced entity "" (empty string) For each node in the tree there is a name and a value string associated whose meanings depend on the type of the node: Element: ELEM Text: TXT Comment: CMT CDATA section: CDATA Entity reference: EREF The success or error code of an OPEN, INPUT or OUTPUT command can be retrieved by the GetLastError instruction of the INPUT command.