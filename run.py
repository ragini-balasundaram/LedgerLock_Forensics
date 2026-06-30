from app import create_app

# Generate the app instance from our factory
app = create_app()

if __name__ == '__main__':
    # Run the app in debug mode so it auto-reloads when we change code
    app.run(debug=True)
    