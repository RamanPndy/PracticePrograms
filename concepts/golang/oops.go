package golang

import "fmt"

// Polymorphism
type Instrument interface {
	Play()
}

func PlayInstrument(i Instrument) {
	i.Play()
}

type Guitar struct {
	Type string
}

func (g Guitar) Play() {
	fmt.Println("Guitar Sounds")
}

func main() {
	g := Guitar{"Classical"}
	PlayInstrument(g)
}

// Constructors
type Customer struct {
	Name string
	Age  int
}

func (c *Customer) NewCustomer(name string, age int) {
	c.Name = name
	c.Age = age
}

func main() {
	customer := new(Customer)
	customer.NewCustomer("John", 30)
	fmt.Printf("%s: %d\n", customer.Name, customer.Age)
}

// Inheritance
type Vehicle struct {
	Seats int
	Color string
}

type Car struct {
	Vehicle
}

type MotorCycle struct {
	Base Vehicle
}

func main() {
	car := &Car{
		Vehicle{
			Seats: 4,
			Color: "blue",
		},
	}

	fmt.Println(car.Seats)
	fmt.Println(car.Color)

	motorCycle := &MotorCycle{
		Vehicle{
			Seats: 2,
			Color: "red",
		},
	}

	fmt.Println(motorCycle.Base.Seats)
	fmt.Println(motorCycle.Base.Color)
}

// Encapsulation
type Customer struct {
	id   int
	name string
}

func (c *Customer) GetID() int {
	return c.id
}

func (c *Customer) GetName() string {
	return c.name
}

// Enums
const (
	Guitar = iota // 0
	Violin        // 1
	Piano         // 2
	Drums         // 3
)
