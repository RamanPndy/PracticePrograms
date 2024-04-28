overview and features of the GORM are:
1. Developer Friendly
2. Every feature comes with a tests
3. Hooks / Callbacks (Before/After Create/Save/Update/Delete/Find)
4. Eager loading with Preload, Joins
5. Context, Prepared Statement Mode, DryRun Mode
6. SQL Builder, Upsert, Locking, Optimizer/Index/Comment Hints, Named Argument, SubQuery
7. Transactions, Nested Transactions, Save Point, Rollback To to Saved Point
8. Associations (Has One, Has Many, Belongs To, Many To Many, Polymorphism)
9. SQL Builder
10. Logger

GORM runs transactions by default whenSave/Delete operations are performed , so changes made in that transaction are not visible 
until it is committed, if you return any error in your hooks, the change will be rollbacked

by default, GORM uses ID as the primary key.

GORM allows you to Define the models before creating tables and the table will be created based on the model, 
it pluralize the struct name to snake_cases as table name, snake_case as column name, and uses CreatedAt, UpdatedAt to track creating/updating time.

AutoMigrate will create tables, missing foreign keys, constraints, columns, and indexes. 
It will change the existing column’s type size, and precision. It WON’T delete unused columns to protect your data.

db.AutoMigrate(&User{})
db.AutoMigrate(&User{}, &Product{}, &Order{})
// You can add table suffix when creating tables
db.Set("gorm:table_options", "ENGINE=InnoDB").AutoMigrate(&User{})

GORM provides a migrator interface, which contains unified API interfaces for each database that could be used to build your 
database-independent migrations,

create ( Create record/records )
user := User{Name: "Jinzhu", Age: 18, Birthday: time.Now()}
result := db.Create(&user)

//GORM supports create from map:
db.Model(&User{}).Create(map[string]interface{}{
  "Name": "jinzhu", "Age": 18,
})

//Create With Associations
type CreditCard struct {
  gorm.Model
  Number   string
  UserID   uint
}

type User struct {
  gorm.Model
  Name       string
  CreditCard CreditCard
}

db.Create(&User{
  Name: "jinzhu",
  CreditCard: CreditCard{Number: "411111111111"}
})

To efficiently insert a large number of records, pass a slice to the Create method. 
GORM will generate a single SQL statement to insert all the data and backfill primary key values, hook methods will be invoked too.
var users = []User{{Name: "jinzhu1"}, {Name: "jinzhu2"}, {Name: "jinzhu3"}}
db.Create(&users)

//You can set batch size when creating with CreateInBatches, e.g:
var users = []User{{Name: "jinzhu_1"}, ...., {Name: "jinzhu_10000"}}

// batch size 100
db.CreateInBatches(users, 100)

When creating from a map, hooks won’t be invoked, associations won’t be saved and primary key values won’t be backfilled.
//GORM supports batch create from map:
// batch insert from `[]map[string]interface{}{}`
db.Model(&User{}).Create([]map[string]interface{}{
  {"Name": "jinzhu_1", "Age": 18},
  {"Name": "jinzhu_2", "Age": 20},
})

querying ( Get record/records)
GORM provides First, Take, Last methods to retrieve a single object from the database, 
it adds LIMIT 1 condition when querying the database, and it will return the error ErrRecordNotFound if no record is found.
db.First(&user) // SELECT * FROM users ORDER BY id LIMIT 1;

db.Take(&user) // SELECT * FROM users LIMIT 1;

db.Last(&user) // SELECT * FROM users ORDER BY id DESC LIMIT 1;

Objects can be retrieved using the primary key by using Inline Conditions if the primary key is a number. 
When working with strings, extra care needs to be taken to avoid SQL Injection

db.First(&user, 10) // SELECT * FROM users WHERE id = 10;

db.Find(&users, []int{1,2,3}) // SELECT * FROM users WHERE id IN (1,2,3);

db.First(&user, "id = ?", "1b74413f-f3b8-409f-ac47-e8c062e3472a") // If the primary key is a string

result := db.Find(&users) // SELECT * FROM users;

db.Where(&User{Name: "jinzhu", Age: 20}).First(&user) // SELECT * FROM users WHERE name = "jinzhu" AND age = 20 ORDER BY id LIMIT 1;

db.Where(map[string]interface{}{"name": "jinzhu", "age": 20}).Find(&users) // SELECT * FROM users WHERE name = "jinzhu" AND age = 20;

updating ( update record/records )
db.First(&user)

user.Name = "jinzhu 2"
user.Age = 100
db.Save(&user)
When updating a single column with Update, it needs to have any conditions or it will raise an error ErrMissingWhereClause, 
checkout Block Global Updates for details When using the Model method and its value have a primary value, 
the primary key will be used to build the condition, for example:

Updates supports update with struct or map[string]interface{}, when updating with struct it will only update non-zero fields by default

db.Model(&User{}).Where("active = ?", true).Update("name", "hello") // UPDATE users SET name='hello', updated_at='2013-11-17 21:34:10' WHERE active=true;

// User's ID is `111`:
db.Model(&user).Update("name", "hello") //UPDATE users SET name='hello', updated_at='2013-11-17 21:34:10' WHERE id=111;

db.Model(&user).Where("active = ?", true).Update("name", "hello") // UPDATE users SET name='hello', updated_at='2013-11-17 21:34:10' WHERE id=111 AND active=true;

If you want to update selected fields or ignore some fields when updating, you can use Select, Omit
db.Model(&user).Select("name").Updates(map[string]interface{}{"name": "hello", "age": 18, "active": false}) // UPDATE users SET name='hello' WHERE id=111;

db.Model(&user).Omit("name").Updates(map[string]interface{}{"name": "hello", "age": 18, "active": false}) // UPDATE users SET age=18, active=false, updated_at='2013-11-17 21:34:10' WHERE id=111;

// Select with Struct (select zero value fields)
db.Model(&user).Select("Name", "Age").Updates(User{Name: "new_name", Age: 0}) // UPDATE users SET name='new_name', age=0 WHERE id=111;

// Select all fields (select all fields include zero value fields)
db.Model(&user).Select("*").Update(User{Name: "jinzhu", Role: "admin", Age: 0})

// Select all fields but omit Role (select all fields include zero value fields)
db.Model(&user).Select("*").Omit("Role").Update(User{Name: "jinzhu", Role: "admin", Age: 0})

Delete ( Deletion of record/records )
When deleting a record, the deleted value needs to have a primary key or it will trigger a Batch Delete, for example:
// Email's ID is `10`
db.Delete(&email) // DELETE from emails where id = 10;

db.Where("name = ?", "jinzhu").Delete(&email) //DELETE from emails where id = 10 AND name = "jinzhu"

GORM allows to delete objects using the primary key(s) with the inline conditions, it works with numbers, check out Query Inline Conditions for details
db.Delete(&User{}, 10) // DELETE FROM users WHERE id = 10;
db.Delete(&users, []int{1,2,3}) //DELETE FROM users WHERE id IN (1,2,3);





