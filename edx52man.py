# coding: utf-8


import invoke
import argparse
import os
import platform

from config import source_location, pr_location, bindings_location, elite_base
from config import filename_binds, filename_profile, filename_profile_custom
from config import filename_colors_default  # Adding colors


# TODO: Refactoring everything to use a single datastructure.
# The goal: simplify the code more.
# How: aggregating all the sources and destinations on a dict we can iter on.

locations = {
    "profile": {
        "deploy": os.path.join(pr_location, filename_profile),
        "collect": os.path.join(source_location, filename_profile)
    },
    "bindings": {
        "deploy": os.path.join(bindings_location, filename_binds),
        "collect": os.path.join(source_location, filename_binds)
    },
    "colors": {
        "deploy": os.path.join(elite_base, "Graphics", filename_colors_default),
        "collect": os.path.join(source_location, "Graphics", filename_colors_default)
    }
}


# trying to do an installer for the files, with auto retrieve for updates
def locations_exist():
    """verify that all locations (filename locations) exist"""
    # TODO: perform this checks on all dirs after initial setup
    # this are all the locations for the files. the source, where all lives,
    # and pr and elite where the saitek tool's and elite's folders are.
    for loc in locations:
        for action in ["collect", "deploy"]:
            folder = os.path.dirname(locations[loc][action])
            a = os.path.isdir(folder)
            if not a:
                print(f"Failed to find {folder}")
    return a


def cp(a, b):
    """run a copy file from a to b"""
    system = platform.system()
    if system == "Linux" or system == "Darwin":
        c = invoke.run('cp "{}" "{}" '.format(a, b), warn=True)
    elif system == "Windows":
        c = invoke.run('copy "{}" "{}" '.format(a, b), warn=True)
    else:
        raise Exception(f"Unsupported OS {system}")
    return c


def copy(a, b):
    """ A nicer wrapper around cp for error control"""
    out = cp(a, b)
    if not out.ok:
        print("FAIL: Some shit went wrong on deployment")
        print(repr(c))
        print(d)
    return out.ok


def collect_files():
    """ Get all the files, iterating over a dict"""
    locate = locations  # us this global
    origin = "deploy"  # The source is the place where we deploy
    destination = "collect"  # Our destination, is the place where we colect
    for loc in locate:
        source = locate[loc][origin]
        target = locate[loc][destination]
        assert copy(source, target)
    invoke.run("git diff")


def deploy_files():
    """ Get all the files, iterating over a dict"""
    locate = locations  # us this global
    source = "collect"  # The source is the repo
    target = "deploy"  # Our destination, is where it's used
    diff = invoke.run("git diff")
    for loc in locate:
        print(f"Moving {loc}")
        try:
            # Copy the files.
            src_file = locate[loc][source]
            tgt_file = locate[loc][target]
            assert copy(src_file, tgt_file)
        except KeyError as e:
            print(f"Failing to copy {loc}")
            print(locate)
            raise e


def check_files():
    """verify that all is good with the files and if they have changes"""
    if locations_exist():
        a = invoke.run("git status")
    return a.ok


if __name__ == "__main__":
    # and then do all the argparse stuff
    a = argparse.ArgumentParser(
        description="manage your ED config files, to make it easier to have your files under version control")
    a.add_argument("operation", nargs="?", help="Choose to 'deploy' or 'collect' the files", choices=(
        "deploy", "collect", "check"), default="check")
    # TODO: Add an argument to support a custom name for the settings, with like a nick or something
    # a.title="choose to deploy or collect the files modified by E:D or Profile Editor"

    opts = a.parse_args()

    if not locations_exist():
        print("WTF Dude, create the folders you need to work")
        # TODO: Have a nicer way of addressing the creation of files and folders, and asking the user.
        exit(1)

    perform = {
        "deploy": deploy_files,
        "collect": collect_files,
        "check": check_files,
    }
    perform[opts.operation]()
