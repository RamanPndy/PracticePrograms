package main

import (
	"fmt"

	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

var DB *gorm.DB

// User represents the user model
type User struct {
	ID      uint   `gorm:"primaryKey"`
	Name    string `gorm:"size:100"`
	Email   string `gorm:"uniqueIndex;size:100"`
	Age     int
	Profile Profile `gorm:"foreignKey:UserID"`
	Orders  []Order `gorm:"foreignKey:UserID"`
}

// Profile represents the profile model
type Profile struct {
	ID     uint   `gorm:"primaryKey"`
	UserID uint   `gorm:"uniqueIndex"`
	Bio    string `gorm:"size:255"`
}

type Order struct {
	ID          uint   `gorm:"primaryKey"`
	OrderNumber string `gorm:"size:100"`
	Amount      float64
	UserID      uint
}

func initDB() {
	dsn := "host=localhost user=your_user password=your_password dbname=your_db port=5432 sslmode=disable"
	var err error
	DB, err = gorm.Open(postgres.Open(dsn), &gorm.Config{})
	if err != nil {
		panic("failed to connect database")
	}
	fmt.Println("Database connection established")
}

// GORM can automatically create or update the database schema based on your models:
func migrate() {
	DB.AutoMigrate(&User{})
}

func createUser(name, email string, age int) {
	user := User{Name: name, Email: email, Age: age}
	result := DB.Create(&user)
	if result.Error != nil {
		fmt.Println("Error creating user:", result.Error)
		return
	}
	fmt.Println("User created successfully:", user)
}

func createUserWithProfile(name, email string, age int, bio string) {
	user := User{
		Name:  name,
		Email: email,
		Age:   age,
		Profile: Profile{
			Bio: bio,
		},
	}
	result := DB.Create(&user)
	if result.Error != nil {
		fmt.Println("Error creating user with profile:", result.Error)
	} else {
		fmt.Println("User with profile created successfully")
	}
}

func createSampleData() {
	user1 := User{Name: "John Doe", Email: "john@example.com", Age: 30}
	user2 := User{Name: "Jane Smith", Email: "jane@example.com", Age: 25}

	DB.Create(&user1)
	DB.Create(&user2)

	order1 := Order{OrderNumber: "A001", Amount: 100.50, UserID: user1.ID}
	order2 := Order{OrderNumber: "A002", Amount: 200.75, UserID: user1.ID}
	order3 := Order{OrderNumber: "B001", Amount: 300.00, UserID: user2.ID}

	DB.Create(&order1)
	DB.Create(&order2)
	DB.Create(&order3)
}

func getUserByID(id uint) {
	var user User
	result := DB.First(&user, id)
	if result.Error != nil {
		fmt.Println("Error fetching user:", result.Error)
		return
	}
	fmt.Println("User fetched successfully:", user)
}

func getAllUsers() {
	var users []User
	result := DB.Find(&users)
	if result.Error != nil {
		fmt.Println("Error fetching users:", result.Error)
		return
	}
	fmt.Println("Users fetched successfully:", users)
}

func updateUserEmail(id uint, newEmail string) {
	var user User
	result := DB.First(&user, id)
	if result.Error != nil {
		fmt.Println("Error fetching user:", result.Error)
		return
	}
	user.Email = newEmail
	DB.Save(&user)
	fmt.Println("User email updated successfully:", user)
}

func deleteUser(id uint) {
	var user User
	result := DB.Delete(&user, id)
	if result.Error != nil {
		fmt.Println("Error deleting user:", result.Error)
		return
	}
	fmt.Println("User deleted successfully")
}

func joinExample() {
	var users []User
	result := DB.Preload("Orders").Find(&users)
	if result.Error != nil {
		fmt.Println("Error fetching users with orders:", result.Error)
		return
	}

	for _, user := range users {
		fmt.Printf("User: %s, Email: %s, Age: %d\n", user.Name, user.Email, user.Age)
		for _, order := range user.Orders {
			fmt.Printf("\tOrder Number: %s, Amount: %.2f\n", order.OrderNumber, order.Amount)
		}
	}
}

func lazyFetchExample() {
	var user User
	result := DB.First(&user, 1) // Fetch the user with ID 1
	if result.Error != nil {
		fmt.Println("Error fetching user:", result.Error)
		return
	}

	fmt.Printf("User: %s, Email: %s, Age: %d\n", user.Name, user.Email, user.Age)

	// Lazy load orders for the user
	var orders []Order
	DB.Model(&user).Association("Orders").Find(&orders)
	for _, order := range orders {
		fmt.Printf("Order Number: %s, Amount: %.2f\n", order.OrderNumber, order.Amount)
	}
}

func main() {
	initDB()
	migrate()
	// Other operations

	// Create users
	createUser("John Doe", "john@example.com", 30)
	createUser("Jane Smith", "jane@example.com", 25)

	createUserWithProfile("John Doe", "john@example.com", 30, "A bio for John")

	// Insert sample data
	createSampleData()

	// Join example
	joinExample()

	// Lazy fetch example
	lazyFetchExample()

	// Read users
	getUserByID(1)
	getAllUsers()

	// Update user
	updateUserEmail(1, "john.doe@example.com")

	// Delete user
	deleteUser(2)
}
