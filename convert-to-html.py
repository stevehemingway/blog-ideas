#!/usr/bin/env python3

# This script generates a Markdown file called `blog_post.md` with the text of the blog post. You can then use this file as is, or convert it to HTML using a Markdown converter.

import markdown

with open("blog_post.md", "r") as f:
    text = f.read()

html = markdown.markdown(text)

with open("blog_post.html", "w") as f:
    f.write(html)
