class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__ (self):
        return '{} -> {}'.format(self.val, self.next)