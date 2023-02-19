"""Module removit_test. Implements test for removit module."""
from praw.models import Comment, ListingGenerator
import praw
from src import reddit as r
from src import removit as rmvit


def test_rmvit():
    """test_rmvit function tests if rmvit executes removit logic."""
    try:
        rmvit.rmvit(write_flag=False)
    except praw.exceptions.RedditAPIException as exception:
        assert exception.items[0].error_type == "USER_REQUIRED"
        assert exception.items[0].message == "Please log in to do that."


def test_get_comments():
    """test_get_comments function tests if get_comments function get a stipulated number 
    of comments.
    """
    r.NUMBER_OF_COMMENTS = 1
    test_subject = rmvit.get_comments(write_flag=False)

    assert isinstance(test_subject, ListingGenerator) is True
    assert test_subject.limit == 1
    for i, comment in enumerate(test_subject):
        assert isinstance(comment, Comment) is True
        assert comment.author == r.USERNAME
        assert i < test_subject.limit

    r.NUMBER_OF_COMMENTS = 5
    test_subject = rmvit.get_comments(write_flag=False)
    assert isinstance(test_subject, ListingGenerator) is True
    assert test_subject.limit == 5
    for i, comment in enumerate(test_subject):
        assert isinstance(comment, Comment) is True
        assert comment.author == r.USERNAME
        assert i < test_subject.limit


def test_iterate_and_delete():
    """test_iterate_and_delete function tests if iterate_and_delete function 
    send delete requests.
    """
    r.NUMBER_OF_COMMENTS = 1
    listing = rmvit.get_comments(write_flag=False)
    assert listing.limit == 1
    for i, comment in enumerate(listing):
        assert isinstance(comment, Comment) is True
        print(comment.score)
        assert comment.author == r.USERNAME
        assert i < listing.limit

    try:
        rmvit.iterate_and_delete(comments=listing)
    except praw.exceptions.RedditAPIException as exception:
        assert exception.items[0].error_type == "USER_REQUIRED"
        assert exception.items[0].message == "Please log in to do that."
