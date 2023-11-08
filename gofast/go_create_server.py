"""Module providing the contents for the 'create_server.go' file."""

GO_CREATE_SERVER_CONTENTS = '''package main

import (
	"net/http"
	"time"

	"github.com/go-chi/chi/v5"
	"github.com/go-chi/cors"
)

func createServer() *http.Server {
	r := chi.NewRouter()
	r.Use(cors.Handler(cors.Options{
		AllowedOrigins: []string{"https://*", "http://*"},
		AllowedMethods: []string{"GET", "POST", "PUT", "DELETE", "OPTIONS"},
		AllowedHeaders: []string{
			"Accept",
			"Authorization",
			"Content-Type",
			"X-CSRF-Token",
		},
		ExposedHeaders:   []string{"Link"},
		AllowCredentials: false,
		MaxAge:           300,
	}))

	v1router := chi.NewRouter()

	//v1router.Get("/readiness", handlerReadiness)
	//v1router.Get("/healthz", handlerReadiness)
	//v1router.Get("/err", handlerErr)

	r.Mount("/v1", v1router)

	return &http.Server{
		Handler:           r,
		Addr:              "localhost:8000",
		ReadHeaderTimeout: 10 * time.Second,
		WriteTimeout:      30 * time.Second,
		ReadTimeout:       30 * time.Second,
	}
}
'''
