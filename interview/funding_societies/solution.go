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

func (s SubCategory) Add(categoryName string, root *Category) *SubCategory {
	cat := SubCategory{Parent: root, Name: categoryName}
	if s.Parent != nil {
		cat.Parent = s.Parent
	}
	return &cat
}

func (s SubCategory) Move(root *Category, parent *Category) *SubCategory {
	cat := SubCategory{Parent: root}
	if parent != nil {
		cat.Parent = parent
	}
	return &cat
}

func (s SubCategory) Find(name string) *Category {
	if s.Name == name {
		return s.Parent
	}
	parent := s.Find(name)
	return parent
}

func (s SubCategory) Get(categoryMap map[string]*SubCategory) string {
	categoryList := make([]string, 0)
	catName := s.Name

	cat, exists := categoryMap[catName]
	if exists && cat.Parent != nil {
		catName := cat.Parent.Name
		categoryList = append(categoryList, catName)
	}
	categoryList = append(categoryList, catName)
	return strings.Join(categoryList, " -> ")
}

func main() {
	commands := []string{"ADD_PRODUCT_CATEGORY MOBILES", "GET_PRODUCT_CATEGORY MOBILES", "ADD_PRODUCT_CATEGORY ANDROID MOBILES", "ADD_PRODUCT_CATEGORY IOS MOBILES", "GET_PRODUCT_CATEGORY IOS"}
	root := &Category{Name: "ALL_PRODUCTS"}
	operation := SubCategory{Parent: root}
	categoryMap := make(map[string]*SubCategory, 0)

	for _, c := range commands {
		for subcatName, catObj := range categoryMap {
			fmt.Println(subcatName)
			if catObj.Parent != nil {
				fmt.Println(catObj.Parent.Name)
			}
		}
		command := strings.Split(c, " ")
		op := command[0]
		subcategories := command[1:]

		switch op {
		case "ADD_PRODUCT_CATEGORY":
			if len(subcategories) == 1 {
				cat := operation.Add(subcategories[0], root)
				categoryMap[cat.Name] = cat
			}
			if len(subcategories) == 2 {
				categoryName, parentCategoryName := subcategories[0], subcategories[1]
				parentCat, exists := categoryMap[parentCategoryName]
				if exists {
					cat := parentCat.Add(categoryName, parentCat.Parent)
					categoryMap[categoryName] = cat
				} else {
					cat := operation.Add(categoryName, root)
					categoryMap[categoryName] = cat
				}
			}

		case "MOVE_PRODUCT_CATEGORY":
			categoryName, parentCategoryName := subcategories[0], subcategories[1]
			cat := categoryMap[categoryName]
			parentCategory := categoryMap[parentCategoryName]
			cat.Move(root, parentCategory.Parent)
		case "GET_PRODUCT_CATEGORY":
			categoryName := subcategories[0]
			cat := categoryMap[categoryName]
			fmt.Println(cat.Get(categoryMap))
		}
	}
}
