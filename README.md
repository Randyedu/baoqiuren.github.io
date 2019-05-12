# -*- coding:utf-8 -*-
import sys
import os
import xmltodict


class YzfXml:
    def __init__(self, xml_file_path):
        self.xml_file_path = xml_file_path
        self.xmldoc_fd = open(xml_file_path, encoding='utf-8')
        self.xmldoc = xmltodict.parse(self.xmldoc_fd.read())

    def save(self):
        out = xmltodict.unparse(self.xmldoc, pretty=True)
        with open(self.xml_file_path, 'wb') as file:
            file.write(out.encode('utf-8'))

    def get_task_group(self, str_type, str_id):
        pass





def GetTaskGroupDict(taskgroupid):
    global doc
    global taskGroup
    with open("PutDataTask.xml", encoding='utf-8') as fd:
        doc = xmltodict.parse(fd.read())
        taskGroups = doc["ExchangeData"]["CompanyTask"]["TaskList"]["TaskGroup"]

        index = 0
        try:
            if '@id' in taskGroups.keys():
                if taskGroups['@id'] == taskgroupid:
                    taskGroup = taskGroups
        except Exception as e:
            while index < len(taskGroups):
                if taskGroups[index]['@id'] == taskgroupid:
                    taskGroup = taskGroups[index]
                break
            else:
                index = index + 1
        return taskGroup

def GetSaveXML():
    out = xmltodict.unparse(doc, pretty=True)

    with open("PutDataTask.xml", 'wb') as file:
        file.write(out.encode('utf-8'))

return




## Welcome to GitHub Pages

You can use the [editor on GitHub](https://github.com/Randyedu/randyguo.github.io/edit/master/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/Randyedu/randyguo.github.io/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
