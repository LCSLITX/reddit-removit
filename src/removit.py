"""Module rmvit. Implements removit logic."""
from praw.models import Comment, Listing
from src import reddit as r


def rmvit():
    """rmvit function executes removit logic."""
    listing = get_comments()
    iterate_and_delete(listing)


def get_comments(number_of_comments = None) -> Listing:
    """get_comments function return a Listing of username's comments.
    The environment variable NUMBER_OF_COMMENTS will define how this function works.
    If NUMBER_OF_COMMENTS is 0, then get_comments will return all of username's comments.
    Otherwise, will return the stipulated number.
    """
    number = int(r.NUMBER_OF_COMMENTS)
    if number >= 1:
        comments = r.reddit_instance.redditor(r.USERNAME).comments.new(limit=number)
        return comments
    comments = r.reddit_instance.redditor(r.USERNAME).comments.new(limit=number_of_comments)
    return comments


def iterate_and_delete(comments: Listing):
    """iterate_and_delete function iterates over the Listing of comments
    and depending on the environment variables set, delete.
    """
    for comment in comments:
        if not isinstance(comment, Comment):
            continue

        print(f"[ID]: {comment.id} - [SCORE]: {comment.score}")

        if comment.score <= int(r.MINIMUM_KARMA):
            if (comment.saved is False) or (comment.saved is True and r.DELETE_SAVED is True):
                print("[DELETING]:", comment.author, comment.body)
                comment.delete()
