def kilometer_to_mile(kilometers):
    """Convert kilometers to miles."""
    miles = kilometers * 0.6214
    return miles

def main():
    """Main function to run the kilometer to mile converter."""
    try:
        kilometers = float(input("Enter distance in kilometers: "))
        miles = kilometer_to_mile(kilometers)
        print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
