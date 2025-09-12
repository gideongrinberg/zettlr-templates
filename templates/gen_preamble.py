def make_variable(name, default=None):
    if default is None:
        return f"""$if({name})$
\\{name}{{$${name}$$}}
$endif$"""
    else:
        return f"""$if({name})$
\\{name}{{$${name}$$}}
$else$
\\{name}{{{str(default)}}}
$endif$"""

variables = [
    make_variable("title"),
    make_variable("author", "Gideon Grinberg"),
    make_variable("date", r"\date"),
    # make_variable("professor"),
    # make_variable("course")
]

out = ""
for v in variables:
    out += v + "\n\n"

print(out)