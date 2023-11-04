"""Module providing the contents for the 'main.go' file."""

GO_MAIN_CONTENTS = """package main

import (
    "fmt"
    "log"
)

func main() {
    fmt.Println("hello world")

    srv := createServer()

    log.Print("Starting server on port #8000")
    log.Fatal(srv.ListenAndServe())
}"""
