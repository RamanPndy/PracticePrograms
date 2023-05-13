// You can edit this code!
// Click here and start typing.
package main

import (
	"fmt"
	"strings"
)

type Category struct {
	Name string
}

type SubCategory struct {
	Parent *Category
	Name   string
}

type operation interface {
	Add(string, *Category) *SubCategory
	Move(*Category, *Category) *SubCategory
	Get() string
	Find(string) *SubCategory
}

func (s Subcategory) Add(string categoryName, Category *root) *Subcategory {
	cat := SubCategory{Parent: root, Name: categoryName}
	if s.Parent != nil {
		cat.Parent = s.Parent
	}
	return &cat
}

func (Subcategory s) Move(Category *root, Category *parent) *Subcategory {
	cat := SubCategory{Parent: root}
	if parent != nil {
		cat.Parent = Parent
	}
	return &cat
}

func (Subcategory s) Find(string name) *SubCategory {
	if s.Name == name {
		return s.Parent
	}
	parent := s.Find(name)
	return parent
}

func (Subcategory s) Get(categoryMap map[string]*Subcategory) string {
	categoryList := make([]string, 0)
	catName := s.Name
	while(catName != "")
	{
		cat, exists := categoryMap[catName]
		if exists && cat.Parent != nil {
			catName := cat.Parent.Name
			categoryList = append(categoryList, catName)
		}
	}
	categoryList = append(categoryList, s.Name)
	return strings.Join(categoryList, " -> ")
}

func main() {
	commands = []string{"ADD_PRODUCT_CATEGORY MOBILES", "GET_PRODUCT_CATEGORY MOBILES", "ADD_PRODUCT_CATEGORY ANDROID MOBILES", "ADD_PRODUCT_CATEGORY IOS MOBILES", "GET_PRODUCT_CATEGORY IOS"}
	operation := SubCategory{Parent: nil, Name: "ALL_PRODUCTS"}
	categoryMap := make(map[string]*Subcategory, 0)

	for c := range commands {
		command := strings.Split(c, " ")
		operation := command[0]
		subcateogries := command[1:]

		switch operation {
		case "ADD_PRODUCT_CATEGORY":
			if len(subcateogries) == 1 {
				cat := operation.Add(subcateogries[0], root)
				categoryMap[cat.Name] = cat
			}
			if len(subcateogries) == 2 {
				categoryName, parentCategoryName := subcateogries[0], subcateogries[1]
				parentCat, exists := categoryMap[parentCategoryName]
				if exists {
					cat := parentCat.Add(categoryName, parentCat)
					categoryMap[categoryName] = cat
				} else {
					cat := root.Add(categoryName, root)
					categoryMap[categoryName] = cat
				}
			}

		case "MOVE_PRODUCT_CATEGORY":
			categoryName, parentCategoryName := subcateogries[0], subcateogries[1]
			cat := categoryMap[categoryName]
			parentCategory := categoryMap[parentCategoryName]
			cat.Move(root, parentCategory)
		case "GET_PRODUCT_CATEGORY":
			categoryName := subcateogries[0]
			cat := categoryMap[categoryName]
			fmt.Println(cat.Get(categoryMap))
		}
	}
}
