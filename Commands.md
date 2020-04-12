db.users.insertOne(
    {
        "name":"George",
        "age":45,
        "email":"admin@tut.by",
        "hasCar":false, 
        "birthday": new Date('1990-11-22')
    }
)

db.users.insertMany([
    {
        "name":"Боб",
        "age":10,
        "email":"admin@tut.by",
    },
    {
        "name":"Fj",
        "age":10,
        "email":"admin@tut.by",
    },
    {
        "name":"Max",
        "age":55,
        "email":"admin@tut.by",
        "birthday": new Date('1990-11-22')
    }
])

//Show all rows
db.users.find()

//Show only 2 rows
db.users.find().limit(2)

//Show 2 rows without _id
db.users.find({}, {_id: 0}).limit(2)

//Show all rows sorted by age from low to high
db.users.find({}, {_id: 0}).sort({age: 1})

//Show all rows sorted by age from hogh to low
db.users.find({}, {_id: 0}).sort({age: -1})

//Show all rows sorted by age and then by email
db.users.find({}, {_id: 0}).sort({age: -1, email: 1})


//Show all rows where age=45 sorted by age and then by email
db.users.find({age: 45}, {_id: 0}).sort({age: -1, email: 1})

//Show all rows where age=45 and hasCar=true sorted by email
db.users.find({age: 45, hasCar: true}, {_id: 0}).sort({email: 1})

//Show all rows where age<45
db.users.find({age: {$lt: 45}}, {_id: 0})

//Show all rows where age<45 or hasCar=true
db.users.find({$or: [{age: {$lt: 45}}, {hasCar: true}]}, {_id: 0})

//Show all rows where age>45
db.users.find({age: {$gt: 45}}, {_id: 0})

//Show all rows where age>=45
db.users.find({age: {$gte: 45}}, {_id: 0})

//Show all rows where age<=45
db.users.find({age: {$lte: 45}}, {_id: 0})

//Show all rows where age=45
db.users.find({age: {$eq: 45}}, {_id: 0})

//Show all rows where age != 45
db.users.find({age: {$ne: 45}}, {_id: 0})


//Show all rows name = Mans or John
db.users.find({name: {$in: ["Mans", "John"]}}, {_id: 0})

//Show all rows name != Mans or John
db.users.find({name: {$nin: ["Mans", "John"]}}, {_id: 0})

//Show all rows which has field child
db.users.find({child: {$exists: true}}, {_id: 0})

//Show all rows which has not field child
db.users.find({child: {$exists: false}}, {_id: 0})

//Show all rows which has field favColors with length = 2
db.users.find({favColors: {$size: 2}}, {_id: 0})

//Show all rows where 1 element of array favColors = red
db.users.find({"favColors.1": "red"}, {_id: 0})

//Show all rows where favColors has elements which >= r
db.users.find({favColors: {$elemMatch: {$lte: "r"}}}, {_id: 0})




