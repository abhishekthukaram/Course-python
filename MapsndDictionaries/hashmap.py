class LinkedlistNode:
    def __init__(self,key, value):
        self.key = key
        self.value= value
        self.next = None

class HashMap:
    def __init__(self, initial_size=10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p =31
        self.num_entries = 0

    def put(self, key, value):
        bucket_index  =self.get_bucket_index(key)
        new_node = LinkedlistNode(key, value)


        pass

    def get(self,key):
        pass

    def get_bucket_index(self,key):
        return self.get_hash_code(key)

    def get_hash_code(self,key):
        key = str(key)
        num_buckets= len(self.bucket_array)
        current = 1
        hash_code =0
        for character in key:
            hash_code+=ord(character)*current
            hash_code = hash_code%num_buckets
            current*=self.p
            current=current%num_buckets
        return hash_code % num_buckets

    def size(self):
        return self.num_entries

hash_ouput = HashMap()
out = hash_ouput.get_bucket_index("abcd")
print out
