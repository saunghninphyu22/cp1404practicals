"""
Estimate: 15 minutes
Actual: 20 minutes
"""

from programming_langugage import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(python)

languages = [python, ruby, visual_basic]

dynamic_languages = [language.name for language in languages if language.is_dynamic()]

print("The dynamically typed languages are:")
for language in dynamic_languages:
    print(language)
