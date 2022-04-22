# main_app/views.py

from django import http
from django.shortcuts import render
from django.http import HttpResponse


class Book:
    def __init__(self, title, author, publication, description, isbn, genre, olid):
        self.title = title
        self.author = author
        self.publication = publication
        self.description = description
        self.isbn = isbn
        self.genre = genre
        self.olid = olid

books = [
    Book("The Shining", "Stephen King", "1977", "Jack Torrance's new job at the Overlook Hotel is the perfect chance for a fresh start. As the off-season caretaker at the atmospheric old hotel, he'll have plenty of time to spend reconnecting with his family and working on his writing. But as the harsh winter weather sets in, the idyllic location feels ever more remote...and more sinister. And the only one to notice the strange and terrible forces gathering around the Overlook is Danny Torrance, a uniquely gifted five-year-old.", "0451150325", "horror", "OL24219563M"),
    Book("A Wizard of EarthSea", "Ursula LeGuin", "1992", "Ged was the greatest sorcerer in Earthsea, but in his youth he was the reckless Sparrowhawk. In his hunger for power and knowledge, he tampered with long-held secrets and loosed a terrible shadow upon the world. This is the tumultuous tale of his testing, how he mastered the mighty words of power, tamed an ancient dragon, and crossed death's threshold to restore the balance.", "1680652109", "fantasy", "OL32560930M"),
    Book("Count of Monte Cristo", "Alexandre Duams", "1844", "Thrown in prison for a crime he has not committed, Edmond Dantes is confined to the grim fortress of If. There he learns of a great hoard of treasure hidden on the Isle of Monte Cristo and he becomes determined not only to escape, but also to unearth the treasure and use it to plot the destruction of the three men responsible for his incarceration. Dumas' epic tale of suffering and retribution, inspired by a real-life case of wrongful imprisonment, was a huge popular success when it was first serialized in the 1840s.", "9780140449266", "action/adventure", "OL24277771M"),
    Book("Atonement", "Ian McEwan", "2001", "On a hot summer day in 1935, thirteen-year-old Briony Tallis witnesses a moment's flirtation between her older sister, Cecilia, and Robbie Turner, the son of a servant and Cecilia's childhood friend. But Briony's incomplete grasp of adult motives—together with her precocious literary gifts—brings about a crime that will change all their lives.", "9780385721790", "contemporary fiction", "OL34972111M"),
    Book("The Dead Girls Club", "Damien Angelica Walters", "2019", "In 1991, Heather Cole and her friends were members of the Dead Girls Club. Obsessed with the macabre, the girls exchanged stories about serial killers and imaginary monsters, like the Red Lady, the spirit of a vengeful witch killed centuries before. Heather knew the stories were just that, until her best friend Becca began insisting the Red Lady was real—and she could prove it.\n\nThat belief got Becca killed.\n\nIt's been nearly thirty years, but Heather has never told anyone what really happened that night—that Becca was right and the Red Lady was real. She's done her best to put that fateful summer, Becca, and the Red Lady, behind her. Until a familiar necklace arrives in the mail, a necklace Heather hasn't seen since the night Becca died.\n\nThe night Heather killed her.\n\nNow, someone else knows what she did...and they're determined to make Heather pay.", "9781643851631", "thriller", "OL27857138M"),
    Book("Mexican Gothic", "Silvia Moreno-Garcia", "2020", "After receiving a frantic letter from her newly-wed cousin begging for someone to save her from a mysterious doom, Noemí Taboada heads to High Place, a distant house in the Mexican countryside. She's not sure what she will find—her cousin's husband, a handsome Englishman, is a stranger, and Noemí knows little about the region.\n\nNoemí is also an unlikely rescuer: She's a glamorous debutante, and her chic gowns and perfect red lipstick are more suited for cocktail parties than amateur sleuthing. But she's also tough and smart, with an indomitable will, and she is not afraid: Not of her cousin's new husband, who is both menacing and alluring; not of his father, the ancient patriarch who seems to be fascinated by Noemí; and not even of the house itself, which begins to invade Noemi's dreams with visions of blood and doom.\n\nHer only ally in this inhospitable abode is the family's youngest son. Shy and gentle, he seems to want to help Noemí, but might also be hiding dark knowledge of his family's past. For there are many secrets behind the walls of High Place. The family's once colossal wealth and faded mining empire kept them from prying eyes, but as Noemí digs deeper she unearths stories of violence and madness.\n\nAnd Noemí, mesmerized by the terrifying yet seductive world of High Place, may soon find it impossible to ever leave this enigmatic house behind.", "9781529402681", "gothic fiction", "OL29541750M"),
    # Book("In The Woods", "Tana French", "descr", "isbn", "genre"),
    # Book("The House Next Door", "Stephen King", "descr", "isbn", "genre"),
    # Book("The Killer Wore Leather", "Laura Antoneiu", "descr", "isbn", "genre"),
    # Book("The Likeness", "Tana French", "descr", "isbn", "genre"),
    # Book("The Secret History", "Donna Tartt", "descr", "isbn", "genre"),
    # Book("The Dwelling", "Susie Moloney", "descr", "isbn", "genre"),
    # Book("Feed", "Mira Grant", "descr", "isbn", "genre"),
    # Book("If it Bleeds", "Stephen King", "descr", "isbn", "genre"),
    # Book("A Beautiful Poison", "Lydia Kang", "descr", "isbn", "genre"),
    # Book("This House is Haunted", "John Boyne", "descr", "isbn", "genre"),
    # Book("East of Eden", "John Steinbeck", "descr", "isbn", "genre"),
    # Book("Fifteen Dogs", "Andre Alexis", "descr", "isbn", "genre"),
    # Book("It", "Stephen King", "descr", "isbn", "genre"),
    # Book("Into the Drowning Deep", "Mira Grant", "descr", "isbn", "genre"),
    # Book("Gideon the Ninth", "Tamsyn Muir", "descr", "isbn", "genre"),
    # Book("The Wild Iris", "Louise Gluck", "descr", "isbn", "genre"),
    # Book("Doctor Sleep", "Stephen King", "descr", "isbn", "genre"),
    # Book("The Shoot Horses, Don't They?", "Horace McCoy", "descr", "isbn", "genre"),
    # Book("My Cousin Rachel", "Daphne du Maurier", "descr", "isbn", "genre"),
]

# Index view
def index(request):
    return render(request, "index.html")

# Profile view
def profile(request):
    return HttpResponse("<h1>Profile page!</h1>")

# Bookshelf view
def bookshelf(request):
    return HttpResponse("<h1>Bookshelf page!</h1>")

# Book view
def books_index(request):
    return render(request, "books/index.html", { "books": books })

# Bookclub view
def bookclub(request):
    return HttpResponse("<h1>Bookclub page!</h1>")

# Search view
def search(request):
    return HttpResponse("<h1>Search page!</h1>")

# Book community view
# def book_comm(request):
#     return HttpResponse("<h1>Book community page!</h1>")
