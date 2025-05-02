nums = [1,4,5,63,27,35]

result = sorted(nums)

print(result)

users= [ #type: ignore
    {"username":"alijamil","posts":["post1","post2"],"email":"alooo@alooo.com"}
    {"username":"bogxd","posts":["post1"],"email":"alooo@abc.com"}
    {"username":"what","posts":["post1","post2"]}
]

result = sorted(users, key=len)

print(len)