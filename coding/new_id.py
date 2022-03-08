import re

# my code
# def solution(new_id):
#     new_id = re.sub("[^a-z0-9-_.]", "", new_id.lower())
#     new_id = re.sub("(([.])\\2{1,})", ".", new_id)
#     if len(new_id) >= 1:
#         if new_id[0] == ".":
#             new_id = new_id[1:]
#         elif new_id[-1] == ".":
#             new_id = new_id[:-1]
#     if new_id == "" or new_id is None:
#         new_id = "a"
#     if len(new_id) >= 16:
#         new_id = new_id[:15]
#     if new_id[-1] == ".":
#         new_id = new_id[:-1]
#     if len(new_id) <= 2:
#         for i in range(3):
#             new_id += new_id[-1]
#             if len(new_id) == 3:
#                 break
#     return new_id

# best code
def solution(new_id):
    st = re.sub('[^a-z0-9\-_.]', '', new_id.lower())
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st



if __name__ == "__main__":
    solution("...!@BaT#*..y.abcdefghijklm")
    #solution(".1.")
