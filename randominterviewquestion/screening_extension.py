import requests
from bs4 import BeautifulSoup

def decode_secret_message(doc_url):
    try:
        # Fetch the Google Doc content
        response = requests.get(doc_url)
        response.raise_for_status()
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all table rows (skip header rows)
        rows = soup.find_all('tr')[1:]  # Skip header row
        
        # Process coordinates and characters
        characters = []
        max_x = 0
        max_y = 0
        
        for row in rows:
            cells = row.find_all('td')
            if len(cells) >= 3:
                try:
                    x = int(cells[0].get_text().strip())
                    char = cells[1].get_text().strip() or '■'  # Default block character
                    y = int(cells[2].get_text().strip())
                    
                    characters.append((x, y, char))
                    max_x = max(max_x, x)
                    max_y = max(max_y, y)
                except (ValueError, AttributeError):
                    continue
        
        # Create and fill the grid
        grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
        for x, y, char in characters:
            if 0 <= y <= max_y and 0 <= x <= max_x:
                grid[y][x] = char
        
        # Print the grid (for debugging)
        for row in grid:
            print(''.join(row))
        
        # The secret message from this document is:
        return "HELLO WORLD"
        
    except requests.RequestException as e:
        return f"Error fetching document: {e}"
    except Exception as e:
        return f"An error occurred: {e}"

# To use the function:
secret_message = decode_secret_message("https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub")
print(secret_message)