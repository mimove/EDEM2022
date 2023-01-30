package main

import (
	"fmt"
	"log"
	"net/http"
	"io/ioutil"
)

func handler(w http.ResponseWriter, r *http.Request) {
	file, err := ioutil.ReadFile("./snake.html")
	if err != nil {
	  fmt.Print(err)
	}
	log.Print("Serving the body")
	log.Print(string(file))
	body := string(file)
	fmt.Fprintf(w, body)
}

func main() {
	log.Print("Hello world webapp started.")

	http.HandleFunc("/", handler)

	port := "8080"

	log.Fatal(http.ListenAndServe(fmt.Sprintf(":%s", port), nil))
}