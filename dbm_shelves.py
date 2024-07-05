import shelve
import dbm
#with shelve.open("shelv") as sh:
 #   sh['one']=1
  #  sh['two']=2
   # sh['three']=3
with dbm.open("testDb.db","n") as db:
    db['a']='97'
    db['b']='98'
