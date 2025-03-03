d = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

def mv1(d):
    return d["imdb"] > 5.5

def mv2(d):
    return [i for i in d if mv1(i)]

def mv3(d, a):
    return [i for i in d if i["category"].lower() == a.lower()]

def mv4(d):
    return sum(i["imdb"] for i in d) / len(d)

def mv5(d, a):
    d1 = mv3(d, a)
    return mv4(d1)

a = int(input())
print(mv1(d[a]))  
print(mv2(d))  
b = input()
print(mv3(d, b))  
print(mv4(d))
c = input()
print(mv5(d, c))  