fruits={
    "apple":250,
    "mango":300,
    "banana":260,
    "avocado":500,
    "orange":350
}
for key,value in fruits.items():
    print(key,value)
    print("Enter the name of required items and write done if you don't want")
cp=0
while True:
    x=input("items name:")
    if x=="done":
        break
    cp+=fruits[x]
if cp>1500:
    final_cp=cp-((10/100)*cp)
    print(f"actual price:{cp}")
    print(f"total price after 10% discount:{final_cp}")
else:
    print(f"total price:{cp}")