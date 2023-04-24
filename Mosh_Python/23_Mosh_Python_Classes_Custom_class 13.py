
# common data structure types(list, set, dictionary,,etc): thiese data stucture(container types) are enough for the most situation
# but there are times we wanna use my own container types

# Here, we made this class "TagCloud", and we wanna keep track of the number of various tags in a block.(ex: how many articles do we have that are tagged with python or javascript and so on)

class TagCloud:
    def __init__(self):
        self.tags = {}      # Assign an empty dictionary to "tag" attribute

    def add(self, tag):     # "add" method with an argument name "tag"
        self.tags[tag] = self.tags.get(tag, 0) + 1   # get "tag" with default value="0"(if don't have), increament by 1

#  여기까지 듣다가 도저히 이해가 안가서 중간에 건너뜀,,, 나중에 나오면 다시 공부

# because this class represents a container, it supports various operations around the containers, 
# for example, these are the operations that are supported in this custom container type.
cloud = TagCloud()      # creat an object
len(cloud)              # we can get the numbers of the items
cloud["python"] = 10    # get an item by it's key, and set that
for item in cloud:      # we could iterate over the container
    print(item)


