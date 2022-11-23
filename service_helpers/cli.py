#!/usr/bin/env python
import os

import click

from .chromedriver import chromedriver
from .compare import compare
from .refresh import login, refresh


@click.group()
def cli():
    pass


@cli.command(name="chromedriver", help="Update chromedriver to latest compatible version")
def click_chromedriver() -> None:
    chromedriver(path=os.getcwd())


@cli.command(name="login", help="Setup Selenium by Logging into Django Admin")
def click_login() -> None:
    print("Logging in, press ctrl+c when finished")
    login()


@cli.command(name="refresh", help="Run Refresh Function")
@click.option("--filename", help="Specify the filename to run")
@click.option("--kind", default="csv", help="Should be one of tableau or csv")
def click_refresh(filename, kind) -> None:
    refresh(filename, kind)


@cli.command(name="compare", help="Run Compare Function")
def click_compare() -> None:
    compare()


if __name__ == "__main__":
    cli()
