import tkinter as tk
class search:
    def __init__(self):
        self.root = tk.Tk
        self.root.geometry("500x500")
        self.word = tk.StringVar
        self.entry = tk.Entry(self.root, textvariable=self.word)

        self.button = tk.Button(text="search", command=self.binarysearch([], search.word, 0, len([])))
        self.root.mainloop()


    def binarysearch(self, lis, target, start, end):
        if start <= end:
            mid = (start + end)//2
            if lis[mid] == target:
                return mid
            elif lis[mid] < target:
                return search.binarysearch(self, lis, target, mid+1, end)
            else:
                return search.binarysearch(self, lis, target, start, mid-1)
        return -1
#search.binarysearch([], search.word, 0, len([]))