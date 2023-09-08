def print_error(message: str, error: Exception, icon: str = "❌"):
	print(f"{icon} {message}: {error}")


def print_saved(file: str, icon: str = "✔"):
	print(f"{icon} Saved {file}")
