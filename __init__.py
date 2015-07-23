#!/usr/bin/python
import bleach
import urllib2
import html5check

sampleXHTML1 = 'http://www.w3.org/2000/07/8378/schemas/xhtml1-sample.xml'
result = urllib2.urlopen(sampleXHTML1)
html = result.read()

attrs = {
  '*'     : ['class'],
  'a'     : ['rel', 'href'],
  'base'  : ['href', 'target'],
  'col'   : ['span'],
  'img'   : ['src', 'alt', 'title'],
  'meta'  : ['charset', 'content', 'http-equiv', 'itemprop', 'name', 'property'],
  'link'  : ['rel', 'href', 'itemprop', 'property'],
  'bdo'   : ['dir'],
  'param' : ['value', 'name'],
  'map'   : ['name'],
  'optgroup' : ['label'],
  'object'   : ['data', 'type'],
  'td'       : ['colspan', 'rowspan'],
  'th'       : ['colspan']
}

tags = ['!DOCTYPE', 'a', 'abbr', 'acronym', 'address', 'applet', 'area', 'article', 'aside', 'audio', 'b', 'base', 'basefont', 'bdi', 'bdo', 'big', 'blockquote', 'body', 'br', 'button', 'canvas', 'caption', 'center', 'cite', 'code', 'col', 'colgroup', 'command', 'datalist', 'dd', 'del', 'details', 'dfn', 'dir', 'div', 'dl', 'dt', 'em', 'embed', 'fieldset', 'figcaption', 'figure', 'font', 'footer', 'form', 'frame', 'frameset', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'head', 'header', 'hgroup', 'hr', 'html', 'i', 'iframe', 'img', 'input', 'ins', 'kbd', 'keygen', 'label', 'legend', 'li', 'link', 'map', 'mark', 'menu', 'meta', 'meter', 'nav', 'noframes', 'noscript', 'object', 'ol', 'optgroup', 'option', 'output', 'p', 'param', 'pre', 'progress', 'q', 'rp', 'rt', 'ruby', 's', 'samp', 'script', 'section', 'select', 'small', 'source', 'span', 'strike', 'strong', 'style', 'sub', 'summary', 'sup', 'table', 'tbody', 'td', 'textarea', 'tfoot', 'th', 'thead', 'time', 'title', 'tr', 'track', 'tt', 'u', 'ul', 'var', 'video', 'wbr']
depreciated_tags  = ['acronym', 'big', 'tt']

for tag in depreciated_tags:
  tags.remove(tag)

sane = bleach.clean(html, tags, attrs, strip=True)

html5check.check(sane)
