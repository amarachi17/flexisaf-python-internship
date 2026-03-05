import requests

def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    try:
        print("Fetching data from API.....")

        response = requests.get(url, timeout=5)

        # Raise error if response code is not successful
        response.raise_for_status()

        data = response.json()

        print("\n API Response Received Successfully! ")
        print("Title:", data["title"])
        print("Body:", data["body"])

    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please try again later.")

    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the API. Check your internet connection.")

    except requests.exceptions.HTTPError as error:
        print(f"HTTP Error occurred: {error}")

    except ValueError:
        print("Error: Invalid response received from the API.")

    except Exception as error:
        print(f"Unexpected error occurred: {error}")


if __name__ == "__main__":
    fetch_data()
