formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one","two","three","four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter,formatter,formatter))
print(formatter.format(
    "Hello",
    "This is my text",
    "Only I can use it",
    "Becuase I know how to use it",
    ))

