#!/usr/bin/env python3
"""VerboseList: a list that prints notifications on modifications"""


class VerboseList(list):
    """List subclass that prints messages when modified"""

    def append(self, item):
        """Add an item and print a notification"""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list and print a notification"""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Remove an item and print a notification"""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item and print a notification"""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
