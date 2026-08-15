def describe(name,**t):
    print("pet Name:",name)
    for k,v in t.items():
        print(f"{k} : {v}")

describe(
    "rato",
    species="dog",
    age=3,
    color="black"
)