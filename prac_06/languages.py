"""
CP1404 Practical - ProgrammingLanguage client code

"""

from programming_language import ProgrammingLanguage

# Create some ProgrammingLanguage objects
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

# Print one to test __str__
print(python)

# Make a list of languages
languages = [python, ruby, visual_basic]

# Print only the dynamically typed languages
print("\nThe dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)
