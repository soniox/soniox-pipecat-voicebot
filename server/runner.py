#
# Copyright (c) 2024–2025, Daily
#
# SPDX-License-Identifier: BSD 2-Clause License
#

import argparse
import asyncio
import os

from bot import bot
from pipecatcloud.agent import DailySessionArguments


def main():
    """Parse the args to launch the appropriate bot using the given room/token."""
    parser = argparse.ArgumentParser(description="Pipecat Bot Runner Example")
    parser.add_argument("-u", "--url", type=str, required=False, help="Daily room URL")
    parser.add_argument(
        "-t",
        "--token",
        type=str,
        required=False,
        help="Daily room token",
    )

    args, unknown = parser.parse_known_args()

    url = args.url or os.getenv("DAILY_SAMPLE_ROOM_URL")
    token = args.token or os.getenv("DAILY_SAMPLE_ROOM_TOKEN")

    if not url:
        raise Exception(
            "No Daily room specified. use the -u/--url option from the command line, or set DAILY_SAMPLE_ROOM_URL in your environment to specify a Daily room URL."
        )

    # Create session arguments and run the bot
    session_args = DailySessionArguments(
        room_url=url,
        token=token,
        body={},  # Empty config for local testing
        session_id=None,  # No session ID needed for local testing
    )

    asyncio.run(bot(session_args))


if __name__ == "__main__":
    main()
