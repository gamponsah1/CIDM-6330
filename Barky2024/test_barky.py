# test_barky.py

import pytest
from unittest.mock import patch, MagicMock
import io

import barky


@pytest.fixture
def mock_input(monkeypatch):
    user_input = io.StringIO()
    monkeypatch.setattr('sys.stdin', user_input)
    return user_input


def test_add_bookmark(mock_input):
    # Mock user input for adding a bookmark
    mock_input.write('A\n')  # Choose 'Add a bookmark'
    mock_input.write('My Bookmark\n')  # Enter bookmark title
    mock_input.write('http://example.com\n')  # Enter bookmark URL
    mock_input.write('This is a test bookmark\n')  # Enter bookmark notes
    mock_input.seek(0)

    with patch('barky.clear_screen'), \
         patch('commands.AddBookmarkCommand.execute', MagicMock()) as mock_execute:
        # Run loop
        barky.loop()

    # Verify that the AddBookmarkCommand.execute method was called with the correct data
    mock_execute.assert_called_once_with({
        "title": "My Bookmark",
        "url": "http://example.com",
        "notes": "This is a test bookmark"
    })


def test_list_bookmarks(mock_input):
    # Mock user input for listing bookmarks by date
    mock_input.write('B\n')  # Choose 'List bookmarks by date'
    mock_input.seek(0)

    with patch('barky.clear_screen'), \
         patch('commands.ListBookmarksCommand.execute', MagicMock(return_value=[])) as mock_execute:
        # Run loop
        barky.loop()

    # Verify that the ListBookmarksCommand.execute method was called
    mock_execute.assert_called_once()


def test_edit_bookmark(mock_input):
    # Mock user input for editing a bookmark
    mock_input.write('E\n')  # Choose 'Edit a bookmark'
    mock_input.write('1\n')  # Enter bookmark ID to edit
    mock_input.write('title\n')  # Choose field to edit
    mock_input.write('New Title\n')  # Enter new value for the field
    mock_input.seek(0)

    with patch('barky.clear_screen'), \
         patch('commands.EditBookmarkCommand.execute', MagicMock()) as mock_execute:
        # Run loop
        barky.loop()

    # Verify that the EditBookmarkCommand.execute method was called with the correct data
    mock_execute.assert_called_once_with({
        "id": "1",
        "update": {"title": "New Title"}
    })


def test_delete_bookmark(mock_input):
    # Mock user input for deleting a bookmark
    mock_input.write('D\n')  # Choose 'Delete a bookmark'
    mock_input.write('1\n')  # Enter bookmark ID to delete
    mock_input.seek(0)

    with patch('barky.clear_screen'), \
         patch('commands.DeleteBookmarkCommand.execute', MagicMock()) as mock_execute:
        # Run loop
        barky.loop()

    # Verify that the DeleteBookmarkCommand.execute method was called with the correct data
    mock_execute.assert_called_once_with("1")


def test_import_github_stars(mock_input):
    # Mock user input for importing GitHub stars
    mock_input.write('G\n')  # Choose 'Import GitHub stars'
    mock_input.write('my_username\n')  # Enter GitHub username
    mock_input.write('Y\n')  # Choose to preserve timestamps
    mock_input.seek(0)

    with patch('barky.clear_screen'), \
         patch('commands.ImportGitHubStarsCommand.execute', MagicMock()) as mock_execute:
        # Run loop
        barky.loop()

    # Verify that the ImportGitHubStarsCommand.execute method was called with the correct data
    mock_execute.assert_called_once_with({
        "github_username": "my_username",
        "preserve_timestamps": True
    })



