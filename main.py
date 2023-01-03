import pyshorteners as ps

link = input("\nEnter your link: ")

shortener = ps.Shortener()
short = shortener.tinyurl.short(link)

print(f"Shorted link is: {short}")