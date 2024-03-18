def insertionShort(arr):
    for j in range(1,len(arr)):
        actual = arr[j]
        
        i=j-1
        while i >= 0 and arr[i]>actual:
            arr[i+1] = arr[i]
            i-=1
        arr[i+1] = actual
    print(arr)

arr=[4,2,5,35,7,4,2,1,9,5,7]
print(arr)
insertionShort(arr)

#https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbEY0RHhTRWp0bjRYZ0tMc2dvUTc2MEU3Z1ZLUXxBQ3Jtc0trNzdVN3hZQmxYQUlkMGdhYmNXci1RRjlSQ3FDWW95OUtIZFhBZm1pWHltQks5a0hIY2s1Qk5BeXQ2YkpJa0xsdC1pYm5NWE9mTjhuakdveWdKSFpJVFdPTktRZWtwdE1nWmp4NjZnaFZFT2pjc0xjWQ&q=https%3A%2F%2Fvisualgo.net%2Fes%2Fsorting&v=6GU6AGEWYJY