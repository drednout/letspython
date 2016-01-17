from model.player import Player

p = Player(name='Vasya', email='vasya@tut.by')
print(p)

p2 = Player()
p2.load_from_db("vasya@tut.by")
print(p2)

p3 = Player(name="Lesha", email="lesha@tut.by", password="123")
p3.save_to_db()
print("Player {} was inserted to db".format(p3))

p4 = Player()
p4.load_from_db("lesha@tut.by")
p4.name = "Lesha2"
p4.save_to_db()
print("Player's {} name was updated in db".format(p4))

# Please uncomment me, if you want to test delete ability
#p4.delete_from_db()
#print("Player's {} was deleted from db".format(p4))