"""Module rmvit. Implements removit logic."""
from urllib.error import HTTPError
from praw.models import Comment, Listing, ListingGenerator
import praw
import prawcore
from src import reddit as r


def rmvit(write_flag: bool = False):
    """rmvit function executes removit logic. It receives a flag that indicates which Reddit
    instance will be used.
    False means a read_only_reddit_instance will be used.
    True means a reddit_instance with write access will be used.
    """
    try:
        listing = get_comments(write_flag)
        iterate_and_delete(comments=listing)
    except HTTPError as err:
        print(err)
    except prawcore.exceptions.Forbidden as exception:
        print(exception)
    except praw.exceptions.RedditAPIException as exception:
        for subexception in exception.items:
            print(subexception)
    except praw.exceptions.ClientException as exception:
        print(exception)


def get_comments(write_flag: bool = False, n_of_comments: int = None) -> ListingGenerator:
    """get_comments function return a Listing of username's comments.
    The environment variable NUMBER_OF_COMMENTS will define how this function works.
    If NUMBER_OF_COMMENTS is 0, then get_comments will return all of username's comments.
    Otherwise, will return the stipulated number.
    """
    number = int(r.NUMBER_OF_COMMENTS)
    if write_flag is False:
        if number >= 1:
            com = r.read_only_reddit_instance.redditor(r.USERNAME).comments.new(limit=number)
            return com
        com = r.read_only_reddit_instance.redditor(r.USERNAME).comments.new(limit=n_of_comments)
        return com

    if number >= 1:
        com = r.reddit_instance.redditor(r.USERNAME).comments.new(limit=number)
        return com
    com = r.reddit_instance.redditor(r.USERNAME).comments.new(limit=n_of_comments)
    return com


def iterate_and_delete(comments: Listing) -> None:
    """iterate_and_delete function iterates over the Listing of comments
    and depending on the environment variables set, delete.
    """
    for comment in comments:
        if not isinstance(comment, Comment):
            continue

        print(f"[ID]: {comment.id} - [SCORE]: {comment.score}")

        print(type(r.DELETE_SAVED))
        if comment.score <= int(r.MINIMUM_KARMA):
            if (comment.saved is False) or (comment.saved is True and r.DELETE_SAVED is True):
                print("[DELETING]:", comment.author, comment.body)
                comment.delete()
