from SingletonPattern.singleton.start import Database

d1 = Database("localhost",
              3306,
              "root",
              "password")

d2 = Database("localhost",
              3306,
              "root",
              "password")
print(d1 is d2)

