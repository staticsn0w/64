from .DataJS import DataJS
from copy import deepcopy
import discord
import os
import argparse


default_path = "config/login.json"


class Setup:

    def __init__(self, path=default_path, parse_args=True):
        self.path = path
        self.check_folders()
        self.default_settings = {
            "TOKEN": None,
            "EMAIL": None,
            "PASSWORD": None,
            "INVOKER": []
            }
        self._memory_only = False

        if not DataJS.is_valid_json(self.path):
            self.bot_settings = deepcopy(self.default_settings)
            self.save_settings()
        else:
            current = DataJS.load_json(self.path)
            if current.keys() != self.default_settings.keys():
                for key in self.default_settings.keys():
                    if key not in current.keys():
                        current[key] = self.default_settings[key]
                        print("Adding " + str(key) +
                              " field to config.json")
                DataJS.save_json(self.path, current)
            self.bot_settings = DataJS.load_json(self.path)


    def parse_cmd_arguments(self):
        parser = argparse.ArgumentParser(description="Eagle - Discord Selfbot")
        parser.add_argument("--memory-only",
                            action="store_true",
                            help="Arguments passed and future edits to the "
                                 "settings will not be saved to disk")
        parser.add_argument("--dry-run",
                            action="store_true",
                            help="Makes Red quit with code 0 just before the "
                                 "login. This is useful for testing the boot "
                                 "process.")
        parser.add_argument("--debug",
                            action="store_true",
                            help="Enables debug mode")

        args = parser.parse_args()


        self.no_prompt = args.no_prompt
        self._memory_only = args.memory_only
        self.debug = args.debug
        self._dry_run = args.dry_run

        self.save_settings()

    def check_folders(self):
        folders = ("data", os.path.dirname(self.path), "cogs", "cogs/utils")
        for folder in folders:
            if not os.path.exists(folder):
                print("Creating " + folder + " folder...")
                os.makedirs(folder)

    def save_settings(self):
        if not self._memory_only:
            DataJS.save_json(self.path, self.bot_settings)

    @property
    def token(self):
        return os.environ.get("EAGLE_TOKEN", self.bot_settings["TOKEN"])

    @token.setter
    def token(self, value):
        self.bot_settings["TOKEN"] = value
        self.bot_settings["EMAIL"] = None
        self.bot_settings["PASSWORD"] = None

    @property
    def email(self):
        return os.environ.get("EAGLE_EMAIL", self.bot_settings["EMAIL"])

    @email.setter
    def email(self, value):
        self.bot_settings["EMAIL"] = value
        self.bot_settings["TOKEN"] = None

    @property
    def password(self):
        return os.environ.get("EAGLE_PASSWORD", self.bot_settings["PASSWORD"])

    @password.setter
    def password(self, value):
        self.bot_settings["PASSWORD"] = value

    @property
    def login_credentials(self):
        if self.token:
            return (self.token,)
        elif self.email and self.password:
            return (self.email, self.password)
        else:
            return tuple()

