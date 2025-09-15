def make_variable(name, default=None):
    if default is None:
        return f"""$if({name})$
\\{name}{{${name}$}}
$else$
\\{name}{{}}
$endif$"""
    else:
        return f"""$if({name})$
\\{name}{{${name}$}}
$else$
\\{name}{{{str(default)}}}
$endif$"""

variables = [
    make_variable("title"),
    make_variable("shorttitle"),
    make_variable("author", "Gideon Grinberg"),
    make_variable("duedate", r"\today"),
    make_variable("professor"),
    make_variable("course"),
    make_variable("affiliation"),

    make_variable("abstract"),
    make_variable("keywords")
]

out = ""
for v in variables:
    out += v + "\n\n"

print(out)