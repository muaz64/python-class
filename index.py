# carDetails= {
#      "brand":"FOrd",
#      "model":"GMAAX",
#      "year":1999,
#      "yamaha":["v1","v2","v3","v4"]
#  }
# # carDetails=dict(brand="ford",model="GMAAX", year="1999")

# print(carDetails)
# # carDetails.pop("model")
# # carDetails.popitem()
# # del carDetails["year"]
# # carDetails.clear()

# print(carDetails)

studentInfo={
    "std01":{
         "age":22,
         "ID":101
     },
     "std02":{
         "age":22,
         "ID":102
     },
     "std03":{
        "age":22,
         "ID":103,
         "skill": ["c","c++"]
     }
}

print(studentInfo)
print(studentInfo["std01"])
print(studentInfo["std02"])
print(studentInfo["std03"] ["skill"])

x=('key1','key2','key3')
y=dict.fromkeys(x,"bd")
print(y)

















