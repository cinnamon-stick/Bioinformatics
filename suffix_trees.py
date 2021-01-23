# Suffix Tree Program
# Elika J

# Given a text file following the format:
# string
# string
#
# Create a suffix tree of those strings
# %%
class Tree:
    def __init__(self, value: str, list_of_children=[]):
        self.value = value
        self.list_of_children = list_of_children

    def has_child_of_i(self, i):
        for u in self.list_of_children:
            num = u.get_value()
            if num == i:
                return u
        return False

    def get_value(self):
        return self.value

    def add_node(self, value: str):
        """
        Adds a node to a tree

        Parameters
        ----------
        value : str
            The value of the new node you are adding

        Returns
        -------
        new_tree : Tree
            Return the tree you have added

        """
        new_tree = Tree(value)
        self.list_of_children.append(new_tree)
        return new_tree

    def add_to_suffix_tree(self, string: str):
        len_str = len(string)
        temp_str = string
        next_tree = self
        while (len_str >= 1):
            next_tree = next_tree.add_node(temp_str[0])
            temp_str = temp_str[1:]
            len_str -= 1
# %%


class String_List:
    def __init__(self, name_of_txt_file: str):
        """
        Purpose
        -------
        Creates an object with a list of strings
        (contained in variable self.strings) for the suffix tree.

        Parameters
        ----------
        name_of_txt_file : str
            Name of the text file you want to read from. Must be in the format
            string+"\n"+string+"\n"+...+"\n"

        Returns
        -------
        None. Creates an object of type String_List

        """
        file_reading = open(name_of_txt_file, "r")
        lines = file_reading.readlines()
        list_of_strings = []
        for line in lines:
            list_of_strings.append(line[:-1]+"$")
        self.strings = list_of_strings

    def get_list_strings(self):
        return self.strings
# %%


root = Tree("ROOT")
sl = String_List("text.txt").get_list_strings()
for j in sl:
    prior_node = root
    counter = 0
    for i in j:
        curr_node = prior_node.has_child_of_i(i)
        if curr_node == False:
            prior_node.add_to_suffix_tree(j[counter:])
            break
        prior_node = curr_node
        counter += 1

for e in root.list_of_children:
    print(e.get_value())
