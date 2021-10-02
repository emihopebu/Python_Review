#containers into containers

locations=[]
la=(34.0522,188.2437)
chicago=(41.8781,87.6298)
locations.append(la)
locations.append(chicago)

print(locations)

eights=["Edgar Allan Poe","Charles Dickens"]
nines=["Hemingway","Fitzgerald","Orwell","Sinclair"]

authors=(eights, nines)
#get a fourth item in the second list
print(authors[1][3])

ny={"location":(40.7128,74.0059),"celebs":["W.Allen","Jay Z","K. Bacon"],
    "facts":{"state":"NY","country":"America"}}
print(ny["location"], ny["facts"])
