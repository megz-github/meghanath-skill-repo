def make_shirt(size="large", message="Bathspa"):
    summary = f"Made a {size}-sized shirt with the message: '{message}'."
    print(summary)

# Create a large shirt with the default message
make_shirt()
# Create a medium shirt with the default message
make_shirt(size="medium")
# Create a custom-sized shirt with a different message
make_shirt(size="small", message="Bathspa")
