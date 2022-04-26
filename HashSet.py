import math
from sys import stdin
import random

def my_hash(s):
    h = 0
    for c in s:
        d = ord(c)    # 0 .. 255
        h = (1_000_003 * h + d) % (2 ** 32)
    return h

class Node:
    def __init__(self, key, val, next = None):
        self.key = key
        self.val = val
        self.next = next

class HashMap:
    def __init__(self):
        # each array element is the head of a linked list of Nodes
        self.a = [None] * 5
        self.load_factor = 0
        self.Num_Buckets = 5
        self.Num_Keys = 0
        self.un_words = 0
        self.keys=[]
        self.length_ = 5


    def get(self, key):
        i = my_hash(key) % len(self.a)
        p = self.a[i]
        while p != None:
            if p.key == key:
                return p.val
            p = p.next
        return None


    def set(self, key, value):
        if self.load_factor_check():
            self.resizing()
        if self.get(key) == None:
            i = my_hash(key) % len(self.a)
            p = self.a[i]   # prepend to hash chain
            self.a[i] = Node(key, value, self.a[i])
            self.Num_Keys += 1
            self.un_words +=1

        else:
            i = my_hash(key) % len(self.a)
            if self.a[i].key == key:
                self.a[i].val = value
            else:
                parent = None
                child = self.a[i]
                while child != None:
                    if child.key == key and parent==None:
                        self.a[i].val = value
                        self.Num_Keys += 1
                        break
                    elif child.key==key:
                        parent.next.val = value
                        self.Num_Keys += 1
                        break


                    parent = child
                    child = child.next


    def unique_words(self):
        count = 0
        for i in range(len(self.a)):
            if self.a[i] != None:
                p = self.a[i]
                while p != None:
                    count+=1
                    p = p.next
        return count

    def remove(self, key):
        if self.get(key) != None:
            i = my_hash(key) % len(self.a)
            parent = None
            child = self.a[i]

            while child:
                if child.key == key:
                    if(parent == None):
                        self.a[i] = self.a[i].next
                        break
                    else:
                        parent.next = child.next
                        break
                else:
                    parent = child
                    child = child.next


        self.Num_Keys -= 1
        self.un_words -= 1

    def load_factor_check(self):
        k = (self.un_words / self.Num_Buckets)
        if k > 4:
            return True
        return False

    def resizing(self):
        while self.load_factor_check()==True:
            self.Num_Buckets = self.Num_Buckets * 2
            print(f"resizing to {self.Num_Buckets} buckets")

        b = [None] * self.Num_Buckets

        for j in range(len(self.a)):
            p = self.a[j]
            while p != None:
                i = my_hash(p.key) % len(b)
                if b[i] == None:
                    b[i] = Node(p.key, p.val)
                else:
                    b[i] = Node(p.key, p.val, b[i])
                p = p.next
        self.a = b.copy()



def dl(s):
    st=''
    str_arr=[]
    for i in s:
        if((i>='A' and i<='Z') or (i>='a' and i<='z')):
            st+=i
        else:
            break
    st_lower=st.lower()
    return st_lower

def toWord(s):
    st = ''
    str_arr=[]
    for i in range(len(s)):
        if ((s[i] >= 'A' and s[i] <= 'Z') or (s[i] >= 'a' and s[i] <= 'z')):
            st += s[i]
        else:
            if(st!=""):
                st_lower=st.lower()
                str_arr.append(st_lower)
                st=""
                st_lower=""
    if(st!=""):
        st_lower=st.lower()
        str_arr.append(st_lower)

    return str_arr

l = []
words = []
checking = []
m = HashMap()
for line in stdin:
    if(line.strip() == "== END =="):
        break
    for i in line.split():
        if (i == ""):
            continue
        else:
            arr_string=toWord(i)
            if(len(arr_string)==0):
                continue
            else:
                for i in range(len(arr_string)):
                    words.append(arr_string[i])

for line1 in stdin:
    checking.append(line1.strip())



for i in range(len(words)):
    if m.get(words[i]) != None:
        var = m.get(words[i])
        var1 = int(var)
        var1+=1
        var_str = str(var1)
        m.set(words[i], var_str)
    else:
        m.set(words[i], "1")

print("unique words =", m.un_words)
for i in checking:
    print(i, m.get(i))
    m.remove(i)














