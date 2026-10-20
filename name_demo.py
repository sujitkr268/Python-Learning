"""Tiny demo to understand __name__ == '__main__'

Run me two ways:
  1. python name_demo.py      -> you are the "main" program
  2. python importer.py       -> someone ELSE imported me
"""

print("name_demo.py says: my __name__ is", repr(__name__))

if __name__ == "__main__":
    print("--> I am the main program, so THIS part runs")
else:
    print("--> I was imported, so THIS part runs instead")
