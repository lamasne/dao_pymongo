How to use:
- create a mongodb_settings file and a co2class dict
- call DAO(mongodb_settings, co2class) first to init, then use DAO()

Notes on design:
- main class DAO is a singleton so that the connection to MONGODB is only open once. (Is it better than making it a static class?)
- to seperate the way objects are saved by the DB from the model, 
    * methods do not recquire any info about the database (not even the collection name)
    * methods only return either a dict of id-object pairs (or a single object), or a dict of attribute-value pairs (or a single value)
