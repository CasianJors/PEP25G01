"""
zoo_feeding_exam.py

A zoo wants an iterable object to keep track of animals fed by each zookeeper each day.
Each zookeeper is identified by name (string), each animal by name (string).
Iterating the object yields the names of all animals fed that day.

1) Definition (40p)
   a) Class constructor takes a date string in YYYY-MM-DD format. (5p)
   b) Method add_feed: (25p)
      - Signature: keeper name (string), animals fed (list of strings). (5p)
      - Adds each animal to the keeper's record; ignore duplicates. (10p)
      - If an animal is already recorded for another keeper, raise ValueError("Animal already fed by another keeper: <animal>"). (10p)
   c) Iteration returns all animals fed that day across all keepers. (10p)

2) Execution (40p)
   a) Create an instance of the class for a specific date. (10p)
   b) Add feeding data and handle errors: (10p)
      - Alice: "Lion", "Tiger", "Bear"
      - Bob:   "Tiger", "Giraffe", "Zebra"  (should raise on "Tiger")
      - Charlie: "Elephant", "Zebra", "Monkey"  (should raise on "Zebra")
   c) Catch and print errors when they occur. (10p)
   d) Iterate the object and save each animal on a new line in a file named "feed_log.txt". (10p)

3) Documentation (20p)
   a) Add module, class, and method docstrings. (10p)
   b) Add basic type hints for method signatures. (10p)
"""