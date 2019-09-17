from doubly_linked_list import DoublyLinkedList

class LRUCache:
  """
  Our LRUCache class keeps track of the max number of nodes it
  can hold, the current number of nodes it is holding, a doubly-
  linked list that holds the key-value entries in the correct 
  order, as well as a storage dict that provides fast access
  to every node stored in the cache.
  """
  def __init__(self, limit=10):
    self.max = limit

    self.doubleList = DoublyLinkedList()
    self.storage = {}

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the end of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):

    current = self.doubleList.head

    print(self.storage)
    
    #loop through each value in list. 
    while current:
      print(self.storage)
      #find out where that key is in DLL, delete  
      if current.value == key:

        #we insert our value to front (add to head)
        self.doubleList.move_to_front(current)

        #we get the value at key from dictionary
        #return dictionary[key]
        return self.storage[key]

      #move to next element
      current = current.next

    return None
    
  """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """
  def set(self, key, value):
    #we check if dictionary[key] exists (if so we get it)
    if key in self.storage:
      self.storage[key] = value
      self.get(key)
    #we check if length of dll is more than limit 
    elif self.doubleList.length == self.max:
      #remove value from tail
      self.storage.pop(self.doubleList.remove_from_tail())
      #add value to head
      self.doubleList.add_to_head(key)
      self.storage[key] = value

    else:
      self.doubleList.add_to_head(key)
      self.storage[key] = value



    

