# CS50-Wiki

## Project: Wikipedia-like Online Encyclopedia

This project is a simple online encyclopedia, inspired by Wikipedia. Users can view and create encyclopedia entries on various topics. Entries are stored in a lightweight, human-friendly markup language called Markdown and are converted to HTML for display.

## Project Overview

The project consists of the following components:

### URL Configuration

The URL configuration is defined in the `encyclopedia/urls.py` file. It includes a default route associated with the `views.index` function.

### Util Functions

The `encyclopedia/util.py` file contains three useful functions:

- `list_entries`: Returns a list of the names of all encyclopedia entries.
- `save_entry`: Saves a new encyclopedia entry, given its title and Markdown content.
- `get_entry`: Retrieves an encyclopedia entry by its title, returning its Markdown content if the entry exists, or None if it does not.

### Encyclopedia Entries

Each encyclopedia entry is stored as a Markdown file inside the `entries/` directory. Sample entries are provided, and you can add more entries as needed.

### Views

The `encyclopedia/views.py` file includes views for key functionality, including:

- `index`: Displays a list of all encyclopedia entries.
- Entry Viewing: Allows users to view encyclopedia entries by visiting a URL with the entry's title.
- Entry Creation: Users can create new encyclopedia entries.

### Templates

Templates are located in the `encyclopedia/templates/` directory. The primary template, `encyclopedia/index.html`, provides an interface for viewing entries and searching. The `layout.html` template defines the overall structure of the pages.

## Key Functionality

- **View Encyclopedia Entry**: Users can view an encyclopedia entry by visiting a URL with the entry's title. The Markdown content is converted to HTML for display.

- **List Entries**: Users can see a list of all encyclopedia entries on the main page.

- **Search**: Users can search for entries by typing a query into the search field (not yet implemented).

- **Create New Entry**: Users can create a new encyclopedia entry.

- **Random Page**: Users can visit a random encyclopedia page.

## Usage

1. Start the Django development server.
2. Open your web browser and navigate to the project's URL.
3. You can view encyclopedia entries, create new entries, and explore the provided functionality.
