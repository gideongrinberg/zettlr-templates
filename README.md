# Zettlr Templates

This repo contains templates for writing academic essays in Markdown using Zettlr and Pandoc. Currently, it has templates for:

- MLA 8th Edition
- Chicago-Turbain 18th Edition (Note & Bibliography)
- Chicago-Turbain 18th Edition (Author-Date)
- APA 7th Edition

## Installation

To install these templates and set them up, first download the repository. Move the `templates/` folder wherever you want. Then, open each yaml file in the `yaml/` folder and replace the string `{{PATH-TO-TEMPLATES}}` with wherever you put the templates.  You can automate this with bash:

```bash
find . -type f -exec sed -i 's|{{PATH-TO-TEMPLATES}}|/Users/gideongrinberg/Documents/templates|g' {} +
```

Note the lack of a trailing `/` after the word "templates."

After that, move all of the yaml files into your Zettlr defaults folder. You can find the folder by going into Zettlr, opening the Asset Manager, and clicking "open defaults folder." 

## Usage

By default, the first top-level heading (`# This Is A Heading`) in your Markdown file will be used as the document’s title. You can override this in the frontmatter (yaml code at the top of your document):

```markdown
--- 
title: This Is The Real Title
---
```

### Template-Specific Documentation

<details>
<summary>Chicago Templates</summary>

These templates offer the following variables:

- `title` (you can also set this by making a top-level heading)
- `author` (*default*: my name, but you can change this in the template)
- `date` (*default*: today's date)
</details>

<details>
<summary>MLA8 Template</summary>

This template offers the following variables:

- `title` (you can also set this by making a top-level heading)
- `author` (*default*: my name, but you can change this in the template)
- `date` (*default*: today's date)
- `professor`
- `course`
</details>

<details>
<summary>APA7 Template</summary>

This template offers the following variables:

- `title` (you can also set this by making a top-level heading)
- `author` (*default*: my name, but you can change this in the template)
- `duedate` (*default*: today's date)
- `professor`
- `course`
- `affiliation`

You can also add an abstract or list of keywords using the `abstract` and `keywords` variables.
</details>

The templates all use citeproc/CSL for citations. [See the Zettlr docs](https://docs.zettlr.com/en/reference/settings/#citations) for more information. Essentially, you just need to point Zettlr to your CSL citation database and then use the syntax explained in the docs. Each template includes the relevant CSL styles, so you do not need to configure that.