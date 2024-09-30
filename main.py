def user_profile(**kwargs):
    """
    Creates a formatted user profile string based on the provided keyword arguments.

    Parameters:
       **kwargs: Variable number of keyword arguments representing user data.

    Returns:
        str: A formatted string containing all the provided user data.
    """
    ...


if __name__ == "__main__":
    # Teste deine Funktion
    print(
        user_profile(name="Alice", age=30)
    )  # Erwarteter Output: "Name: Alice, Age: 30"
