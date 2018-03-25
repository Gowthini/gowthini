def rev(text):
    for line in text.split('\n'):
        return(' '.join(line.split()[::-1]))
print(rev("what you think you can do it...that one you really love it."))
print(rev("Python Exercises."))
